from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

def test_login():
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(1)

        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")

        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()
        time.sleep(2)

        current_url = driver.current_url
        if "inventory.html" in current_url:
            print("Giriş başarılı: Test geçti.")
        else:
            print("Giriş başarısız: Test başarısız.")

    finally:
        driver.quit()
