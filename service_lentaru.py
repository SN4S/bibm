import requests 
from bs4 import BeautifulSoup
from pprint import pprint
from schemas import NewsBase


def parse_lentaru_source() -> list[NewsBase]:
    list_of_news: list[NewsBase] = []

    LENTA_NEWS_URL: str = 'https://lenta.ru/parts/news/'
    LENTA_NEWS_DOMEN: str = 'https://lenta.ru'

    proxy = {
        'http': "tom%40gmail.com:password123@au473.nordvpn.com",
        'https': "tom%40gmail.com:password123@au473.nordvpn.com"
    }



    page = requests.get(LENTA_NEWS_URL)


    soup = BeautifulSoup(page.content, "html.parser")

    a_tags = soup.find('ul', class_='parts-page__body _parts-news').find_all('a', href=True)

    links_to_news: list[str] = [LENTA_NEWS_DOMEN + item['href'] for item in a_tags]


    # pprint(links_to_news)

    for counter, link in enumerate(links_to_news): 
        try:
            _page = requests.get(link)
            _soup = BeautifulSoup(_page.content, 'html.parser') #class="topic-body__content"

            title = _soup.find(class_='topic-body__title').text.replace("\xa0", '')
            date = _soup.find(class_='topic-header__time topic-header__item').text.replace("\xa0", '')
            body = _soup.find(class_='topic-body__content').text.replace("\xa0", '')

            data = NewsBase(source=link, title=title, date=date,content=body)
            list_of_news.append(data)

        except Exception:
            continue
    return list_of_news

parse_lentaru_source()
