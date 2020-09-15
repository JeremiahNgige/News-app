import os
class Config:
    '''
    general configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?apiKey={}'
    NEWS_API_BASE_ARTICLE = 'https://newsapi.org/v2/{}?language=en&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
class ProdConfig(Config):
    '''
    production configuration subclass
    Args:
        Config: The general configuration class with the the general configuration settings
    '''
    pass
class DevConfig(Config):
    '''
    development configuration subclass
    Args:
        Config: The general configuration class with the the general configuration settings
    '''
    DEBUG = True
    
config_options = {
    'development':DevConfig,
    'production': ProdConfig
}
    