import os

# Base URL del eCommerce de pruebas
BASE_URL = "https://www.saucedemo.com"

# Tiempos de espera (en segundos)
IMPLICIT_WAIT = 10
PAGE_LOAD_TIMEOUT = 20

# Credenciales de prueba
USERNAME_STANDARD = "standard_user"
PASSWORD = "secret_sauce"

# Rutas de carpetas
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOTS_DIR = os.path.join(ROOT_DIR, "screenshots")
REPORTS_DIR = os.path.join(ROOT_DIR, "reports")
TESTDATA_DIR = os.path.join(ROOT_DIR, "testdata")
