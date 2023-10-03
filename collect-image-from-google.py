
pip install requests beautifulsoup4 urllib3

query = "your search query"
num_images = 100  # The number of images you want to collect
url = f"https://www.google.com/search?q={query}&tbm=isch&num={num_images}"


import requests

response = requests.get(url)

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser")

# Find image URLs in the HTML
image_tags = soup.find_all("img")


import urllib3

for i, img_tag in enumerate(image_tags):
    img_url = img_tag.get("src")
    if img_url:
        img_name = f"{query}_{i}.jpg"
        urllib3.PoolManager().request('GET', img_url, preload_content=False)
        with open(img_name, 'wb') as out:
            while True:
                data = response.read(1024)
                if not data:
                    break
                out.write(data)
