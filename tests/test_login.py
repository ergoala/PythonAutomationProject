import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import BASE_URL, USERNAME_STANDARD, PASSWORD


class TestLogin:
    def test_login_exitoso(self, driver):
        driver.get(BASE_URL)

        login_page = LoginPage(driver)
        login_page.login(USERNAME_STANDARD, PASSWORD)

        inventory_page = InventoryPage(driver)
        assert inventory_page.get_page_title() == "Products"

    def test_login_usuario_invalido(self, driver):
        driver.get(BASE_URL)

        login_page = LoginPage(driver)
        login_page.login("wrong_user", "wrong_password")

        assert login_page.is_error_displayed()
        assert "Username and password do not match" in login_page.get_error_message()

    def test_login_usuario_bloqueado(self, driver):
        driver.get(BASE_URL)

        login_page = LoginPage(driver)
        login_page.login("locked_out_user", PASSWORD)

        assert login_page.is_error_displayed()
        assert "locked out" in login_page.get_error_message()

    @pytest.mark.smoke
    def test_login_campos_vacios(self, driver):
        driver.get(BASE_URL)

        login_page = LoginPage(driver)
        login_page.click_login()

        assert login_page.is_error_displayed()
        assert "Username is required" in login_page.get_error_message()
