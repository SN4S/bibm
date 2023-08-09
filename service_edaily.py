import requests 
from bs4 import BeautifulSoup
from datetime import date as d
from pprint import pprint
import re 
from schemas import NewsBase


def parse_edaily_source() -> list[NewsBase]:
    """Parse todays news from https://eadaily.com/ru ."""

    list_of_news: list[NewsBase] = []

    day = str(d.today().day)
    month = str(d.today().month)
    year = str(d.today().year)


    EDAILY_NEWS_URL: str = f'https://eadaily.com/ru/news/ukraine/{year}/{month}/{day}/'
    EDAILY_NEWS_DOMEN: str = 'https://eadaily.com'

    mian_page = requests.get(EDAILY_NEWS_URL)


    soup_main = BeautifulSoup(mian_page.content, "html.parser")

    a_tags = soup_main.find('ul', class_='news-feed').find_all('a', href=True)

    links_to_news: list[str] = [EDAILY_NEWS_DOMEN + item['href'] for item in a_tags]

    for counter, link in enumerate(links_to_news):
        _page = requests.get(link)
        _soup = soup_main = BeautifulSoup(_page.content, "html.parser")

        title = _soup.find('article').find('p').text.replace("\xa0", '')
        date = _soup.find('div', class_='datetime').find('time')['datetime']

        image = None
        try:
            image = _soup.find('figure', class_='oneimage').find('img')['src']
            image = 'https:'+image
        except Exception:
            pass

        body = _soup.find('div', class_='news-text-body')
        cleaned_body = re.sub(r"<.*?>", "", str(body)).replace("\xa0", '').replace('\n', '')    

        data = NewsBase(source=link, title=title, date=date,content=cleaned_body, image=image)
        list_of_news.append(data)

    return list_of_news



