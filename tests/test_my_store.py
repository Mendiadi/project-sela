import logging
import time
import allure
import pytest
from selenium.webdriver import Chrome
from pages.main_page import MainPage
from tests.init_json import TestsData

LOGGER = logging.getLogger(__name__)


@pytest.fixture
def init_data():
    data = TestsData.load("init.json")
    return data


@pytest.fixture
def main_page(init_data,request):
    driver = Chrome()
    driver.get(init_data.url)
    driver.maximize_window()
    main_page = MainPage(driver)
    yield main_page
    if request.node.rep_call.failed:
        try:
            driver.execute_script("document.body.bgColor = 'white';")
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
        except:
            pass
    driver.quit()
    del main_page


def test_login_valid(main_page,init_data):
    autho_page = main_page.sign_in()
    autho_page.login(email=init_data.email,password=init_data.password)


def test_login_invalid_password(main_page,init_data):
    autho_page = main_page.sign_in()
    autho_page.login(email=init_data.email,password="11")

def test_login_wrong_password(main_page,init_data):
    autho_page = main_page.sign_in()
    autho_page.login(email=init_data.email,password="mypass11")


def test_login_wrong_email(main_page, init_data):
    autho_page = main_page.sign_in()
    autho_page.login(email="wrong!email@aa.co", password="mypass11")


def test_login_without_email(main_page, init_data):
    autho_page = main_page.sign_in()
    autho_page.login(email="", password="mypass11")

def test_login_without_password(main_page, init_data):
    autho_page = main_page.sign_in()
    autho_page.login(email=init_data.email, password="")

def test_login_without_email_and_password(main_page, init_data):
    autho_page = main_page.sign_in()
    autho_page.login(email="", password="")

def test_buy_summer(main_page, init_data):
    autho_page = main_page.sign_in()
    my_acc_page = autho_page.login(email=init_data.email, password=init_data.password)
    main_page_ = my_acc_page.click_home()
    result_page = main_page_.search("summer")
    dress = result_page.find_cheapest_product()
    result_page.add_product_to_cart(dress)
    checkout_page = result_page.process_to_checkout()
    checkout_page.checkout_and_complete_purchase()
    time.sleep(5)
