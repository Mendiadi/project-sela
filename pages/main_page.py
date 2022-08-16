from commons.driver import Driver
from pages.base_page import BasePage
from pages.authentication_page import AuthenticationPage


class MainPage(BasePage):
    def __init__(self, driver: Driver):
        super().__init__(driver)

    _locators = {
        "sign_in": ".login"
    }

    def sign_in(self) -> AuthenticationPage:
        """
        Click Signin button
        :return: object of authentication page
        :rtype: AuthenticationPage
        """
        sign_in_btn = self.driver.locate_element(self._locators['sign_in'])
        sign_in_btn.click()
        return AuthenticationPage(self.driver)
