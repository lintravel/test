from utils import selenium_tools as tools

if __name__=="__main__":

    dr=tools.PySelenium(url="http://132.232.44.158:8080/morning/")
    
    input_text=('id','searchInput')
    button=('xpath','//*[@id="zySearch"]/button')
    locator=('xpath','//*[@id="products-list"]/ul/li/div[1]/a/img')
    cart=('xpath','//*[@id="form"]/div[2]/label/a')
    check=('xpath','//*[@id="buy"]/a')
    goods_cart=('xpath','//*[@id="cartTable"]/tbody/tr/td[2]/span')
    dr.input(dr.driver,input_text,"苹果6s")
    dr.click_element(dr.driver,button)
    dr.click_element(dr.driver,locator)
    dr.driver.switch_to.window(dr.driver.window_handles[-1])
    dr.click_element(dr.driver,cart)
    dr.click_element(dr.driver,check)
    try:
        dr.exist_elemwent(dr.driver,goods_cart)
        print("加入购物车成功！")
    except:
        print("加入购物车失败！")

    dr.quit_browser()