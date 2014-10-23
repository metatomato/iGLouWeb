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

    def set_scroll(self, y):
        self.browser.execute_script('window.scrollBy(0,arguments[0])', y)
        scroll_y = self.get_scroll_offset()
        assert y == scroll_y
        return scroll_y

    def test_label(self):
        # Bob to iGLou site
        self.browser.get(self.live_server_url)
        # Bob notices the page title
        self.assertEqual('iGLou Studio', self.browser.title)
        #Bob found out he was on the home page 

    def test_navigation_scrolling(self):
        # Bob go to iGLou site
        self.browser.get(self.live_server_url)
        # Bob scrolls down and see that the nav bar still sticks the top page
        nav_bar = self.browser.find_element_by_class_name('navbar')
        nav_bar_pos = nav_bar.location['y']
        scrolled_val = self.set_scroll(800)
        self.assertEqual(nav_bar.location['y'] - scrolled_val, nav_bar_pos)

    def test_navigation_link(self):
        # Bob go to iGLou site
        self.browser.get(self.live_server_url)
        # He clicks on the navigation button in navbar and page goes to the section
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/ul/li[4]/a').click()
        #and click the first entry in the dropdown menu
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/ul/li[4]/ul/li[1]/a').click()




        #self.fail('go, go, cactus man!')

# test from python/console
# if __name__ == '__main__':
#    unittest.main(warnings='ignore')





































