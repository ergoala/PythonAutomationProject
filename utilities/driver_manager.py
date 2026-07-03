from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config.config import IMPLICIT_WAIT, PAGE_LOAD_TIMEOUT


class DriverManager:
    def __init__(self):
        self.driver = None

    def create_driver(self, headless=False):
        chrome_options = Options()

        if headless:
            chrome_options.add_argument("--headless=new")

        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

        self.driver.implicitly_wait(IMPLICIT_WAIT)
        self.driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
        self.driver.set_script_timeout(PAGE_LOAD_TIMEOUT)

        return self.driver

    def quit_driver(self):
        if self.driver:
            try:
                self.driver.quit()
            except Exception:
                pass
