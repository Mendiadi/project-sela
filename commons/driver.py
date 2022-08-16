from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver


class Driver:
    def __init__(self, driver: webdriver):
        self._driver = driver

    @staticmethod
    def send_keys(locator: WebElement, keys: str) -> None:
        """
        send keys to locator
        :param locator: input locator
        :param keys: some string
        """
        locator.send_keys(keys)

    def locate_element(self, locator: tuple[[], str], driver: [] = None, wait: int = 5, mark=False) -> WebElement:
        """
        Locating element with wait timeout and option to mark that element
        :param locator: tuple - (By,str) - locator
        :param driver: optional - some WebElement to search inside
        :param wait: timeout wait - int
        :param mark: bool - True to mark , False to not mark
        :return: the element that found
        :rtype: WebElement
        """
        if driver is None:
            driver = self._driver
        element = WebDriverWait(driver, wait).until(EC.presence_of_element_located(locator))
        if mark:
            self._driver.execute_script("arguments[0].style.border='2px solid red'", element)
        return element

    def locate_elements(self, locator: tuple[[], str], wait: int = 5) -> [WebElement]:
        """
       Locating elements with wait timeout and option to mark that elements
       :param locator: tuple - (By,str) - locator
       :param wait: timeout wait - int
       :return: the element that found
       :rtype: [WebElement]
        """
        elements = WebDriverWait(self._driver, wait).until(EC.presence_of_all_elements_located(locator))
        return elements

    def locate_frame(self, locator: tuple[[], str], wait: int = 5):
        """
       Locating frame with wait timeout
       :param locator: tuple - (By,str) - locator
       :param wait: timeout wait - int
        """
        try:
            self._driver.switch_to.frame(locator)
        except Exception:
            WebDriverWait(self._driver, wait).until(EC.frame_to_be_available_and_switch_to_it(locator))

    def switch_to_default(self):
        """
        Switching back to default content
        """
        self._driver.switch_to.default_content()

    def script_execute(self, __script: str):
        """
        Executing given JS script
        :param __script: string of JS script
        """
        self._driver.execute_script(__script)

    def get_screenshot(self) -> bytes:
        """
        Get driver screenshot
        :return: screenshot
        :rtype: bytes
        """
        return self._driver.get_screenshot_as_png()

    @property
    def title(self) -> str:
        """
        getter to title
        :return: title of page
        :rtype: str
        """
        return self._driver.title


    def text(self,locator) -> str:
        return locator.text