from commons.driver import Driver
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver: Driver):
        self.driver = driver

    _common_locators = {
        "search": (By.NAME, 'submit_search'),
        "search_q": (By.ID, 'search_query_top')
    }

    def search(self, query: str) -> "ResultPage":
        """
        Perform Search some query
        :param query: a query to ask/searching
        :return: result page
        :rtype: ResultPage
        """
        from pages.result_page import ResultPage
        input_ = self.driver.locate_element(self._common_locators['search_q'])
        self.driver.send_keys(input_, query)
        self.driver.locate_element(self._common_locators['search']).click()
        return ResultPage(self.driver)

    @property
    def title(self) -> str:
        """
        getter to page title
        :return: title of the page
        :rtype: str
        """
        return self.driver.title
