# addTest()方法

# coding=utf-8
import unittest
import testsuits
from testsuits.baidu_search2 import BaiduSearch
from testsuits.test_get_page_title import GetPageTitle

suite = unittest.TestSuite()
suite.addTest(BaiduSearch('test_baidu_search'))
suite.addTest(BaiduSearch('test_search2'))
suite.addTest(GetPageTitle('test_get_title'))

if __name__=='__main__':
    #执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)


