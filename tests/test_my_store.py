import logging
import allure
import pytest
from playwright.sync_api import sync_playwright
from pages.main_page import MainPage
from commons.init_json import TestsData, CHROME, FIREFOX
from commons.driver import Driver
import ctypes

LOGGER = logging.getLogger(__name__)


@pytest.fixture
def init_data():
    data = TestsData.load("init.json")
    return data


@pytest.fixture
def driver_fix(init_data):
    user32 = ctypes.windll.user32
    screensize = {"width": user32.GetSystemMetrics(78), "height": user32.GetSystemMetrics(79)}
    if init_data.browser == CHROME:
        with sync_playwright() as p:
            driver = p.chromium.launch(headless=False, timeout=60000)
            page = driver.new_page()
            page.set_viewport_size(screensize)
            page.goto(init_data.url)
            yield page
            driver.close()

    if init_data.browser == FIREFOX:
        with sync_playwright() as p:
            driver = p.firefox.launch(headless=False)
            page = driver.new_page()
            page.set_viewport_size(screensize)
            page.goto(init_data.url)
            yield page
            driver.close()


@pytest.fixture
def main_page(driver_fix, request):
    init_driver = Driver(driver_fix)
    main_page = MainPage(init_driver)
    yield main_page
    if request.node.rep_call.failed:
        try:
            init_driver.script_execute("document.body.bgColor = 'white';")
            allure.attach(init_driver.get_screenshot(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
        except:
            pass
    del init_driver
    del main_page


@pytest.mark.valid
def test_login_valid(main_page, init_data):
    LOGGER.info("login valid test")
    authentication_page = main_page.sign_in()
    authentication_page.login(email=init_data.email, password=init_data.password)
    LOGGER.info(f"title: {authentication_page.title}")
    assert authentication_page.title == "My account - My Store"


@pytest.mark.invalid
def test_login_invalid_password(main_page, init_data):
    LOGGER.info("login invalid password test")
    authentication_page = main_page.sign_in()
    authentication_page.login(email=init_data.email, password="11")
    LOGGER.info(f"title: {authentication_page.title},msg: {authentication_page.get_authentication_message()}")
    assert authentication_page.get_authentication_message() == 'Invalid password.'


@pytest.mark.invalid
def test_login_wrong_password(main_page, init_data):
    LOGGER.info(f"login wrong password test")
    authentication_page = main_page.sign_in()
    authentication_page.login(email=init_data.email, password="mypass11")
    LOGGER.info(f"title: {authentication_page.title},msg: {authentication_page.get_authentication_message()}")
    assert authentication_page.get_authentication_message() == 'Authentication failed.'


@pytest.mark.invalid
def test_login_wrong_email(main_page):
    LOGGER.info("login wrong email test")
    authentication_page = main_page.sign_in()
    authentication_page.login(email="wrong!email@aa.co", password="mypass11")
    LOGGER.info(f"title: {authentication_page.title},msg: {authentication_page.get_authentication_message()}")
    assert authentication_page.get_authentication_message() == 'Authentication failed.'


@pytest.mark.invalid
def test_login_without_email(main_page):
    LOGGER.info("login without email test")
    authentication_page = main_page.sign_in()
    authentication_page.login(email="", password="mypass11")
    LOGGER.info(f"title: {authentication_page.title},msg: {authentication_page.get_authentication_message()}")
    assert authentication_page.get_authentication_message() == 'An email address required.'


@pytest.mark.invalid
def test_login_without_password(main_page, init_data):
    LOGGER.info("login without password test ")
    authentication_page = main_page.sign_in()
    authentication_page.login(email=init_data.email, password="")
    LOGGER.info(f"title: {authentication_page.title},msg: {authentication_page.get_authentication_message()}")
    assert authentication_page.get_authentication_message() == 'Password is required.'


@pytest.mark.invalid
def test_login_invalid_email(main_page):
    LOGGER.info("login without password test ")
    authentication_page = main_page.sign_in()
    authentication_page.login(email="v4vh666", password="bnv")
    LOGGER.info(f"title: {authentication_page.title},msg: {authentication_page.get_authentication_message()}")
    assert authentication_page.get_authentication_message() == 'Invalid email address.'

@pytest.mark.invalid
def test_login_without_email_and_password(main_page):
    LOGGER.info(f"login without email and password test")
    authentication_page = main_page.sign_in()
    authentication_page.login(email="", password="")
    LOGGER.info(f", title: {authentication_page.title},msg: {authentication_page.get_authentication_message()}")
    assert authentication_page.get_authentication_message() == 'An email address required.'


@pytest.mark.valid
def test_login_search_buy_cheapest(main_page, init_data):
    LOGGER.info(f"login search choose cheapest dress and buy.")
    authentication_page = main_page.sign_in()
    my_acc_page = authentication_page.login(email=init_data.email, password=init_data.password)
    result_page = my_acc_page.search("summer")
    dress = result_page.find_cheapest_product()
    result_page.add_product_to_cart(dress)
    checkout_page = result_page.process_to_checkout()
    checkout_page.checkout_and_complete_purchase()
    LOGGER.info(f"title: {authentication_page.title},msg: {authentication_page.get_authentication_message()}")
    assert checkout_page.title == 'Order confirmation - My Store'
