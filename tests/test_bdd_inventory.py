import pytest
from pytest_bdd import scenario, given, when, then, parsers
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import BASE_URL, USERNAME_STANDARD, PASSWORD


# --- Scenarios ---
@scenario("inventory.feature", "Page title is displayed")
def test_page_title():
    pass

@scenario("inventory.feature", "Products list is displayed")
def test_products_list():
    pass

@scenario("inventory.feature", "Product names are displayed")
def test_product_names():
    pass

@scenario("inventory.feature", "Product prices are displayed")
def test_product_prices():
    pass

@scenario("inventory.feature", "Add product to cart")
def test_add_to_cart():
    pass

@scenario("inventory.feature", "Add multiple products to cart")
def test_add_multiple_to_cart():
    pass


# --- Steps ---
@given("the user is logged in")
def user_logged_in(driver):
    driver.get(BASE_URL)
    LoginPage(driver).login(USERNAME_STANDARD, PASSWORD)


@given("the user is on the inventory page")
def on_inventory_page(driver):
    assert InventoryPage(driver).get_page_title() == "Products"


@then(parsers.parse('the page title should be "{title}"'))
def verify_page_title(driver, title):
    assert InventoryPage(driver).get_page_title() == title


@then(parsers.parse("the products list should contain {count:d} items"))
def verify_products_count(driver, count):
    assert len(InventoryPage(driver).get_all_items()) == count


@then("the products should have names")
def verify_products_have_names(driver):
    names = InventoryPage(driver).get_all_item_names()
    assert len(names) > 0


@then(parsers.parse('"{product}" should be in the product list'))
def verify_product_in_list(driver, product):
    names = InventoryPage(driver).get_all_item_names()
    assert product in names


@then("the products should have prices")
def verify_products_have_prices(driver):
    prices = InventoryPage(driver).get_all_item_prices()
    assert len(prices) > 0


@then(parsers.parse('all prices should start with "{prefix}"'))
def verify_prices_format(driver, prefix):
    prices = InventoryPage(driver).get_all_item_prices()
    for price in prices:
        assert price.startswith(prefix)


@when(parsers.parse("the user adds item {item_index:d} to the cart"))
def add_item_to_cart(driver, item_index):
    InventoryPage(driver).add_item_to_cart(item_index)


@then(parsers.parse("the cart should contain {count:d} item"))
@then(parsers.parse("the cart should contain {count:d} items"))
def verify_cart_count(driver, count):
    assert InventoryPage(driver).get_cart_count() == count
