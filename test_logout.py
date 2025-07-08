from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_logout():
	try:
		driver.get("https://www.saucedemo.com/")
		driver.maximize_window()
		time.sleep(1)

		driver.find_element(By.ID, "user-name").send_keys("standard_user")
		driver.find_element(By.ID, "password").send_keys("secret_sauce")
		driver.find_element(By.ID, "login-button").click()
		time.sleep(2)

		menu_button=driver.find_element(By.ID,"react-burger-menu-btn")
		menu_button.click()
		time.sleep(1)

		logout_button=driver.find_element(By.ID,"logout_sidebar_link")
		logout_button.click()
		time.sleep(2)

		current_url=driver.current_url
		if current_url == "https://www.saucedemo.com/" :
			print("Logout Başarılı")
		else:
			print("Logout başarısız")

	finally:
		driver.quit()

