from pages.base_page import BasePage

class LoginPage(BasePage):
    username_input = "#user-name"
    password_input = "#password"
    login_button = "#login-button"
    error_message = "[data-test='error']"

    def __init__(self, page):
        super().__init__(page)
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)

    def is_error_displayed(self):   # Returns boolean, only check error msg is there or not
        return self.page.is_visible(self.error_message)

    def get_error_message(self):
        self.wait_for_selector(self.error_message)
        return self.get_text(self.error_message)

    def assert_error_message(self, expected_message):
        actual = self.get_error_message()
        assert actual == expected_message, f"\nExpected: {expected_message}\nActual: {actual}"