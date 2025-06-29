import requests
from bs4 import BeautifulSoup

def get_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    paragraphs = soup.find_all("p")
    text = " ".join([p.get_text() for p in paragraphs])
    return text.strip()
