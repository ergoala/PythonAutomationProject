from selenium.webdriver.common.by import By
from utilities.logger import Logger


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger()

        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.logger.info(f"Usuario ingresado: {username}")

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)
        self.logger.info("Contraseña ingresada")

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        self.logger.info("Botón de login clickeado")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text

    def is_error_displayed(self):
        try:
            return self.driver.find_element(*self.error_message).is_displayed()
        except:
            return False
