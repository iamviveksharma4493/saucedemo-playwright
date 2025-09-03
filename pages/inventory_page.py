from pages.base_page import BasePage

class InventoryPage(BasePage):
    add_to_cart_button = "#add-to-cart-sauce-labs-backpack"
    cart_icon = ".shopping_cart_link"
    sort_dropdown = '//select[@class="product_sort_container"]'
    item_prices = '.inventory_item_price'

    def add_item_to_cart(self):
        print("Going to click on add button")   # Added comment to debug
        self.click(self.add_to_cart_button)
        print("Add button clicked") # Added to debug

    def go_to_cart(self):
        self.click(self.cart_icon)

    def sort_items_by(self, option_text):
        self.page.wait_for_timeout(3000)  # 1 second wait before sort drop down appear
        #self.click(self.sort_dropdown)
        print("going to click on drop down")
        self.wait_for_selector(self.sort_dropdown)
        print("drop down found")
        self.page.select_option(self.sort_dropdown, label=option_text)
        print("drop down value selected")

    # def sort_items_by(self, option_text):
    #     self.wait_for_selector(self.sort_dropdown)
    #     self.click(self.sort_dropdown)  # Trying with click
        # self.select_option_by_text(self.sort_dropdown, option_text)

    def get_all_item_prices(self):
        print("Inside get all item prices")
        self.wait_for_selector(self.item_prices)
        print("selector found")
        prices = self.page.locator(self.item_prices).all_text_contents()
        # Convert $ values to float
        return [float(price.replace("$", "")) for price in prices]