from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
class Driver:
    def __init__(self,driver):
        self._driver = driver
    def locate_element(self, locator: tuple[[], str], driver: [] = None, wait: int = 5, mark=False) -> WebElement:
        if driver is None:
            driver = self._driver
        element = WebDriverWait(driver, wait).until(EC.presence_of_element_located((locator)))
        if mark:
            self._driver.execute_script("arguments[0].style.border='2px solid red'", element)
        return element

    def locate_elements(self, locator: tuple[[], str], wait: int = 5) -> [WebElement]:
        elements = WebDriverWait(self._driver, wait).until(EC.presence_of_all_elements_located(locator))
        return elements

    def locate_and_switch_to_frame(self, locator: tuple[[], str], wait: int = 5):
        WebDriverWait(self._driver, wait).until(EC.frame_to_be_available_and_switch_to_it(locator))