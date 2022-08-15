from pages.base_page import BasePage
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from pages.checkout_page import CheckOutPage


class ResultPage(BasePage):
    def __init__(self, driver: Chrome):
        super().__init__(driver)

    locators = {
        "products": (By.CLASS_NAME, 'product-container'),
        "product_link": (By.CLASS_NAME, 'product-image-container'),
        "right_block": (By.CLASS_NAME, 'right-block'),
        "price": (By.CLASS_NAME, 'content_price'),
        "price_span": (By.TAG_NAME, 'span'),
        "iframe_product": (By.CLASS_NAME, 'fancybox-iframe'),
        'add_to_card_btn': (By.ID, 'add_to_cart'),
        'checkout_layer': (By.ID, 'layer_cart'),
        'checkout_container': (By.CLASS_NAME, 'button-container'),
        'checkout_btn': (By.CLASS_NAME, 'btn'),
        'continue_shop': (By.CLASS_NAME, 'continue')
    }

    def product_list(self) -> [WebElement]:
        return self.locate_elements(self.locators['products'])

    def find_cheapest_product(self) -> [WebElement]:
        """
        Find all the products that search results found,
        locate the button and price value for each one,
        and find the cheapest product.
        """
        products = self.product_list()
        list_of_prices = []
        for product in products:
            link = self.locate_element(self.locators['product_link'], product)
            right_block = self.locate_element(self.locators['right_block'], product)
            try:
                prices = self.locate_element(self.locators['price'], right_block)
                price = self.locate_element(self.locators["price_span"], prices)
            except Exception:
                price = self.locate_element(self.locators['price'], right_block)
            list_of_prices.append((link, float(price.text.replace("$", ""))))
        dress = min(list_of_prices, key=lambda t: t[1])[0]
        return dress

    def add_product_to_cart(self, product: WebElement):
        product.click()
        self.locate_and_switch_to_frame(self.locators['iframe_product'])
        self.locate_element(self.locators['add_to_card_btn']).click()

    def process_to_checkout(self) -> CheckOutPage:
        layer = self.locate_element(self.locators['checkout_layer'])
        btn_container = self.locate_element(self.locators['checkout_container'], layer)
        self.locate_element(self.locators['checkout_btn'], btn_container).click()
        return CheckOutPage(self.driver)

    def continue_shopping(self):
        layer = self.locate_element(self.locators['checkout_layer'])
        btn_container = self.locate_element(self.locators['checkout_container'], layer)
        self.locate_element(self.locators['continue_shop'], btn_container).click()
