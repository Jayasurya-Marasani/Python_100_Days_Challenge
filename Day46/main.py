import requests
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url = URL)
songs_web_page = response.text
soup = BeautifulSoup(songs_web_page, "html.parser")
h3_tags = soup.select(selector= "li ul li h3")
songs_names = [tag.getText().strip() for tag in h3_tags]
