from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, driver: Chrome):
        self.driver = driver

    def locate_element(self,locator,wait:int=3) -> WebElement:
        element = WebDriverWait(self.driver,wait).until(EC.presence_of_element_located((locator)))
        return element

