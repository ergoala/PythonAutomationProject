import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.config import BASE_URL, USERNAME_STANDARD, PASSWORD


@pytest.mark.regression
class TestCheckout:
    def login_and_add_products(self, driver):
        driver.get(BASE_URL)
        LoginPage(driver).login(USERNAME_STANDARD, PASSWORD)
        InventoryPage(driver).add_item_to_cart(0)
        InventoryPage(driver).add_item_to_cart(1)

    def test_flujo_completo_compra(self, driver):
        self.login_and_add_products(driver)

        inventory_page = InventoryPage(driver)
        inventory_page.click_cart()

        cart_page = CartPage(driver)
        assert cart_page.get_cart_item_count() == 2
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_info("Juan", "Perez", "12345")

        assert checkout_page.get_subtotal() != ""
        assert checkout_page.get_tax() != ""
        assert checkout_page.get_total() != ""
        checkout_page.click_finish()

        assert "Thank you for your order" in checkout_page.get_complete_message()

    def test_cancelar_checkout(self, driver):
        self.login_and_add_products(driver)

        inventory_page = InventoryPage(driver)
        inventory_page.click_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_info("Juan", "Perez", "12345")

        checkout_page.click_continue()
        checkout_page.click_back_home()

        assert inventory_page.get_page_title() == "Products"

    @pytest.mark.smoke
    def testEliminar_producto_del_carrito(self, driver):
        self.login_and_add_products(driver)

        inventory_page = InventoryPage(driver)
        inventory_page.click_cart()

        cart_page = CartPage(driver)
        assert cart_page.get_cart_item_count() == 2

        cart_page.remove_item(0)
        assert cart_page.get_cart_item_count() == 1

    def test_datos_faltantes_checkout(self, driver):
        self.login_and_add_products(driver)

        inventory_page = InventoryPage(driver)
        inventory_page.click_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.click_continue()

        error_message = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        assert error_message.is_displayed()
        assert "First Name is required" in error_message.text
