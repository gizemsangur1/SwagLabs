from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")
        self.add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_item_name = (By.CLASS_NAME, "inventory_item_name")

    def logout(self):
        self.driver.find_element(*self.menu_button).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.logout_link)
        ).click()

    def is_logged_out(self):
        WebDriverWait(self.driver, 5).until(
            EC.url_to_be("https://www.saucedemo.com/")
        )
        return self.driver.current_url == "https://www.saucedemo.com/"

    def add_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart_btn).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_badge).text

    def get_cart_item_name(self):
        return self.driver.find_element(*self.cart_item_name).text
