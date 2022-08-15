from commons.driver import Driver


class BasePage:
    def __init__(self, driver: Driver):
        self.driver = driver



    def get_message(self):
        pass

