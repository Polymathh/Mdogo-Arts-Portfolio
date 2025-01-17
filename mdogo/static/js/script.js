document.addEventListener("DOMContentLoaded", () => {
    console.log("JavaScript is loaded!");

    const navToggle = document.querySelector(".nav-toggle");
    const navLinks = document.querySelector(".nav-links");

    // Toggle the menu when the hamburger is clicked
    navToggle.addEventListener("click", () => {
        navLinks.classList.toggle("active");
    });

    // Close the menu when any link is clicked
    navLinks.querySelectorAll("a").forEach(link => {
        link.addEventListener("click", () => {
            navLinks.classList.remove("active");
        });
    });
});
