from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_sort_items_by_price_low_to_high(browser):
    login = LoginPage(browser)
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(browser)
    inventory.sort_items_by("Price (low to high)")
    prices = inventory.get_all_item_prices()

    # Validate prices are sorted
    assert prices == sorted(prices), f"Prices not sorted: {prices}"
