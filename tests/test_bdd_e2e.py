import pytest
from pytest_bdd import scenario, given, when, then, parsers
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.config import BASE_URL, USERNAME_STANDARD, PASSWORD


# --- Scenarios ---
@scenario("E2E.feature", "Complete purchase flow - Happy Path")
def test_e2e_happy_path():
    pass

# --- Steps ---
@given("the user is on the login page")
def go_to_login(driver):
    driver.get(BASE_URL)


@when("the user enters valid credentials")
def enter_valid_credentials(driver):
    LoginPage(driver).login(USERNAME_STANDARD, PASSWORD)


@then("the user should see the products page")
def verify_products_page(driver):
    assert InventoryPage(driver).get_page_title() == "Products"


@when(parsers.parse("the user adds item {item_index:d} to the cart"))
def add_item_to_cart(driver, item_index):
    InventoryPage(driver).add_item_to_cart(item_index)


@when(parsers.parse('the user adds "{product_name}" to the cart'))
def add_named_product_to_cart(driver, product_name):
    inventory_page = InventoryPage(driver)
    names = inventory_page.get_all_item_names()
    index = names.index(product_name)
    inventory_page.add_item_to_cart(index)


@when("the user goes to the cart")
def go_to_cart(driver):
    InventoryPage(driver).click_cart()


@then(parsers.parse("the cart should contain {count:d} items"))
def verify_cart_count(driver, count):
    assert InventoryPage(driver).get_cart_count() == count


@when("the user proceeds to checkout")
def proceed_to_checkout(driver):
    CartPage(driver).click_checkout()


@when("the user fills in checkout information")
def fill_checkout_info(driver):
    CheckoutPage(driver).fill_checkout_info("Juan", "Perez", "12345")


@then("the order summary should be displayed")
def verify_order_summary(driver):
    checkout_page = CheckoutPage(driver)
    assert checkout_page.get_subtotal() != ""
    assert checkout_page.get_tax() != ""
    assert checkout_page.get_total() != ""


@when("the user finishes the order")
def finish_order(driver):
    CheckoutPage(driver).click_finish()


@then("the user should see the confirmation message")
def verify_confirmation(driver):
    assert CheckoutPage(driver).get_complete_message() != ""


@then(parsers.parse('the confirmation message should contain "{message}"'))
def verify_confirmation_message(driver, message):
    assert message in CheckoutPage(driver).get_complete_message()


@when(parsers.parse("the user removes item {item_index:d} from the cart"))
def remove_item_from_cart(driver, item_index):
    CartPage(driver).remove_item(item_index)


@then(parsers.parse('"{product_name}" should be in the cart'))
def verify_product_in_cart(driver, product_name):
    cart_page = CartPage(driver)
    names = cart_page.get_item_names()
    assert product_name in names
