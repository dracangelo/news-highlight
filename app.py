from flask import Flask, render_template
from newsapi import NewsApiClient




app = Flask(__name__)


@app.route('/')

def index():
    newsapi = NewsApiClient(api_key = 'c43cae8199d1435fa1e4cc0737cd4a88')
    topheadlines = newsapi.get_top_headlines(sources = "al-jazeera-english")


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []


    for i in range (len(articles)):
        myarticles = articles [i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])


    myList = zip(news, desc, img)


    return render_template ('index.html', context = myList)




if __name__ == "__main__":
    app.run(debug=True)
