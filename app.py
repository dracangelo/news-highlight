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
    pubAt=[]
    url= []
    
    for i in range (len(articles)):
        myarticles = articles [i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        pubAt.append(myarticles['publishedAt'])
        url.append(myarticles['url'])


    myList = zip(news, desc, img)


    return render_template ('index.html', context = myList)


@app.route('/abc')
def Abc():
    """
 A view root page function that returns the index page and its data
    """
    newsapi = NewsApiClient(api_key="c43cae8199d1435fa1e4cc0737cd4a88")
    topheadlines = newsapi.get_top_headlines(sources="abc-news-au")
    
    articles = topheadlines['articles']
     
    des=[]
    image=[]
    news=[]
    pubAt=[]
    url= []
    
    for i in range(len(articles)):
        myarticles = articles[i]
        
        news.append(myarticles['title'])
        image.append(myarticles['urlToImage'])
        des.append(myarticles['description'])
        pubAt.append(myarticles['publishedAt'])
        url.append(myarticles['url'])
        
    mylist=zip(des,image,news,pubAt,url)
    return render_template('abc.html', context = mylist)

@app.route('/Bbc')
def Bbc():
    
    
    """
 A view root page function that returns the index page and its data
    """
    newsapi = NewsApiClient(api_key="c43cae8199d1435fa1e4cc0737cd4a88")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")
    
    articles = topheadlines['articles']
     
    des=[]
    image=[]
    news=[]
    pubAt=[]
    url= []
    
  
    
    for i in range(len(articles)):
        myarticles = articles[i]
        
        news.append(myarticles['title'])
        image.append(myarticles['urlToImage'])
        des.append(myarticles['description'])
        pubAt.append(myarticles['publishedAt'])
        url.append(myarticles['url'])
 
        
    mylist=zip(des,image,news,pubAt,url)
    return render_template('Bbc.html', context = mylist)
@app.route('/Cnn')
def Cnn():
    
    
    """
 A view root page function that returns the index page and its data
    """
    newsapi = NewsApiClient(api_key="c43cae8199d1435fa1e4cc0737cd4a88")
    topheadlines = newsapi.get_top_headlines(sources="abc-news-au")
    
    articles = topheadlines['articles']
     
    des=[]
    image=[]
    news=[]
    pubAt=[]
    url= []
    
  
    
    for i in range(len(articles)):
        myarticles = articles[i]
        
        news.append(myarticles['title'])
        image.append(myarticles['urlToImage'])
        des.append(myarticles['description'])
        pubAt.append(myarticles['publishedAt'])
        url.append(myarticles['url'])
 
        
    mylist=zip(des,image,news,pubAt,url)
    return render_template('Cnn.html', context = mylist)
@app.route('/Aljazeera')
def Aljzeera():
    
    
    """
 A view root page function that returns the index page and its data
    """
    newsapi = NewsApiClient(api_key="c43cae8199d1435fa1e4cc0737cd4a88")
    topheadlines = newsapi.get_top_headlines(sources="abc-news-au")
    
    articles = topheadlines['articles']
     
    des=[]
    image=[]
    news=[]
    pubAt=[]
    url= []
    
  
    
    for i in range(len(articles)):
        myarticles = articles[i]
        
        news.append(myarticles['title'])
        image.append(myarticles['urlToImage'])
        des.append(myarticles['description'])
        pubAt.append(myarticles['publishedAt'])
        url.append(myarticles['url'])
 
        
    mylist=zip(des,image,news,pubAt,url)
    return render_template('Aljzeera.html', context = mylist)
   




if __name__ == "__main__":
    app.run(debug=True)
