from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_logout(driver):
    login_page = LoginPage(driver)
    inventory = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    inventory.logout()

    assert inventory.is_logged_out()
