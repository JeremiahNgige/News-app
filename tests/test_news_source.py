import unittest
from app.news_src import Source

class TestSource(unittest.TestCase):
    '''
    test behaviour of the latestTopSArticles class
    '''
    def setUp(self):
        '''
        setUp method that will run before every test
        '''
        self.new_source = Source('abc-news',
                                                         'ABC News', 
                                                         'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.',
                                                         'https://abcnews.go.com', 
                                                         'general',
                                                         'en',
                                                         'us' 
                                                          )
    def test_instance(self):
        
        self.assertTrue(isinstance(self.new_source,Source))
        
if __name__ == '__main__':
    unittest.main()