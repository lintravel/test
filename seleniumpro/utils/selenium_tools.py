from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class PySelenium():
    def __init__(self,browser="chrome",url=None,path="E:\\seleniumstdy\\chromedriver.exe"):
        '''
        初始化并打开浏览器
        '''
        if browser=="chrome" or browser=="ch":
            self.driver=webdriver.Chrome(executable_path=path)
            self.driver.get(url)
        elif browser=="firefox" or browser=="ff":
            self.driver=webdriver.Firefox(executable_path=path)
            self.driver.get(url)
        elif browser=="internet explorer" or browser=="ie":
            self.driver=webdriver.Ie(executable_path=path)
            self.driver.get(url)
        elif browser=="edge":
            self.driver=webdriver.Edge(executable_path=path)
            self.driver.get(url)
    
    def find_element(self,driver,locator,timeout=10):
        '''
        查找元素
        '''
        try:
            e=WebDriverWait(driver,timeout).until(lambda s:s.find_element(*locator))
            return e
        except:
            return None

    def click_element(self,driver,locator):
        '''
        点击元素
        '''
        e=self.find_element(driver,locator)
        e.click()

    def input(self,driver,locator,content):
        '''
        输入内容
        '''
        e=self.find_element(driver,locator)
        e.send_keys(content)

    def exist_elemwent(self,driver,locator):
        '''
        '''
        try:
            self.find_element(driver,locator)
            return True
        except:
            return False


    def quit_browser(self):
        '''
        退出浏览器
        '''
        self.driver.quit()

# if __name__=="__main__":
#     dr=PySelenium(url="http://132.232.44.158:8080/morning/")
#     input_text=('id','searchInput')
#     button=('xpath','//*[@id="zySearch"]/button')
#     dr.input(dr.driver,input_text,"苹果6s")
#     dr.click_element(dr.driver,button)
#     dr.driver.quit()
    