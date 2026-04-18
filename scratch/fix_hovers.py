import os
import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix "Visit Website" buttons: subtle bg, orange text
    # Finding strings like hover:bg-brand-orange hover:text-white and replacing with subtle versions
    new_content = content.replace('hover:bg-brand-orange hover:text-white', 'hover:bg-orange-50 hover:text-brand-orange border border-transparent hover:border-orange-100')
    
    # 2. Fix "Apply Now" buttons (specifically in careers.html)
    # They have two spaces typically: hover:bg-brand-orange  transition-colors
    new_content = new_content.replace('hover:bg-brand-orange  transition-colors', 'hover:bg-[#c2410c] hover:text-white transition-colors')
    
    # 3. Fix Newsletter / Footer orange buttons: darker orange for white text
    new_content = new_content.replace('hover:brightness-110', 'hover:bg-[#c2410c]')

    # 4. Fix Product Nodes in products.html
    # group-hover:bg-brand-orange -> group-hover:bg-orange-50
    # group-hover:text-white -> group-hover:text-brand-orange (specifically for the lucide icons)
    # We need to be careful with group-hover:text-white in general though.
    # For now, let's target the products.html specific blocks if we can.
    
    if 'products.html' in filepath:
        # Replace occurrences in node containers
        new_content = new_content.replace('group-hover:border-brand-orange group-hover:bg-brand-orange transition-all duration-300', 'group-hover:border-brand-orange group-hover:bg-orange-50 transition-all duration-300')
        new_content = new_content.replace('text-gray-400 group-hover:text-white transition-colors duration-300', 'text-gray-400 group-hover:text-brand-orange transition-colors duration-300')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in files:
    print(f"Fixing {f}...")
    fix_file(f)
print("Finished fixing hovers.")
