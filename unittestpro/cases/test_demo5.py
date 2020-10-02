from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest

class TestCaseShop(unittest.TestCase):

    def is_element_exist(self,driver,locator):        
        try:
            WebDriverWait(driver,30).until(lambda s:s.find_element(*locator))
            return True
        except:
            return False

    def find_element(self,driver,locator):
        return WebDriverWait(driver,30).until(lambda s:s.find_element(*locator))

    def test_01_shop(self):

        driver = webdriver.Chrome(executable_path="C:\\Users\\林颖慧\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
        driver.get("http://132.232.44.158:8080/login")

        username = ('id','username')
        password = ('id','password')
        btnlogin = ('id','btnLogin')
        self.find_element(driver,username).send_keys("1")
        self.find_element(driver,password).send_keys("2")
        self.find_element(driver,btnlogin).click()

        locator = ('id','usernameTips')
        self.assertTrue(self.is_element_exist(driver,locator),"未找到元素")
    
        driver.quit()

if __name__=="__main__":
    unittest.main()