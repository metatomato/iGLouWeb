from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from .ft_base import FunctionalTest
import time

class NavigationTest(FunctionalTest):
    
    def get_scroll_offset(self):
        scroll_position_script = """
            var pageY;
            if (typeof(window.pageYOffset) == 'number') {
                pageY = window.pageYOffset;
            } else {
                pageY = document.documentElement.scrollTop;
            }
            return pageY;
        """
        return self.browser.execute_script(scroll_position_script)


    def test_label(self):
        #Bob to iGLou site
        self.browser.get(self.live_server_url)   
        #Bob notices the page title  
        self.assertEqual('iGLou Studio', self.browser.title) 
        #Bob found out he was on the home page 
        

    def test_navigation(self):
        #Bob to iGLou site
        self.browser.get(self.live_server_url)
        #Bob scroll down and see that the nav bar still sticks the top page
        nav_bar = self.browser.find_element_by_class_name('navbar')
        nav_bar_pos = nav_bar.location['y']
        self.browser.execute_script('window.scrollBy(0,800)','')
        self.assertEqual(nav_bar.location['y'] - self.get_scroll_offset(), nav_bar_pos)
        
        #self.fail('go, go, cactus man!')

#test from python/console
#if __name__ == '__main__': 
#    unittest.main(warnings='ignore')
