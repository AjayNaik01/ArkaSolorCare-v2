import os

html_file = r"c:\Users\AJAY\Downloads\solar-navbar-hero-clean\index.html"

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    "#09262c": "#0f172a",
    "#718789": "#475569",
    "#f4f6f4": "#f8fafc",
    "#c1c9c7": "#cbd5e1",
    "#c7d0cd": "#cbd5e1"
}

for old, new in replacements.items():
    content = content.replace(old, new)
    # Also replace uppercase in case
    content = content.replace(old.upper(), new)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Colors updated successfully.")
