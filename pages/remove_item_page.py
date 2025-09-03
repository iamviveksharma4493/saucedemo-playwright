from pages.base_page import BasePage

class RemoveItemPage(BasePage):
    cart_icon = ".shopping_cart_link"
    remove_button = "#remove-sauce-labs-backpack"

    def go_to_cart_and_remove(self):
        self.click(self.cart_icon)
        self.click(self.remove_button)