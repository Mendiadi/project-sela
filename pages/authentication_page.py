from pages.base_page import BasePage
from commons.driver import Driver
from pages.my_account_page import MyAccountPage


class AuthenticationPage(BasePage):
    def __init__(self, driver: Driver):
        super().__init__(driver)

    _locators = {
        "email_entry": 'id=email',
        "pass_entry": 'id=passwd',
        "submit_login": "id=SubmitLogin",
        "message_layer": '.alert',
        "message_text": 'li'
    }

    def press_sign_in(self) -> None:
        """
        Perform pressing sign_in button.
        """
        self.driver.locate_element(self._locators['submit_login']).click()

    def send_password(self, password: str) -> None:
        """
        Perform send password to entry.
        :param password: (string) your password
        """
        input_ = self.driver.locate_element(self._locators['pass_entry'])
        self.driver.send_keys(input_, password)

    def send_email(self, email: str) -> None:
        """
        Perform send email to entry.
        :param email: (string) your email
        """
        input_ = self.driver.locate_element(self._locators['email_entry'])
        self.driver.send_keys(input_, email)

    def login(self, email: str, password: str) -> MyAccountPage:
        """
        Perform login operation and return "my account page"
        :param email: string represent your email
        :param password:  string represent your password
        :return: object of MyAccountPage
        :rtype: MyAccountPage
        """
        self.send_email(email)
        self.send_password(password)
        self.press_sign_in()
        return MyAccountPage(self.driver)

    def get_authentication_message(self) -> str:
        """
        Get the message label in authentication alert.
        :return: message of authentication
        :rtype: str
        """
        layer = self.driver.locate_element(self._locators['message_layer'])
        text = self.driver.locate_element(self._locators['message_text'], layer)
        return self.driver.text(text)