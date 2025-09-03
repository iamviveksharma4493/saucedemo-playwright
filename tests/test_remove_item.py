from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.remove_item_page import RemoveItemPage

def test_remove_item(browser):
    login = LoginPage(browser)
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(browser)
    inventory.add_item_to_cart()

    remover = RemoveItemPage(browser)
    remover.go_to_cart_and_remove()