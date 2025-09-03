from pages.base_page import BasePage

class ConfirmationPage(BasePage):
    complete_header = ".complete-header"

    def is_order_complete(self):
        self.assert_text(self.complete_header, "Thank you for your order!")
