from pages.login_page import LoginPage

def test_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url
