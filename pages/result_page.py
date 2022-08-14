from pages.base_page import BasePage
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
class ResultPage(BasePage):
    def __init__(self,driver:Chrome):
        super().__init__(driver)

    locators = {
        "products":(By.CLASS_NAME,'product-container'),
        "product_link":(By.CLASS_NAME,'product-image-container'),
        "right_block":(By.CLASS_NAME,'right-block'),
        "price":(By.CLASS_NAME,'content_price'),
        "price_span":(By.TAG_NAME, 'span')
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
            link = self.locate_element(self.locators['product_link'],product)
            right_block = self.locate_element(self.locators['right_block'],product)
            try:
                prices = self.locate_element(self.locators['price'],right_block)
                price = self.locate_element(self.locators["price_span"],prices)
            except Exception:
                price = self.locate_element(self.locators['price'],right_block)
            list_of_prices.append((link, float(price.text.replace("$", ""))))
        to_click = min(list_of_prices, key=lambda t: t[1])[0]
        return to_click