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


    def press_sign_in(self) -> None:
        self.locate_element(self._locators['submit_login']).click()

    def send_password(self,password:str)->None:
        self.locate_element(self._locators['pass_entry']).send_keys(password)

    def send_email(self,email:str) -> None:
        self.locate_element(self._locators['email_entry']).send_keys(email)

    def login(self,email:str,password:str) -> MyAccountPage:
        self.send_email(email)
        self.send_password(password)
        self.press_sign_in()
        return MyAccountPage(self.driver)