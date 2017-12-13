# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage

class BaiduSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是提前准备工作
        :return:
        """
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上就是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_baidu_search(self):
        """
        这里一定要test开头，把测试的逻辑代码封装到一个test开头的方法里
        :return:
        """
        homepage = HomePage(self.driver)
        homepage.type_search("selenium") # 调用页面对象中的方法
        homepage.send_submit_btn() # 调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        homepage.get_window_img() #调用基类截图方法
        try:
            assert 'selenium' in homepage.get_page_title()
            print("Test pass!")
        except Exception as e:
            print("Test Fail".format(e))

    def test_search2(self):
        homepage = HomePage(self.driver)
        homepage.type_search("python")
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_window_img()

if __name__ == '__main__':
    unittest.main()
