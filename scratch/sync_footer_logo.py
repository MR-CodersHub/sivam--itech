import os
import re

# We will target the logo inside the footer specifically
def update_footer_logo(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the footer section first to avoid touching the header logo
    footer_match = re.search(r'<footer.*?>(.*?)</footer>', content, re.DOTALL)
    if not footer_match:
        return

    footer_content = footer_match.group(1)
    
    # Target the logo image in the footer
    # h-20 md:h-28 -> h-24 md:h-32 lg:h-36
    new_footer_content = re.sub(
        r'class="h-20 md:h-28 w-auto object-contain"',
        'class="h-24 md:h-32 lg:h-36 w-auto object-contain"',
        footer_content
    )
    
    if new_footer_content != footer_content:
        new_full_content = content.replace(footer_content, new_footer_content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_full_content)
        print(f"Updated Footer Logo in {os.path.basename(file_path)}")

if __name__ == "__main__":
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for file in html_files:
        update_footer_logo(file)
