import unittest
from news_top_articles import latestTopArticles

class TestTopArticles(unittest.TestCase):
    '''
    test behaviour of the latestTopSArticles class
    '''
    def setUp(self):
        '''
        setUp method that will run before every test
        '''
        self.new_latest_top_articles = latestTopArticles('Rebecca Klar',
                                                         "Israel will reinstate strict lockdown measures for three weeks am...",
                                                         "https://thehill.com/policy/international/middle-east-north-africa/516214-israel-to-reinstate-strict-three-week",
                                                         "https://thehill.com/sites/default/files/netanyahu_1_0.jpg",
                                                         "2020-09-13T19:15:56Z"
                                                          )
    def test_instance(self):
        
        self.assertTrue(isinstance(self.new_latest_top_articles,latestTopArticles))
        
if __name__ == '__main__':
    unittest.main()