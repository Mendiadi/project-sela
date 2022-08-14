from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.autho_page import AuthoPage
from pages.result_page import ResultPage


class MainPage(BasePage):
    def __init__(self, driver: Chrome):
        super().__init__(driver)
    locators = {
        "sign_in":(By.CLASS_NAME, "login"),
        "search": (By.NAME, 'submit_search'),
        "search_q": (By.ID, 'search_query_top')
    }

    def sign_in(self) -> AuthoPage:
        sign_in_btn = self.locate_element(self.locators['sign_in'])
        sign_in_btn.click()
        return AuthoPage(self.driver)

    def search(self, query: str):
        self.locate_element(self.locators['search_q']).send_keys(query)
        self.locate_element(self.locators['search']).click()
        return ResultPage(self.driver)


