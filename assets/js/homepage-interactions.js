document.addEventListener("DOMContentLoaded", () => {
  const hero = document.getElementById("biography");
  if (!hero) return;
  const links = [...document.querySelectorAll(".home-section-link")];
  const sections = links.map((link) => document.getElementById(link.dataset.section)).filter(Boolean);
  const updateNavigation = () => {
    const current = sections.filter((section) => section.getBoundingClientRect().top <= 160).at(-1) || hero;
    links.forEach((link) => {
      const active = link.dataset.section === current.id;
      link.parentElement.classList.toggle("active", active);
      if (active) link.setAttribute("aria-current", "location");
      else link.removeAttribute("aria-current");
    });
  };
  let scheduled = false;
  window.addEventListener(
    "scroll",
    () => {
      if (scheduled) return;
      scheduled = true;
      requestAnimationFrame(() => {
        updateNavigation();
        scheduled = false;
      });
    },
    { passive: true }
  );
  updateNavigation();

  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches || !("IntersectionObserver" in window)) return;
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.remove("reveal-pending");
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.05, rootMargin: "0px 0px -30px 0px" }
  );
  const content = hero.parentElement;
  [...content.children].forEach((element) => {
    if (element === hero || !["H2", "H4", "DIV", "P"].includes(element.tagName) || element.getBoundingClientRect().top < window.innerHeight) return;
    element.classList.add("scroll-reveal", "reveal-pending");
    observer.observe(element);
  });
});
