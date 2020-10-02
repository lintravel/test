# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from utils import selenuimtools as st



class TestCaseShop(unittest.TestCase):
    def test_01(self):

        driver = webdriver.Edge(executable_path="D:\\codes\\drivers\\msedgedriver.exe")
        driver.get("http://www.baidu.com")
        locator = ('id', 'su')
        

if __name__ == "__main__":
    unittest.main()
