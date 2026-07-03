import pytest
from pytest_bdd import scenario, given, when, then
from pages.E2E_page import E2E_page
from config.config import BASE_URL


# --- Scenarios ---

@scenario("E2E.feature", "Happy path E2E")
def test_e2e_happy_path():
    pass

# --- Steps ---
@given("El usuario se enecuentra en la pagina liverpool")
def go_to_liverpool(driver):
    driver.get(BASE_URL)
    driver.refresh()


@when("El usuario hace click en categorias")
def click_on_categorias(driver):
    E2E_page(driver).click_on_category()


@then("El usuario hace hover en electronica")
def click_on_electronica(driver):
    E2E_page(driver).click_on_electronica()


@then("El usuario hace click en celulares")
def click_on_celulares(driver):
    E2E_page(driver).click_on_celulares()


@then("El usuario hace click en 128 gb checkbox")
def click_on_128gb(driver):
    E2E_page(driver).click_on_128gb_checkbox()


@then("El usuario selecciona el primer articulo")
def select_first_article(driver):
    E2E_page(driver).select_first_article()


@when("El usuario hace click en Agregar a mi bolsa")
def click_add_to_bag(driver):
    E2E_page(driver).click_add_to_bag()


@when("El usuario selecciona el carrito")
def click_on_cart(driver):
    E2E_page(driver).click_on_cart()


@then("el usuario debe ingresar a la cartpage")
def verify_cart_page(driver):
    assert E2E_page(driver).is_cart_page_displayed()



