from selenium.webdriver.support.ui import WebDriverWait

def find_element(driver,locator,timeout=20):
    return WebDriverWait(driver,timeout).until(lambda s:s.find_element(*locator))