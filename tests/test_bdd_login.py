import pytest
from pytest_bdd import scenario, given, when, then, parsers
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import BASE_URL, USERNAME_STANDARD, PASSWORD, USERNAME_LOCKED_OUT


# --- Scenarios ---
@scenario("login.feature", "Successful login")
def test_successful_login():
    pass

@scenario("login.feature", "Login with invalid credentials")
def test_login_invalid_credentials():
    pass

@scenario("login.feature", "Login with locked out user")
def test_login_locked_out_user():
    pass

@scenario("login.feature", "Login with empty fields")
def test_login_empty_fields():
    pass


# --- Steps ---
@given("the user is on the login page")
def go_to_login(driver):
    driver.get(BASE_URL)


@when("the user enters valid credentials")
def enter_valid_credentials(driver):
    LoginPage(driver).login(USERNAME_STANDARD, PASSWORD)


@when("the user enters invalid credentials")
def enter_invalid_credentials(driver):
    LoginPage(driver).login("wrong_user", "wrong_password")


@when("the user enters locked out user credentials")
def enter_locked_out_credentials(driver):
    LoginPage(driver).login(USERNAME_LOCKED_OUT, PASSWORD)


@when("the user clicks the login button")
def click_login_button(driver):
    LoginPage(driver).click_login()


@then("the user should see the products page")
def verify_products_page(driver):
    assert InventoryPage(driver).get_page_title() == "Products"


@then("the user should see an error message")
def verify_error_displayed(driver):
    assert LoginPage(driver).is_error_displayed()


@then(parsers.parse('the error message should contain "{message}"'))
def verify_error_message(driver, message):
    assert message in LoginPage(driver).get_error_message()
