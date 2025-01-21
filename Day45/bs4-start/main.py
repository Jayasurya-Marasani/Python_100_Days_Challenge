from bs4 import BeautifulSoup
import requests

response = requests.get(url = "https://news.ycombinator.com/news")
# response.raise_for_status()
# print(response.status_code)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

span_tags = soup.find_all(name = "span", class_ = "titleline")
article_text = [span.find('a').getText() for span in span_tags]
article_links = [span.find('a').get("href") for span in span_tags]

span_upvotes_tags = soup.find_all(name = "span", class_ = "score")
article_upvotes = [int(span.getText().split(" ")[0]) for span in span_upvotes_tags]

max_upvotes_index = article_upvotes.index(max(article_upvotes))
print(article_text[max_upvotes_index])
print(article_links[max_upvotes_index])
print(article_upvotes[max_upvotes_index])



