#!/usr/bin/env python3
"""Refresh the homepage Google Scholar snapshot from the public author profile."""

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode, urljoin
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
DATA_PATHS = [ROOT / "_data/scholar_impact.json", ROOT / "assets/data/scholar_impact.json"]
SCHOLAR_ID_FILE = ROOT / "_data/socials.yml"


def scholar_id():
    match = re.search(r"^scholar_userid:\s*([\w-]+)", SCHOLAR_ID_FILE.read_text(), re.MULTILINE)
    if not match:
        raise ValueError("Missing scholar_userid in _data/socials.yml")
    return match.group(1)


def chart_points(history):
    values = [point["total_citations"] for point in history]
    if len(values) < 2:
        return "0,35 300,35"
    low, high = min(values), max(values)
    spread = high - low
    return " ".join(
        f"{round(index * 300 / (len(values) - 1))},{round(60 - (value - low) * 50 / spread) if spread else 35}"
        for index, value in enumerate(values)
    )


def main():
    user_id = scholar_id()
    profile_url = "https://scholar.google.com/citations?" + urlencode(
        {"user": user_id, "hl": "en", "pagesize": 100}
    )
    request = Request(
        profile_url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urlopen(request, timeout=30) as response:
        soup = BeautifulSoup(response.read(), "html.parser")

    name = soup.select_one("#gsc_prf_in")
    stats = [int(cell.get_text(strip=True).replace(",", "")) for cell in soup.select("#gsc_rsb_st td.gsc_rsb_std")]
    rows = soup.select("tr.gsc_a_tr")
    if not name or len(stats) < 6 or not rows:
        raise ValueError("Google Scholar did not return a complete public author profile")

    papers = []
    for row in rows:
        title = row.select_one("a.gsc_a_at")
        if not title:
            continue
        count = row.select_one("a.gsc_a_ac")
        papers.append(
            {
                "title": title.get_text(" ", strip=True),
                "citations": int(count.get_text(strip=True).replace(",", "") or 0) if count else 0,
                "url": urljoin("https://scholar.google.com", title.get("href", "")),
            }
        )
    if not papers:
        raise ValueError("Google Scholar returned no readable publications")

    today = datetime.now(ZoneInfo("America/Los_Angeles")).date().isoformat()
    previous = json.loads(DATA_PATHS[0].read_text()) if DATA_PATHS[0].exists() else {}
    history = [point for point in previous.get("history", []) if point.get("date") != today]
    history.append({"date": today, "total_citations": stats[0]})
    history = sorted(history, key=lambda point: point["date"])[-365:]

    impact = {
        "profile": {
            "name": name.get_text(" ", strip=True),
            "scholar_id": user_id,
            "scholar_url": profile_url,
        },
        "summary": {
            "total_citations": stats[0],
            "h_index": stats[2],
            "i10_index": stats[4],
            "paper_count": len(papers),
            "updated": today,
            "updated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "source": "Google Scholar public profile",
        },
        "history": history,
        "chart_points": chart_points(history),
        "top_paper": max(papers, key=lambda paper: paper["citations"]),
    }
    if previous:
        comparable = {key: value for key, value in impact.items() if key != "summary"}
        previous_comparable = {key: value for key, value in previous.items() if key != "summary"}
        if comparable == previous_comparable and {
            key: value for key, value in impact["summary"].items() if key != "updated_at_utc"
        } == {
            key: value for key, value in previous.get("summary", {}).items() if key != "updated_at_utc"
        }:
            print("Scholar impact is already current")
            return

    payload = json.dumps(impact, ensure_ascii=False, indent=2) + "\n"
    for path in DATA_PATHS:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(payload)
    print(f"Updated Scholar impact for {impact['profile']['name']}: {stats[0]} citations")


if __name__ == "__main__":
    main()
