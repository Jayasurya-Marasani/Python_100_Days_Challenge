
from bs4 import BeautifulSoup
# import lxml

with open("website.html", "r") as file:
    contents =file.read()
    # print(contents)


soup = BeautifulSoup(contents, "html.parser")

print(soup.title)
print(soup.title.name)
print(soup.title.string)

# print(soup.prettify())
print(soup.a)
print(soup.a.name)
print(soup.a.string)
