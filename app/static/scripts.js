
gsap.registerPlugin(ScrollTrigger);


gsap.from(".hero h1", { opacity: 0, y: -50, duration: 1 });
gsap.from(".hero p", { opacity: 0, y: 50, duration: 1, delay: 0.5 });
gsap.from(".cta-button", { opacity: 0, y: 50, duration: 1, delay: 1 });


gsap.utils.toArray("section").forEach((section) => {
    gsap.from(section, {
        opacity: 0,
        y: 50,
        duration: 1,
        scrollTrigger: {
            trigger: section,
            start: "top 80%",
        },
    });
});


const skillItems = document.querySelectorAll(".skills li");
const skillDescription = document.querySelector(".skill-description");

skillItems.forEach((item) => {
    item.addEventListener("mouseenter", () => {
        const description = item.getAttribute("data-description");
        skillDescription.textContent = description;
        skillDescription.classList.add("active");
    });

    item.addEventListener("mouseleave", () => {
        skillDescription.classList.remove("active");
    });
});

// Переключатель темы
const themeToggle = document.getElementById("theme-toggle");
const body = document.body;

// Проверяем сохранённую тему в localStorage
const savedTheme = localStorage.getItem("theme");
if (savedTheme === "dark-theme") {
    body.classList.add("dark-theme");
    themeToggle.checked = true;
}

// Обработчик изменения состояния переключателя
themeToggle.addEventListener("change", () => {
    if (themeToggle.checked) {
        body.classList.add("dark-theme");
        localStorage.setItem("theme", "dark-theme");
    } else {
        body.classList.remove("dark-theme");
        localStorage.setItem("theme", "light-theme");
    }
});