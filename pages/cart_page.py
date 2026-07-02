from selenium.webdriver.common.by import By
from utilities.logger import Logger


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger()

        self.page_title = (By.CLASS_NAME, "title")
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.cart_item_name = (By.CLASS_NAME, "inventory_item_name")
        self.cart_item_price = (By.CLASS_NAME, "inventory_item_price")
        self.remove_buttons = (By.CSS_SELECTOR, "button[data-test^='remove']")
        self.checkout_button = (By.ID, "checkout")
        self.continue_shopping_button = (By.ID, "continue-shopping")

    def get_page_title(self):
        return self.driver.find_element(*self.page_title).text

    def get_cart_items(self):
        return self.driver.find_elements(*self.cart_items)

    def get_cart_item_count(self):
        return len(self.get_cart_items())

    def get_item_names(self):
        elements = self.driver.find_elements(*self.cart_item_name)
        return [element.text for element in elements]

    def get_item_prices(self):
        elements = self.driver.find_elements(*self.cart_item_price)
        return [element.text for element in elements]

    def remove_item(self, item_index):
        buttons = self.driver.find_elements(*self.remove_buttons)
        buttons[item_index].click()
        self.logger.info(f"Item {item_index} eliminado del carrito")

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
        self.logger.info("Botón checkout clickeado")

    def click_continue_shopping(self):
        self.driver.find_element(*self.continue_shopping_button).click()
        self.logger.info("Botón continue shopping clickeado")
