from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_add_to_chart():
	try:
		driver.get("https://www.saucedemo.com/")
		driver.maximize_window()
		time.sleep(1)

		driver.find_element(By.ID, "user-name").send_keys("standard_user")
		driver.find_element(By.ID, "password").send_keys("secret_sauce")
		driver.find_element(By.ID, "login-button").click()
		time.sleep(2)

		driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
		time.sleep(1)

		cart_badge=driver.find_element(By.CLASS_NAME,"shopping_cart_link")

		if cart_badge.text=="1":
			print("add to chart sayacı doğru çalışıyor")
		else:
			print("Add to chart sayacı hatalı")
		
		cart_item=driver.find_element(By.CLASS_NAME,"inventory_item_name")
		if "Backpack" in cart_item.text:
			print("Sepette doğru ürün görünüyor")
		else:
			print("Sepette yanlış ürün görünüyor")

	finally:
		driver.quit()
