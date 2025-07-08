from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_invalid_password():
	try:
		driver.get("https://www.saucedemo.com/")
		driver.maximize_window()
		time.sleep(1)

		username = driver.find_element(By.ID, "user-name")
		password = driver.find_element(By.ID, "password")
		username.send_keys("standard_user")
		password.send_keys("wrong_password")

		login_btn = driver.find_element(By.ID, "login-button")
		login_btn.click()
		time.sleep(2)

		error_msg = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
		expected_msg = "Epic sadface: Username and password do not match any user in this service"

		if expected_msg in error_msg.text:
			print("Hatalı parola testi geçti.")
		else:
			print("Beklenen hata mesajı görünmedi.")

	finally:
		driver.quit()
