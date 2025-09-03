from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.cancel_order_page import CancelOrderPage

def test_cancel_order_flow(browser):
    login = LoginPage(browser)
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(browser)
    inventory.add_item_to_cart()
    inventory.go_to_cart()

    cart = CartPage(browser)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(browser)
    checkout.fill_form_and_continue("Vivek", "Sharma", "12345")

    cancel = CancelOrderPage(browser)
    cancel.cancel_checkout()