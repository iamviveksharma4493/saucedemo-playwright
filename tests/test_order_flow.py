from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage

def test_order_flow(browser, credentials):
    login = LoginPage(browser)
    login.login(credentials["username"], credentials["password"])

    inventory = InventoryPage(browser)
    print("Inside test class")  # Comment added to debug
    inventory.add_item_to_cart()
    inventory.go_to_cart()

    cart = CartPage(browser)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(browser)
    checkout.fill_form_and_continue(
        credentials["first_name"], 
        credentials["last_name"], 
        credentials["postal_code"]
        )
    checkout.finish_checkout()

    confirm = ConfirmationPage(browser)
    confirm.is_order_complete()