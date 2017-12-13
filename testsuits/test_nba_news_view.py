# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage
from pageobjects.baidu_news_home import NewsHomePage
from pageobjects.news_sports_home import SportNewsHomePage

class ViewNBANews(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_view_nba_views(self):
        #初始化百度首页，并点开新闻链接
        baiduhome = HomePage(self.driver)
        self.driver.find_element_by_xpath("//*[@id='u1']/a[1]").click()
        #初始化百度新闻主页对象，点击体育
        newhome = NewsHomePage(self.driver)
        self.driver.find_element_by_xpath("//*[@id='channel-all']/div/ul/li[9]/a").click()
        #初始化一个体育新闻主页，点击NBA
        sportnewhome = SportNewsHomePage(self.driver)
        self.driver.find_element_by_xpath("//*[@id='channel-submenu']/div/span[2]/a[1]").click()
        sportnewhome.get_window_img()

if __name__== '__main__':
    unittest.main()