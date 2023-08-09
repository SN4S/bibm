from fastapi import FastAPI
from service_edaily import parse_edaily_source
from service_lentaru import parse_lentaru_source

app = FastAPI()

@app.get('')
async def index():
    return {'message': 'hueta pashe'}

@app.get('/edaily-news')
async def get_edaily_news():
    return parse_edaily_source()


@app.get('/lentaru-news/')
async def get_lentaru_news():
    return parse_lentaru_source()

