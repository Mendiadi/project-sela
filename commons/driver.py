from playwright.sync_api import Page, Locator,ElementHandle


class Driver:
    def __init__(self, driver: Page):
        self._driver = driver


    def click(self,locator:str):
        self._driver.click(locator)

    def locate_element(self, locator: str, driver: [] = None, wait: int = 5, mark=False) -> Locator:
        """
        Locating element with wait timeout and option to mark that element
        :param locator: tuple - (By,str) - locator
        :param driver: optional - some WebElement to search inside
        :param wait: timeout wait - int
        :param mark: bool - True to mark , False to not mark
        :return: the element that found
        :rtype: Locator
        """
        if driver is None:
            driver = self._driver
        if driver.is_visible(locator,timeout=wait):
            element = driver.locator(locator)
            if mark:
                self._driver.evaluate("arguments[0].style.border='2px solid red'", element)
            return element

    def query_select(self, locator: str, driver: [] = None, wait: int = 5, mark=False) -> ElementHandle:
        """
        Locating element with wait timeout and option to mark that element
        :param locator: tuple - (By,str) - locator
        :param driver: optional - some WebElement to search inside
        :param wait: timeout wait - int
        :param mark: bool - True to mark , False to not mark
        :return: the element that found
        :rtype: ElementHandle
        """
        if driver is None:
            driver = self._driver
        if driver.is_visible(locator):
            element = driver.query_selector(locator)
            if mark:
                self._driver.evaluate("arguments[0].style.border='2px solid red'", element)
            return element

    def locate_elements(self, locator: str, wait: int = 5) -> [ElementHandle]:
        """
       Locating elements with wait timeout and option to mark that elements
       :param locator: tuple - (By,str) - locator
       :param wait: timeout wait - int
       :param mark: bool - True to mark , False to not mark
       :return: the element that found
       :rtype: [ElementHandle]
        """
        if self._driver.is_visible(locator, timeout=wait):
            elements = self._driver.query_selector_all(locator)
            return elements

    def script_execute(self, __script: str):
        """
        Executing given JS script
        :param __script: string of JS script
        """
        self._driver.evaluate(__script)

    def get_screenshot(self) -> bytes:
        """
        Get driver screenshot
        :return: screenshot
        :rtype: bytes
        """
        return self._driver.screenshot()

    @property
    def title(self) -> str:
        """
        getter to title
        :return: title of page
        :rtype: str
        """
        return self._driver.title()
