from pages.base_page import BasePage
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from pages.my_account_page import MyAccountPage

class AuthoPage(BasePage):
    def __init__(self,driver:Chrome):
        super().__init__(driver)
        self._locators = {
            "email_entry":(By.NAME,'email'),
            "pass_entry": (By.NAME, 'passwd'),
            "submit_login":(By.ID,"SubmitLogin")
        }

    def login(self,user:str,password:str) -> MyAccountPage:
        self.locate_element(self._locators['email_entry']).send_keys(user)
        self.locate_element(self._locators['pass_entry']).send_keys(password)
        self.locate_element(self._locators['submit_login']).click()
        return MyAccountPage(self.driver)