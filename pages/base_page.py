from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def wait_for_selector(self, locator):
        self.page.wait_for_selector(locator)

    def click(self, locator):
        self.wait_for_selector(locator)
        self.page.click(locator)

    def fill(self, locator, text):
        self.wait_for_selector(locator)
        self.page.fill(locator, text)

    def get_text(self, locator):
        self.wait_for_selector(locator)
        return self.page.text_content(locator)
    
    def select_option_by_text(self, locator, text):
        self.page.select_option(locator, label=text)

    # New assertion
    def assert_text(self, locator, expected):
        actual = self.get_text(locator)
        print(f"[DEBUG] Actual text from '{locator}': '{actual}'")  # Optional debug print
        assert expected.lower() in actual.lower(), f"Expected '{expected}' in '{actual}'"

    def assert_login_error_message(self, locator, expected):
        actual = self.get_text(locator)
        assert expected in actual    

    # Old assertion
    # def assert_text(self, locator, expected):
    #     actual = self.get_text(locator)
    #     assert expected in actual
