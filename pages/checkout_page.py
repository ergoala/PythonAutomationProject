from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

        # Paso 1: Información del cliente
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

        # Paso 2: Resumen del pedido
        self.page_title = (By.CLASS_NAME, "title")
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.subtotal_label = (By.CLASS_NAME, "summary_subtotal_label")
        self.tax_label = (By.CLASS_NAME, "summary_tax_label")
        self.total_label = (By.CLASS_NAME, "summary_total_label")
        self.finish_button = (By.ID, "finish")

        # Paso 3: Confirmación
        self.complete_header = (By.CLASS_NAME, "complete-header")
        self.back_home_button = (By.ID, "back-to-products")

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue()

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def get_subtotal(self):
        text = self.driver.find_element(*self.subtotal_label).text
        return text.split(":")[1].strip()

    def get_tax(self):
        text = self.driver.find_element(*self.tax_label).text
        return text.split(":")[1].strip()

    def get_total(self):
        text = self.driver.find_element(*self.total_label).text
        return text.split(":")[1].strip()

    def click_finish(self):
        self.driver.find_element(*self.finish_button).click()

    def get_complete_message(self):
        return self.driver.find_element(*self.complete_header).text

    def click_back_home(self):
        self.driver.find_element(*self.back_home_button).click()
