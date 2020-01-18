import unittest
from selenium import webdriver
from po.baiduindex import Baiduindex
@unittest.skip("PASS")
class TestCaseBaiduindex(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="E:\\seleniumstdy\\chromedriver.exe")
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
        import time
        time.sleep(5)
        cls.driver.quit()

    def test_01_baiduindex(self):
        baidu=Baiduindex(self.driver)
        baidu.open_baiduindex()
        baidu.search()
        
        