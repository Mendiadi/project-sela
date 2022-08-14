from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, driver: Chrome):
        self.driver = driver

    def locate_element(self,locator,driver=None,wait:int=3) -> WebElement:
        if driver is None:
            driver = self.driver
        element = WebDriverWait(driver,wait).until(EC.presence_of_element_located((locator)))
        return element

    def locate_elements(self,locator,wait:int=3) -> [WebElement]:
        elements = WebDriverWait(self.driver,wait).until(EC.presence_of_all_elements_located(locator))
        return elements
    def get_message(self):
        pass