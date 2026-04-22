import os
import re

def fix_html_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 1. Fix header logo classes (remove hardcoded responsive heights)
            content = re.sub(r'class="h-20 md:h-28 lg:h-32 w-auto object-contain transition-transform duration-500 group-hover:scale-105"', 
                             r'class="w-auto object-contain transition-transform duration-500 group-hover:scale-105"', 
                             content)
            # Also catch the one in the footer
            content = re.sub(r'class="h-20 md:h-28 lg:h-32 w-auto object-contain"', 
                             r'class="w-auto object-contain"', 
                             content)
            
            # 2. Remove decorative background shapes (ovals/blurs)
            # Match absolute divs with rounded-full or rounded-[...] and blur-...
            content = re.sub(r'<div class="absolute[^">]*rounded-(?:full|\[[^\]]+\])[^">]*blur-[^">]*"></div>', 
                             '', 
                             content)
            
            # Additional specific cleanups for index.html nextgen blurs
            content = re.sub(r'<!-- Subtle Background Decoration -->\s*', '', content)
            
            # 3. Fix broken footer tags and garbage at the end
            # This looks for the common pattern of extra divs and 'er>' garbage
            content = re.sub(r'</div>\s*</div>\s*er>.*?All images are for demo purposes only\.</p>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
            
            # Ensure footer-bottom-dark is properly closed with TWO divs
            # This is tricky because it varies. I'll just check if there's exactly two </div> after the designed by link.
            # Actually, I'll just do a targeted fix for the bottom bar structure.
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

if __name__ == "__main__":
    fix_html_files(r"C:\Users\dines\OneDrive\Desktop\client\Sivam itech")
