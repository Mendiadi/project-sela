from pages.base_page import BasePage
from commons.driver import Driver
from selenium.webdriver.common.by import By


class MyAccountPage(BasePage):
    def __init__(self, driver: Driver):
        super().__init__(driver)

    _locators = {
        'icon_home': (By.CLASS_NAME, 'icon-home')
    }

    def click_home(self) -> "MainPage":
        """
        Clicking the home page button
        :return: main page
        :rtype: MainPage
        """
        from pages.main_page import MainPage
        self.driver.locate_element(self._locators['icon_home'], mark=True).click()
        return MainPage(self.driver)
