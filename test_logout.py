from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

def test_logout():
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
        menu_button.click()

        time.sleep(2.5) 
        logout_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        )
        logout_button.click()

        time.sleep(2)
        assert driver.current_url == "https://www.saucedemo.com/"
        print("Logout başarılı")

    finally:
        driver.quit()
