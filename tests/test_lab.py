import pytest
from selenium.webdriver import Chrome
from pages.main_page import MainPage
from tests.init_json import TestsData

"""
def test_buy_summer(main_page):
    Authntication_page = main_page.SignIn()
    MyAccount_page = Authntication_page.login("user","password")
    main_page  = MyAccount_page.home()
    searchReslut_page = main_page.search("summer")

"""
@pytest.fixture
def init_data():
    data = TestsData.load("init.json")
    return data

@pytest.fixture
def main_page():
    driver = Chrome()
    driver.get('http://automationpractice.com/index.php')
    driver.maximize_window()
    main_page = MainPage(driver)
    yield main_page


def test_buy_summer(main_page,init_data):
    autho_page = main_page.sign_in()
    my_acc_page = autho_page.login(init_data.email,init_data.password)
    main_page_ = my_acc_page.home()
    result_page = main_page_.search("summer")
