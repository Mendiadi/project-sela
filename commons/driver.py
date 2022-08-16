from playwright.sync_api import Page, Locator, ElementHandle, FrameLocator


class Driver:
    def __init__(self, driver: Page):
        self._driver = driver

    @staticmethod
    def send_keys(locator_: [], keys: str) -> None:
        """
        Send keys to input
        :param locator_: element locator to send keys
        :param keys: some string
        """
        locator_.fill(keys)

    def locate_element(self, locator: str, driver: [] = None) -> [Locator, ElementHandle]:
        """
        Locating element with wait timeout and option to mark that element
        :param locator: tuple - (By,str) - locator
        :param driver: optional - some WebElement to search inside
        :return: the element that found
        :rtype: Locator
        """
        if driver is None:
            driver = self._driver

        try:
            element = driver.locator(locator)

            return element
        except:
            element = driver.query_selector(locator)
            return element

    def locate_elements(self, locator: str) -> [ElementHandle]:
        """
       Locating elements with wait timeout and option to mark that elements
       :param locator: tuple - (By,str) - locator
       :return: the element that found
       :rtype: [ElementHandle]
        """
        # if self._driver.is_visible(locator, timeout=wait):
        elements = self._driver.query_selector_all(locator)
        return elements
        # else:
        #     raise TimeoutError

    def locate_frame(self, locator: str) -> FrameLocator:
        """
        Locate frame
        :param locator: frame locator
        :return: frame
        :rtype: FrameLocator
        """
        frame = self._driver.frame_locator(locator)
        return frame

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
