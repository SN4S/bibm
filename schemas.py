from pydantic import BaseModel


class NewsBase(BaseModel):
    source: str 
    title: str 
    date: str 
    content: str
    image: str = None