from pages.base_page import BasePage
from selenium.webdriver import Chrome


class ResultPage(BasePage):
    def __init__(self,driver:Chrome):
        super().__init__(driver)