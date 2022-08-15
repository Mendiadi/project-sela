from pages.base_page import BasePage
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class MyAccountPage(BasePage):
    def __init__(self, driver: Chrome):
        super().__init__(driver)

    locators = {
        'icon_home': (By.CLASS_NAME, 'icon-home')
    }

    def click_home(self) -> "MainPage":
        from pages.main_page import MainPage
        self.locate_element(self.locators['icon_home'],mark=True).click()
        return MainPage(self.driver)
