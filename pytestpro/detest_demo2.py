import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_01_baidusearch():

    driver = webdriver.Chrome(executable_path="E:\\seleniumstdy\\chromedriver.exe")
    driver.get("https:\\www.baidu.com")
    driver.maximize_window()

    def find_element(driver,locator):
        return WebDriverWait(driver,30).until(lambda s:s.find_element(*locator))
    
    search=('id','kw')
    button=('id','su')
    find_element(driver,search).send_keys("pytest")
    find_element(driver,button).send_keys(Keys.ENTER)

    sleep(3)
    assert driver.title=="pytest_百度搜索"

    driver.quit()

def test_02_morning_sx():

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
