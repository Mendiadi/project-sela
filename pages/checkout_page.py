from pages.base_page import BasePage
from commons.driver import Driver


class CheckOutPage(BasePage):
    def __init__(self, driver: Driver):
        super().__init__(driver)

    _locators = {
        'checkout_step_layer': '.cart_navigation',
        'checkout_step_btn': '.button',
        'checkout_checker_btn': 'id=uniform-cgv',
        'pay_hook_id': 'id=HOOK_PAYMENT',
        'pay_hook_class': '.row',
        'bank_wire_btn': '.payment_module'
    }

    def checkout_and_complete_purchase(self):
        """
        Perform all checkout steps to finally purchase success.
        """
        self.click_process_continue()
        self.click_process_continue()
        self.driver.locate_element(self._locators['checkout_checker_btn']).click()
        self.click_process_continue()
        pay_hook_layer = self.driver.locate_element(self._locators['pay_hook_id'])
        btn_layer_class = self.driver.locate_element(self._locators['pay_hook_class'], pay_hook_layer)
        self.driver.locate_element(self._locators['bank_wire_btn'], btn_layer_class).click()
        self.click_process_continue()

    def click_process_continue(self):
        """
        Perform clicking on continue button to move steps
        """
        layer = self.driver.locate_element(self._locators['checkout_step_layer'])
        self.driver.locate_element(self._locators['checkout_step_btn'], layer).click()
