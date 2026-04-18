import os

def update_logo(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Target the navbar logo specifically
    # Current: class="h-16 md:h-20 lg:h-24 w-auto object-contain transition-transform duration-500 group-hover:scale-105"
    # New: h-16 md:h-24 lg:h-28
    new_content = content.replace('h-16 md:h-20 lg:h-24 w-auto', 'h-16 md:h-24 lg:h-28 w-auto')
    
    # Also ensure footer logo is large and clear
    # Current: class="h-20 md:h-28 w-auto object-contain"
    # Let's keep it at h-28 for footer, it's already good.
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in files:
    update_logo(f)
print("Finished updating logo sizes.")
