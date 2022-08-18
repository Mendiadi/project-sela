from pages.base_page import BasePage
from commons.driver import Driver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from pages.checkout_page import CheckOutPage


class ResultPage(BasePage):
    def __init__(self, driver: Driver):
        super().__init__(driver)

    _locators = {
        "products": (By.CLASS_NAME, 'product-container'),
        "product_link": (By.CLASS_NAME, 'product-image-container'),
        "right_block": (By.CLASS_NAME, 'right-block'),
        "price": (By.CLASS_NAME, 'content_price'),
        "price_span": (By.TAG_NAME, 'span'),
        "iframe_product": (By.CLASS_NAME, 'fancybox-iframe'),
        'add_to_card_btn': (By.ID, 'add_to_cart'),
        'checkout_layer': (By.ID, 'layer_cart'),
        'checkout_container': (By.CLASS_NAME, 'button-container'),
        'checkout_btn': (By.TAG_NAME, 'a'),
        'continue_shop': (By.CLASS_NAME, 'continue')
    }

    def product_list(self) -> [WebElement]:
        """
        Find all the products that search results found,
        :return: list of products that found
        :rtype: [WebElement]
        """
        return self.driver.locate_elements(self._locators['products'])

    def find_cheapest_product(self) -> WebElement:
        """
        Find all the products that search results found,
        locate the button and price value for each one,
        and find the cheapest product.
        :return: cheapest product that found
        :rtype: WebElement
        """
        products = self.product_list()
        list_of_prices = []
        for product in products:
            link = self.driver.locate_element(self._locators['product_link'], product)
            right_block = self.driver.locate_element(self._locators['right_block'], product)
            try:
                prices = self.driver.locate_element(self._locators['price'], right_block)
                price = self.driver.locate_element(self._locators["price_span"], prices)
            except Exception:
                price = self.driver.locate_element(self._locators['price'], right_block)
            list_of_prices.append((link, float(self.driver.text(price).replace("$", ""))))
        dress = min(list_of_prices, key=lambda t: t[1])[0]
        return dress

    def add_product_to_cart(self, product: WebElement):
        """
        Adding product to cart
        :param product: WebElement type - product
        """
        product.click()
        self.driver.locate_frame(self._locators['iframe_product'])
        self.driver.locate_element(self._locators['add_to_card_btn']).click()

    def process_to_checkout(self) -> CheckOutPage:
        """
        Clicking checkout button and move to checkout page
        :return: page of checkout process
        :rtype: CheckOutPage
        """
        layer = self.driver.locate_element(self._locators['checkout_layer'])
        btn_container = self.driver.locate_element(self._locators['checkout_container'], layer)
        self.driver.locate_element(self._locators['checkout_btn'], btn_container).click()
        return CheckOutPage(self.driver)

    def continue_shopping(self):
        """
        Clicking continue shopping.
        """
        layer = self.driver.locate_element(self._locators['checkout_layer'])
        btn_container = self.driver.locate_element(self._locators['checkout_container'], layer)
        self.driver.locate_element(self._locators['continue_shop'], btn_container).click()
