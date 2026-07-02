from selenium.webdriver.common.by import By
from utilities.logger import Logger


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger()

        self.page_title = (By.CLASS_NAME, "title")
        self.inventory_items = (By.CLASS_NAME, "inventory_item")
        self.inventory_item_name = (By.CLASS_NAME, "inventory_item_name")
        self.inventory_item_price = (By.CLASS_NAME, "inventory_item_price")
        self.add_to_cart_buttons = (By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
        self.shopping_cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.shopping_cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.burger_menu = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")

    def get_page_title(self):
        return self.driver.find_element(*self.page_title).text

    def get_all_items(self):
        return self.driver.find_elements(*self.inventory_items)

    def get_all_item_names(self):
        elements = self.driver.find_elements(*self.inventory_item_name)
        return [element.text for element in elements]

    def get_all_item_prices(self):
        elements = self.driver.find_elements(*self.inventory_item_price)
        return [element.text for element in elements]

    def add_item_to_cart(self, item_index):
        buttons = self.driver.find_elements(*self.add_to_cart_buttons)
        buttons[item_index].click()
        self.logger.info(f"Item {item_index} agregado al carrito")

    def get_cart_count(self):
        try:
            badge = self.driver.find_element(*self.shopping_cart_badge)
            return int(badge.text)
        except:
            return 0

    def click_cart(self):
        self.driver.find_element(*self.shopping_cart_link).click()
        self.logger.info("Carrito clickeado")

    def logout(self):
        self.driver.find_element(*self.burger_menu).click()
        self.driver.find_element(*self.logout_link).click()
        self.logger.info("Logout realizado")
