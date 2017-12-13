#用discover()方法
# coding = utf-8
import HTMLTestRunner
import unittest
import os
import time
from testsuits.baidu_search2 import BaiduSearch

#设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.'))+'/test_report/'
#获取系统当前时间
now = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))

#设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile,'wb')

#构建suite
# suite = unittest.TestLoader().discover("testsuits")
suite = unittest.TestSuite(unittest.makeSuite(BaiduSearch))

if __name__=='__main__':
    #初始化一个HTMLtestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="XX项目测试报告",description="用例情况")
    runner.run(suite)