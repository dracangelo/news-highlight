from flask import Flask
from newsapi import NewsApiClient




app = Flask(__name__)


@app.route('/')

def index():
    newsapi = NewsApiClient(api_key = 'b1e9516dfbd64a7fba60978b8591d03e')
    topheadlines = newsapi.get_top_headlines(sources = "abc-news")


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    