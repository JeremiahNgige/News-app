from flask import render_template,request,redirect, url_for
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

@main.route('/articles')
def articles():
    '''
    view root function to display the top headlines
    '''
    articles = get_latest_articles('top-headlines')
    print(articles)
    
    return render_template('new_article.html',articles=articles)
    