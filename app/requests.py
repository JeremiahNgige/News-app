import urllib.request,json
from .news_src import Sources
from .news_top_articles import latestTopArticles

#Getting api key
api_key = None
#Getting the source base URL
base_url = None
#getting the articles list
article_url = None 

def configure_request(app):
    global api_key, base_url, article_url
    
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['NEWS_API_BASE_ARTICLE']
    
def get_sources(source):
    '''
    function to get the url response for the sources
    '''
    get_sources_url = base_url.format(source,api_key)
    
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        
        news_results = None
        if get_sources_response['sources']:
            news_results_list = get_sources_response['sources']
            news_results = process_results(news_results_list)
            
    return news_results

def get_latest_articles(everything):
    '''
    function to get url response for the latest articles
    '''
    get_articles_url = article_url.format(everything,api_key)
    
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        
        articles_results = None
        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_results_list)
            
    return articles_results
            
    
def process_results(news_list):
    '''
    function that processes the list of news details to news objects
    Args:
        news_list: Alist of dictionaries that contain news source details
    returns: 
        news_results: A list of news objects
    '''
        
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')
            
        if name:
            news_object = Sources(id,name,description,url,category,language,country)
            news_results.append(news_object)
        
    return news_results
    
def process_articles_results(articles_list):
    '''
    function that processes the list of article details to artcle objects
    Args:
        articles_list: Alist of dictionaries that contain articles details
    returns: 
        article_results: A list of article objects
    '''
        
    articles_results = []
    for article_item in articles_list:
        author = article_item.get('author')
        description = article_item.get("description")
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
            
            
        if urlToImage and author:
            articles_object = latestTopArticles(author, description, url, urlToImage, publishedAt)
            articles_results.append(articles_object)
        
    return articles_results