import os
import re

def fix_html_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 1. Fix header logo classes
            content = re.sub(r'class="h-20 md:h-28 lg:h-32 w-auto object-contain transition-transform duration-500 group-hover:scale-105"', 
                             r'class="w-auto object-contain transition-transform duration-500 group-hover:scale-105"', 
                             content)
            
            # 2. Remove decorative divs in nextgen (oval shapes)
            content = re.sub(r'<!-- Subtle Background Decoration -->\s*<div class="absolute top-0 right-0 -mr-20 -mt-20 w-96 h-96 bg-brand-orange/5 rounded-full blur-3xl"></div>\s*<div class="absolute bottom-0 left-0 -ml-20 -mb-20 w-96 h-96 bg-gray-200 rounded-full blur-3xl opacity-50">\s*</div>', 
                             '', 
                             content)
            
            # 3. Fix broken footer tags (garbage at the end)
            # This pattern matches the specific garbage block found in the files.
            garbage_pattern = re.compile(r'</div>\s*</div>\s*er>.*?All images are for demo purposes only\.</p>\s*</div>\s*</div>', re.DOTALL)
            content = garbage_pattern.sub('', content)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

if __name__ == "__main__":
    fix_html_files(r"C:\Users\dines\OneDrive\Desktop\client\Sivam itech")
