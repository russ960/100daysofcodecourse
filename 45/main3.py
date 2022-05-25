from gettext import find
from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/news"

site_request = requests.get(url)
site_code = site_request.text

soup = BeautifulSoup(site_code, "html.parser")

articles = soup.find_all(name='a', class_="titlelink")

article_text = []
article_links = []

for article in articles:
    article_text.append(article.getText())
    link = article.get('href')
    article_links.append(link)

article_upvotes = [int((score.getText()).split(' ')[0]) for score in soup.find_all(name='span', class_="score")]

max_points = max(article_upvotes)
max_index = article_upvotes.index(max_points)

print(max_index)
print(article_text[max_index])
print(article_links[max_index])
print(article_upvotes[max_index])
