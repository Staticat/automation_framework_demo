# makeSuite()方法
# coding=utf-8
import unittest
import testsuits
from testsuits.baidu_search2 import BaiduSearch
from testsuits.test_get_page_title import GetPageTitle

suite = unittest.TestSuite(unittest.makeSuite(BaiduSearch))
# suite(unittest.makeSuite(GetPageTitle))

if __name__=='__main__':
    #执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)
