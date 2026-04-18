document.addEventListener('DOMContentLoaded', () => {
    // Initialize Lucide icons
    if (window.lucide) {
        lucide.createIcons();
    }

    // Handle Loader Dismissal
    window.addEventListener('load', () => {
        const loader = document.getElementById('loader');
        if (loader) {
            setTimeout(() => {
                loader.classList.add('loaded');
                setTimeout(() => {
                    loader.style.display = 'none';
                }, 500);
            }, 500);
        }
    });

    // Navbar Scroll Effect
    const nav = document.querySelector('nav');
    if (nav) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                nav.classList.add('scrolled');
            } else {
                nav.classList.remove('scrolled');
            }
        });
    }

    // Mobile Menu Toggle
    const menuButton = document.getElementById('mobile-menu-btn');
    if (menuButton) {
        menuButton.addEventListener('click', toggleMenu);
    }
});

function toggleMenu() {
    const menu = document.getElementById('mobile-menu');
    if (menu) {
        menu.classList.toggle('active');
    }
}
