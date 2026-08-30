import os

html_file = r"c:\Users\AJAY\Downloads\solar-navbar-hero-clean\index.html"

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    "#7f9598": "#64748b",
    "#50676b": "#475569",
    "#233d42": "#1e293b",
    "#536a6d": "#334155",
    "#8da0a2": "#94a3b8",
    "#173238": "#0f172a",
    "#19343a": "#1e293b",
    "#627a7d": "#475569",
    "#0e3037": "#1e293b"
}

for old, new in replacements.items():
    content = content.replace(old, new)
    content = content.replace(old.upper(), new)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Remaining green variants updated successfully.")
