import os
import re

# Master Navbar Template (Symmetrical Layout)
# We will dynamicallly set the "active" class based on the filename later.
NAVBAR_TEMPLATE = """    <nav class="sticky top-0 w-full z-50 glass-nav">
        <div class="nav-container">
            <!-- Logo Section -->
            <a href="index.html" class="flex items-center group">
                <img width="343" height="96" loading="eager" src="uploads/logo.png"
                    alt="Sivam Itech Metal Forming Industries Official Logo"
                    class="h-20 md:h-28 lg:h-32 w-auto object-contain transition-transform duration-500 group-hover:scale-105">
            </a>

            <!-- Navigation Links - Centered Pill -->
            <div class="hidden lg:flex items-center justify-center flex-grow">
                <div class="nav-pill-wrapper">
                    <a href="index.html" class="nav-link {index_active}">Home</a>
                    <a href="about.html" class="nav-link {about_active}">About Us</a>
                    <a href="infrastructure.html" class="nav-link {infrastructure_active}">Infrastructure</a>
                    <a href="products.html" class="nav-link {products_active}">Products</a>
                    <a href="careers.html" class="nav-link {careers_active}">Careers</a>
                    <a href="contact.html" class="nav-link {contact_active}">Contact Us</a>
                </div>
            </div>

            <!-- CTA Section -->
            <div class="flex items-center gap-6">
                <a href="inquire.html"
                    class="hidden md:flex btn-orange-premium px-8 py-3 text-xs font-bold uppercase tracking-widest rounded-full">
                    Inquire Now
                </a>

                <!-- Mobile Menu Button -->
                <button type="button" id="mobile-menu-btn"
                    class="lg:hidden p-2 text-gray-700 hover:text-brand-orange transition-all duration-300"
                    title="Toggle mobile menu">
                    <i data-lucide="menu" class="w-7 h-7"></i>
                </button>
            </div>
        </div>

        <!-- Mobile Menu -->
        <div id="mobile-menu">
            <div class="px-8 py-6 flex flex-col h-full bg-white/95">
                <a href="index.html" class="nav-link-mobile {index_active}">Home</a>
                <a href="about.html" class="nav-link-mobile {about_active}">About Us</a>
                <a href="infrastructure.html" class="nav-link-mobile {infrastructure_active}">Infrastructure</a>
                <a href="products.html" class="nav-link-mobile {products_active}">Products</a>
                <a href="careers.html" class="nav-link-mobile {careers_active}">Careers</a>
                <a href="contact.html" class="nav-link-mobile {contact_active}">Contact Us</a>
                <a href="inquire.html" class="btn-orange-premium px-8 py-4 text-center mt-8 rounded-xl shadow-xl">Inquire Now</a>
            </div>
        </div>
    </nav>"""

def update_navbar(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(file_path)
    
    # Determine active page
    context = {
        'index_active': 'active' if filename == 'index.html' else '',
        'about_active': 'active' if filename == 'about.html' else '',
        'infrastructure_active': 'active' if filename == 'infrastructure.html' else '',
        'products_active': 'active' if filename == 'products.html' else '',
        'careers_active': 'active' if filename in ['careers.html', 'application.html'] else '',
        'contact_active': 'active' if filename == 'contact.html' else '',
    }
    
    new_nav = NAVBAR_TEMPLATE.format(**context)
    
    # Use regex to find the <nav> block and replace it
    # This regex is broad enough to catch different nav blocks
    new_content = re.sub(r'<nav.*?>.*?</nav>', new_nav, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No changes for {filename}")

if __name__ == "__main__":
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for file in html_files:
        update_navbar(file)
