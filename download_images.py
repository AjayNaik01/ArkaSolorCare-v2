import re
import urllib.request
import os
import uuid

html_file = r"c:\Users\AJAY\Downloads\solar-navbar-hero-clean\index.html"
assets_dir = r"c:\Users\AJAY\Downloads\solar-navbar-hero-clean\assets\images"

os.makedirs(assets_dir, exist_ok=True)

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all unsplash urls
urls = set(re.findall(r'https://images\.unsplash\.com/[^"\']+', content))

url_map = {}
for i, url in enumerate(urls):
    # generate a nice name based on photo id or just a number
    img_name = f"image_{i+1}.jpg"
    img_path = os.path.join(assets_dir, img_name)
    print(f"Downloading {url} to {img_path}")
    try:
        # Add a user agent to avoid 403 Forbidden
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(img_path, 'wb') as out_file:
            out_file.write(response.read())
        url_map[url] = f"assets/images/{img_name}"
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# Replace in content
for url, local_path in url_map.items():
    content = content.replace(url, local_path)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done replacing and downloading.")
