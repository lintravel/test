from selenium import webdriver
import time

driver=webdriver.Edge(executable_path="D:\\codes\\drivers\\msedgedriver.exe")
driver.get("http://www.baidu.com")
time.sleep(3)
driver.close
#111