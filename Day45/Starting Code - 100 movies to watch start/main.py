import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url = URL)
movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, "html.parser")

h3_tags = soup.find_all(name = "h3", class_ = "title")
print(h3_tags)
h3_tags_movies = [tag.getText() for tag in h3_tags]
h3_tags_movies = h3_tags_movies[::-1]
print(h3_tags_movies)

with open("movies.txt", "a", encoding="utf-8") as file:
    for movie in h3_tags_movies:
        file.write(movie + "\n")
