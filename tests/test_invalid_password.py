from pages.login_page import LoginPage

def test_invalid_password(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "wrong_password")
    assert "Epic sadface" in login.get_error_message()
