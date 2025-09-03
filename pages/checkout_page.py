from pages.base_page import BasePage

class CheckoutPage(BasePage):
    first_name = "#first-name"
    last_name = "#last-name"
    postal_code = "#postal-code"
    continue_button = "#continue"
    finish_button = "#finish"

    def fill_form_and_continue(self, fname, lname, zip_code):
        self.fill(self.first_name, fname)
        self.fill(self.last_name, lname)
        self.fill(self.postal_code, zip_code)
        self.click(self.continue_button)

    def finish_checkout(self):
        self.click(self.finish_button)