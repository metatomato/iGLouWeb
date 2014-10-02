from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from .ft_base import FunctionalTest
import time

class NavigationTest(FunctionalTest):

    def test_navigation(self):
        self.browser.get('http://tomato-studio.ddns.net')
        time.sleep(5)
        self.fail('go, go, cactus man!')

#test from python/console
#if __name__ == '__main__': 
#    unittest.main(warnings='ignore')
