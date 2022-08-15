from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckOutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    _locators = {
        'checkout_step_layer':(By.CLASS_NAME,'cart_navigation'),
        'checkout_step_btn':(By.CLASS_NAME,'button'),
        'checkout_step_1_btn':(By.NAME, 'processAddress'),
        'checkout_checker_btn':(By.ID, 'uniform-cgv'),
        'checkout_step_2_btn':(By.NAME, 'processCarrier'),
        'pay_hook_id':(By.ID, 'HOOK_PAYMENT'),
        'pay_hook_class':(By.CLASS_NAME,'row'),
        'bank_wire_btn':(By.CLASS_NAME, 'payment_module'),
        'confirm_btn_class':(By.CLASS_NAME, 'cart_navigation'),
        'confirm_btn':(By.CLASS_NAME, 'button')
    }
    def checkout_and_complete_purchase(self):
        step_1_layer = self.locate_element(self._locators['checkout_step_layer'])
        self.locate_element(self._locators['checkout_step_btn'],step_1_layer).click()
        self.locate_element(self._locators['checkout_step_1_btn']).click()
        self.locate_element(self._locators['checkout_checker_btn']).click()
        self.locate_element(self._locators['checkout_step_2_btn']).click()
        pay_hook_layer = self.locate_element(self._locators['pay_hook_id'])
        btn_layer_class = self.locate_element(self._locators['pay_hook_class'],pay_hook_layer)
        self.locate_element(self._locators['bank_wire_btn'],btn_layer_class).click()
        cofirm_class = self.locate_element(self._locators['confirm_btn_class'])
        self.locate_element(self._locators['confirm_btn'], cofirm_class).click()
