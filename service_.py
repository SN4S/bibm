
import requests
from bs4 import BeautifulSoup
from schemas import NewsBase




def parse_obozrevatel_source() -> list[NewsBase]:
    """"""
    list_of_news: list[NewsBase] =[]