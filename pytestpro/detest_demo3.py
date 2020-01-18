import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import requests

class TestCasesDemo1():

    def test_01_morning_login(self):

        driver=webdriver.Chrome(executable_path="E:\\seleniumstdy\\chromedriver.exe")
        driver.get("http://132.232.44.158:8080/login")
        driver.maximize_window()

        def find_element(driver,locator):
            return WebDriverWait(driver,30).until(lambda s:s.find_element(*locator))

        username=('id','username')
        password=('id','password')
        btnlogin=('id','btnLogin')
        find_element(driver,username).send_keys("18361208507")
        find_element(driver,password).send_keys("123456")
        find_element(driver,btnlogin).click()

        assert driver.title=="首页"

        driver.quit()
    
    def test_02_requets(self):
      
        #requests的测试方法
        
        
        #1、构造请求
        response=requests.get("http://132.232.44.158:8080/login")
        #2、http相应状态断言
        assert requests.status_codes == 200
        #3、接口的返回值断言
        assert response.json().get("code")==200
        #4、查询数据库
        pass
    