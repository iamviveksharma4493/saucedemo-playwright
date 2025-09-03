from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import pytest

@pytest.fixture
def login_page(browser):
    return LoginPage(browser)

def test_locked_out_user(login_page: LoginPage):
    login_page.login("locked_out_user", "secret_sauce") # Reusing login page object directly
    login_page.assert_error_message("Epic sadface: Sorry, this user has been locked out.")

def test_blank_username(browser):
    login = LoginPage(browser)
    login.login("", "secret_sauce")
    login.assert_error_message("Epic sadface: Password is required")    # Failed tc

def test_blank_password(login_page: LoginPage): # Added type hint ie LoginPage
    login_page.login("standard_user", "")
    assert login_page.is_error_displayed()

def test_blank_username_password(browser):
    login = LoginPage(browser)
    login.login("", "")
    # assert login.is_error_displayed()     # Old assertion
    login.assert_error_message("Epic sadface: Username is required")

# def test_blank_username(browser):
#     login = LoginPage(browser)
#     login.login("", "secret_sauce")
#     assert login.is_error_displayed()

def test_checkout_with_blank_user_info(browser):
    login = LoginPage(browser)
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(browser)
    inventory.add_item_to_cart()
    inventory.go_to_cart()

    cart = CartPage(browser)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(browser)
    checkout.fill_form_and_continue("", "", "")
    assert browser.is_visible("[data-test='error']")