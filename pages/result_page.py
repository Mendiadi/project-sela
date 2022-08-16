from pages.base_page import BasePage
from commons.driver import Driver
from playwright.sync_api import Page, ElementHandle
from pages.checkout_page import CheckOutPage


class ResultPage(BasePage):
    def __init__(self, driver: Driver):
        super().__init__(driver)

    _locators = {
        "products": '.product-container',
        "product_link": '.product-image-container',
        "right_block": '.right-block',
        "price": '.content_price',
        "price_span": 'span',
        "iframe_product": '.fancybox-iframe',
        'add_to_card_btn': 'id=add_to_cart',
        'checkout_layer': 'id=layer_cart',
        'checkout_container': '.button-container',
        'checkout_btn': 'a',
        'continue_shop': '.continue'
    }

    def product_list(self) -> [ElementHandle]:
        """
        Find all the products that search results found,
        :return: list of products that found
        :rtype: [ElementHandle]
        """
        return self.driver.locate_elements(self._locators['products'])

    def find_cheapest_product(self) -> ElementHandle:
        """
        Find all the products that search results found,
        locate the button and price value for each one,
        and find the cheapest product.
        :return: cheapest product that found
        :rtype: ElementHandle
        """
        products = self.product_list()
        list_of_prices = []
        for product in products:
            link = self.driver.query_select(self._locators['product_link'], product)
            right_block = self.driver.query_select(self._locators['right_block'], product)
            try:
                prices = self.driver.query_select(self._locators['price'], right_block)
                price = self.driver.query_select(self._locators["price_span"], prices)
            except Exception:
                price = self.driver.query_select(self._locators['price'], right_block)
            list_of_prices.append((link, float(price.text_content().replace("$", ""))))
        dress = min(list_of_prices, key=lambda t: t[1])[0]
        return dress

    def add_product_to_cart(self, product: ElementHandle):
        """
        Adding product to cart
        :param product: ElementHandle type - product
        """
        product.click()
        frame = self.driver.locate_element(self._locators['iframe_product'])
        self.driver.locate_element(self._locators['add_to_card_btn'], frame).click()

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
