'''
百度首页的pageobject

'''

from utils.selenuimtools import find_element

class Baiduindex():

    def __init__(self,driver):
        self.driver=driver
        self.search_input=('id','kw')
        self.seaech_btn=('id','su')

    def open_baiduindex(self):
        self.driver.get("https://www.baidu.com")

    def search(self):
        find_element(self.driver,self.search_input).send_keys("po")
        find_element(self.driver,self.seaech_btn).click()