from pages.base_page import BasePage

class CartPage(BasePage):
    checkout_button = "#checkout"
    remove_button = "#remove-sauce-labs-backpack"

    def proceed_to_checkout(self):
        self.click(self.checkout_button)

    def remove_item(self):
        self.click(self.remove_button)