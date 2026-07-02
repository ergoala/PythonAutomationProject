import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import BASE_URL, USERNAME_STANDARD, PASSWORD


@pytest.mark.smoke
class TestInventory:
    def login(self, driver):
        driver.get(BASE_URL)
        LoginPage(driver).login(USERNAME_STANDARD, PASSWORD)

    def test_titutlo_pagina(self, driver):
        self.login(driver)
        inventory_page = InventoryPage(driver)
        assert inventory_page.get_page_title() == "Products"

    def test_listado_productos(self, driver):
        self.login(driver)
        inventory_page = InventoryPage(driver)
        items = inventory_page.get_all_items()
        assert len(items) == 6

    def test_nombres_productos(self, driver):
        self.login(driver)
        inventory_page = InventoryPage(driver)
        names = inventory_page.get_all_item_names()
        assert "Sauce Labs Backpack" in names
        assert "Sauce Labs Bike Light" in names

    def test_precios_productos(self, driver):
        self.login(driver)
        inventory_page = InventoryPage(driver)
        prices = inventory_page.get_all_item_prices()
        assert len(prices) == 6
        for price in prices:
            assert price.startswith("$")

    def test_agregar_producto_al_carrito(self, driver):
        self.login(driver)
        inventory_page = InventoryPage(driver)
        inventory_page.add_item_to_cart(0)
        assert inventory_page.get_cart_count() == 1

    def test_agregar_multiples_productos(self, driver):
        self.login(driver)
        inventory_page = InventoryPage(driver)
        inventory_page.add_item_to_cart(0)
        inventory_page.add_item_to_cart(1)
        inventory_page.add_item_to_cart(2)
        assert inventory_page.get_cart_count() == 3
