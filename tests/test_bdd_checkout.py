import pytest
from pytest_bdd import scenario, given, when, then, parsers
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.config import BASE_URL, USERNAME_STANDARD, PASSWORD
from selenium.webdriver.common.by import By


# --- Scenarios ---
@scenario("checkout.feature", "Complete checkout flow")
def test_complete_checkout():
    pass

@scenario("checkout.feature", "Remove item from cart")
def test_remove_from_cart():
    pass

@scenario("checkout.feature", "Checkout with missing data")
def test_checkout_missing_data():
    pass


# --- Steps ---
@given("the user is logged in")
def user_logged_in(driver):
    driver.get(BASE_URL)
    LoginPage(driver).login(USERNAME_STANDARD, PASSWORD)


@given("the user has products in the cart")
def user_has_products_in_cart(driver):
    InventoryPage(driver).add_item_to_cart(0)
    InventoryPage(driver).add_item_to_cart(1)


@when("the user goes to the cart")
def go_to_cart(driver):
    InventoryPage(driver).click_cart()


@when("the user proceeds to checkout")
def proceed_to_checkout(driver):
    CartPage(driver).click_checkout()


@when("the user fills in checkout information")
def fill_checkout_info(driver):
    CheckoutPage(driver).fill_checkout_info("Juan", "Perez", "12345")


@when("the user finishes the order")
def finish_order(driver):
    CheckoutPage(driver).click_finish()


@when("the user goes back to products")
def go_back_to_products(driver):
    CheckoutPage(driver).click_back_home()


@when("the user clicks continue without filling information")
def click_continue_without_info(driver):
    CheckoutPage(driver).click_continue()


@then("the order summary should be displayed")
def verify_order_summary(driver):
    checkout_page = CheckoutPage(driver)
    assert checkout_page.get_subtotal() != ""
    assert checkout_page.get_tax() != ""
    assert checkout_page.get_total() != ""


@then("the user should see the confirmation message")
def verify_confirmation(driver):
    assert "Thank you for your order" in CheckoutPage(driver).get_complete_message()


@then("the user should see the products page")
def verify_products_page(driver):
    assert InventoryPage(driver).get_page_title() == "Products"


@when(parsers.parse("the user removes item {item_index:d} from the cart"))
def remove_item_from_cart(driver, item_index):
    CartPage(driver).remove_item(item_index)


@then(parsers.parse("the cart should contain {count:d} item"))
@then(parsers.parse("the cart should contain {count:d} items"))
def verify_cart_count_items(driver, count):
    assert InventoryPage(driver).get_cart_count() == count


@then("the user should see an error message")
def verify_error_displayed(driver):
    error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert error.is_displayed()


@then(parsers.parse('the error message should contain "{message}"'))
def verify_error_message(driver, message):
    error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert message in error.text
