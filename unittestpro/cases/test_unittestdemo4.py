import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
@unittest.skip("pass")
class TestCaseLifeCycle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="E:\\seleniumstdy\\chromedriver.exe")
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        print("setup")
    def tearDown(self):
        print("teardown")
    
    def test_01_shop2(self):
        '''
        这是第一个测试用例。。。
        '''
        self.driver.get("http://132.232.44.158:8080/")

        baicaitai=('xpath','//*[@id="J_wrap_pro_add"]/li[3]/div[1]/a/img')
        ee=WebDriverWait(self.driver,10).until(lambda s : s.find_element(*baicaitai))
        ee.click()
        jiagou=('id','J_mer_saleTag')
        e1=WebDriverWait(self.driver,10).until(lambda s : s.find_element(*jiagou))
        e1.click()
        bag=('link text',"购物袋")
        e2=WebDriverWait(self.driver,10).until(lambda s : s.find_element(*bag))
        e2.click()
        baicaitai1=('xpath','//*[@id="cart_item_3"]/td[1]/a/img')
               
        self.assertTrue(self.is_element_exist(self.driver,baicaitai1))
    
    def test_02_shop1(self):
        '''
        这是第二个测试用例。。。

        '''
        self.driver.get("http://132.232.44.158:8080/")
        
        jielan = ('xpath','//*[@id="J_wrap_pro_add"]/li[2]/div[1]/a/img')
        self.find_element(self.driver,jielan).click()                                             #通过xpath找到商品并点击该商品（芥兰）
        btncart = ('xpath','//*[@id="J_mer_saleTag"]')
        self.find_element(self.driver,btncart).click()                                            #通过xpath找到加入购物袋按钮并点击该按钮
        bag = ('xpath','//*[@id="J_header_cart"]/div[1]/a[1]')
        self.find_element(self.driver,bag).click()                                                #通过xpath找到购物袋并点击购物袋
        jielan_cart = ('link text',"mudan")                                                         #通过link_text查找商品芥兰
                                                   
        self.assertTrue(self.is_element_exist(self.driver,jielan_cart),"{}没有加入购物车".format(jielan_cart[1]))

    def find_element(self,driver,locator):
        return WebDriverWait(driver,30).until(lambda s:s.find_element(*locator))

    def is_element_exist(self,driver,locator):       
        try:
            WebDriverWait(driver,30).until(lambda s:s.find_element(*locator))
            return True
        except:
            return False

if __name__=="__main__":
    unittest.main()