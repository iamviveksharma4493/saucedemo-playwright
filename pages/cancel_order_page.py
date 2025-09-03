from pages.base_page import BasePage

class CancelOrderPage(BasePage):
    cancel_button = "#cancel"

    def cancel_checkout(self):
        self.click(self.cancel_button)