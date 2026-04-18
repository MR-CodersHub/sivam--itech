import os
import re

FOOTER_TEMPLATE = """
    <!-- Footer -->
    <footer class="bg-white border-t border-gray-100">
        <div class="max-w-7xl mx-auto px-6">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-12 lg:gap-8">

                <!-- Column 1: Logo & About -->
                <div class="lg:col-span-4 space-y-8">
                    <a href="index.html" class="inline-block">
                        <img width="343" height="96" src="uploads/logo.png" alt="Sivam Itech Logo"
                            class="h-20 md:h-28 lg:h-32 w-auto object-contain">
                    </a>
                    <p class="text-zinc-600 text-[14px] leading-relaxed max-w-sm font-medium">
                        Redefining precision and synergy in the industrial sector. From concept to complex component
                        manufacturing with unmatched excellence and technical leadership.
                    </p>
                </div>

                <!-- Column 2: Company -->
                <div class="lg:col-span-2">
                    <h5 class="footer-section-title">COMPANY</h5>
                    <ul class="space-y-4 text-[14px] font-semibold text-gray-500">
                        <li><a href="about.html" class="hover:text-brand-orange transition-colors">About Us</a></li>
                        <li><a href="infrastructure.html" class="hover:text-brand-orange transition-colors">Infrastructure</a></li>
                        <li><a href="products.html" class="hover:text-brand-orange transition-colors">Products</a></li>
                        <li><a href="careers.html" class="hover:text-brand-orange transition-colors">Careers</a></li>
                        <li><a href="contact.html" class="hover:text-brand-orange transition-colors">Contact Us</a></li>
                    </ul>
                </div>

                <!-- Column 3: Connect -->
                <div class="lg:col-span-3">
                    <h5 class="footer-section-title">CONNECT</h5>
                    <div class="space-y-6">
                        <!-- Address -->
                        <div class="flex gap-4">
                            <div class="footer-icon-circle">
                                <i data-lucide="map-pin" class="w-5 h-5"></i>
                            </div>
                            <p class="text-[13px] font-bold text-gray-600 leading-relaxed">
                                No. 115 / 2A, Mahalakshmi Nagar Extension, Noombal, Chennai – 600 077, India.
                            </p>
                        </div>

                        <!-- Phone -->
                        <div class="flex gap-4">
                            <div class="footer-icon-circle">
                                <i data-lucide="phone" class="w-5 h-5"></i>
                            </div>
                            <div class="flex flex-col text-[13px] font-bold text-gray-600 space-y-1">
                                <a href="tel:+919884426111" class="hover:text-brand-orange transition-colors">+91 98844 26111</a>
                                <a href="tel:+918428283013" class="hover:text-brand-orange transition-colors">+91 84282 83013</a>
                                <a href="tel:+919000012345" class="hover:text-brand-orange transition-colors">+91 90000 12345</a>
                            </div>
                        </div>

                        <!-- Email -->
                        <div class="flex gap-4">
                            <div class="footer-icon-circle">
                                <i data-lucide="mail" class="w-5 h-5"></i>
                            </div>
                            <div class="flex flex-col text-[13px] font-bold text-gray-600 space-y-1">
                                <a href="mailto:Vijayakumar.k@sivamitech.com" class="hover:text-brand-orange transition-colors">Vijayakumar.k@sivamitech.com</a>
                                <a href="mailto:Nagendran.P@sivamitech.com" class="hover:text-brand-orange transition-colors">Nagendran.P@sivamitech.com</a>
                                <a href="mailto:info@sivamitech.com" class="hover:text-brand-orange transition-colors">info@sivamitech.com</a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Column 4: Follow & Newsletter -->
                <div class="lg:col-span-3 space-y-10">
                    <div>
                        <h5 class="footer-section-title">FOLLOW US</h5>
                        <div class="space-y-3">
                            <a href="https://www.linkedin.com/company/sivam-itech-metal-forming-industries/" target="_blank" class="footer-social-block">
                                <div class="footer-social-icon">
                                    <i class="fa-brands fa-linkedin-in text-[1.2rem] text-[#0A66C2]"></i>
                                </div>
                                <span class="text-[13px] font-bold text-gray-700">LinkedIn</span>
                            </a>
                            <a href="https://wa.me/919884426111" target="_blank" class="footer-social-block">
                                <div class="footer-social-icon">
                                    <i class="fa-brands fa-whatsapp text-[1.2rem] text-[#25D366]"></i>
                                </div>
                                <span class="text-[13px] font-bold text-gray-700">WhatsApp</span>
                            </a>
                        </div>
                    </div>

                    <div>
                        <h5 class="footer-section-title">NEWSLETTER</h5>
                        <div class="footer-newsletter-box">
                            <input type="email" placeholder="Corporate email" class="footer-newsletter-input">
                            <button class="w-10 h-10 bg-brand-orange text-white rounded-xl flex items-center justify-center hover:bg-orange-700 transition-all">
                                <i data-lucide="send" class="w-4 h-4"></i>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </footer>

    <!-- Bottom Bar -->
    <div class="footer-bottom-dark px-6">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-6">
            <div class="flex items-center gap-6">
                <a href="about.html" class="footer-bottom-link">Our History</a>
                <span class="opacity-10 text-gray-300">|</span>
                <a href="infrastructure.html" class="footer-bottom-link">What We Do</a>
                <span class="opacity-10 text-gray-300">|</span>
                <a href="contact.html" class="footer-bottom-link">Support Centre</a>
            </div>
            <div class="text-right">
                <p class="text-[11px] font-semibold text-gray-400 uppercase tracking-widest">
                    © 2024 Sivam Itech Metal Forming Industries. Precision Simplified.
                </p>
                <p class="text-[10px] text-gray-400 mt-1 font-medium italic">
                    Designed and Developed by <a href="https://mrcodershub.in/" target="_blank" class="text-brand-orange hover:underline transition-all">MR Coders Hub</a>
                </p>
            </div>
        </div>
    </div>
"""

def sync_footer(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find the whole footer and bottom bar section
    # Targets the block from '<!-- Footer -->' to the end of the legal bottom bar
    pattern = re.compile(r'<!-- Footer -->.*?© 2024 Sivam Itech Metal Forming Industries.*?</div>\s*</div>', re.DOTALL)
    
    if pattern.search(content):
        new_content = pattern.sub(FOOTER_TEMPLATE.strip(), content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated Footer in {os.path.basename(file_path)}")
    else:
        # Alt match: look for <footer and the footer-bottom-dark div
        pattern_alt = re.compile(r'<footer.*?>.*?</footer>\s*<div class="footer-bottom-dark.*?>.*?</div>\s*</div>', re.DOTALL)
        if pattern_alt.search(content):
            new_content = pattern_alt.sub(FOOTER_TEMPLATE.strip(), content)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated Footer (Alt Match) in {os.path.basename(file_path)}")

if __name__ == "__main__":
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for file in html_files:
        sync_footer(file)
