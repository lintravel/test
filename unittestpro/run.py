


import unittest
from utils.HTMLTestRunner import HTMLTestRunner

testcases = unittest.defaultTestLoader.discover("cases","test_*.py")

testsuits = unittest.TestSuite()
testsuits.addTests(testcases)

title="测试报告"
descr="猫宁生鲜"
file_path="./report/morning_report.html"

with open(file_path,'wb') as f:
    runner=HTMLTestRunner(stream=f,title=title,description=descr)
    runner.run(testsuits)