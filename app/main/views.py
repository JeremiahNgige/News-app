from flask import render_template
from . import main
from ..requests import get_sources, get_latest_articles

@main.route('/')
def index():
    '''
    view root page that returns the home page with the sources
    '''
    #getting the various lited sources
    sources = get_sources('sources')
    title = 'News sources'
    print(sources)
    
    return render_template('index.html', sources=sources)

@main.route('/article')
def article():
    '''
    view root function to display the top headlines
    '''
    articles = get_latest_articles('top-headlines')
    print(articles)
    
    return render_template('news_article.html',articles=articles)
    