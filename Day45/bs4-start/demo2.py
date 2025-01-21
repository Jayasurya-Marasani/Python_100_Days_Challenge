

from bs4 import BeautifulSoup
from requests import head
# import lxml

with open("website.html", "r") as file:
    contents =file.read()
    # print(contents)


soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# # print(soup.prettify())
# print(soup.a)
# print(soup.a.name)
# print(soup.a.string)

all_anchor_tags = soup.find_all(name = "a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag.string)
    # print(tag.getText())
    # print(tag.get("href"))
    pass


heading = soup.find(name="h1", id = "name")
print(heading)

h3_heading = soup.find(name="h3", class_ = "heading")
print(h3_heading.getText())
print(h3_heading.get("class"))

company_url = soup.select_one(selector="p a")
print(company_url.get("href"))

heading_name = soup.select_one(selector="#name")
print(heading_name)

headings = soup.select(".heading")
print(headings)