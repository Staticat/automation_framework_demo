# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage

class BaiduSearch(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_baidu_search(self):
        homepage = HomePage(self.driver)
        homepage.type_search('selenium')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_window_img()
        try:
            assert 'selenium' in homepage.get_page_title()
            print('Test Pass')
        except Exception as e:
            print('Test Fail',format(e))

if __name__ == '__main__':
    unittest.main()

