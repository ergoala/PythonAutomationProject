import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException

logger = logging.getLogger(__name__)

class E2E_page:
    """
    Page Object para el flujo E2E de Liverpool.
    Contiene los métodos para interactuar con la página durante la compra.
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        # Localizadores de elementos
        self.categorys = (By.XPATH, "//span[@class='font-semibold']")
        self.electronica = (By.XPATH, "//span[@class='line-clamp-1 text-start'][text()='Electrónica']")
        self.celulares = (By.XPATH, "//span[@class='line-clamp-2'][text()='Celulares']")
        self.vermas = (By.XPATH, "//button[contains(@class, 'text-prim') and contains(text(), 'Ver más')]")
        self.checkbox = (By.XPATH, "//input[@value='128 GB']")
        self.first_article = (By.CSS_SELECTOR, "a.plp-card")
        self.add_to_bag = (By.CSS_SELECTOR, "button[data-testid='addToCarBtn']")
        self.cart_icon = (By.CSS_SELECTOR, "a[href='/tienda/cart']")
        self.cart_page = (By.CSS_SELECTOR, "div.cart-container, #mainContainer")



    def click_on_category(self):
        """Hace click en el botón de categorías para abrir el menú."""
        self.wait.until(EC.element_to_be_clickable(self.categorys)).click()

    def click_on_electronica(self):
        """Hace hover sobre la categoría Electrónica para desplegar el submenú."""
        element = self.wait.until(EC.visibility_of_element_located(self.electronica))
        ActionChains(self.driver).move_to_element(element).perform()

    def click_on_celulares(self):
        """Hace click en la opción Celulares dentro del submenú."""
        self.wait.until(EC.element_to_be_clickable(self.celulares)).click()

    def click_on_128gb_checkbox(self):
        """Selecciona el checkbox de almacenamiento 128 GB en los filtros."""
        try:
            logger.info("Iniciando búsqueda del checkbox 128 GB")

            # Intentar hacer click en "Ver más" si existe
            try:
                ver_mas = self.driver.find_element(*self.vermas)
                logger.info("Clic en el botón 'Ver más'")
                ver_mas.click()
            except NoSuchElementException:
                logger.warning("El botón 'Ver más' no existe o no es necesario")

            # Localizar el checkbox
            checkbox = self.wait.until(EC.presence_of_element_located(self.checkbox))
            logger.info("Checkbox 128 GB encontrado, realizando scroll")

            # Scroll hasta el checkbox
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
            logger.info("Scroll realizado hacia el checkbox 128 GB")

            # Verificar visibilidad y seleccionar
            try:
                self.wait.until(EC.visibility_of(checkbox))
            except TimeoutException:
                logger.warning("El checkbox no es visible en el primer intento, reintentando...")

            self.wait.until(EC.element_to_be_clickable(self.checkbox)).click()
            logger.info("Checkbox 128 GB seleccionado exitosamente")

        except TimeoutException as e:
            logger.error(f"Error al encontrar el checkbox de 128 GB: {e}")
            raise
        except Exception as e:
            logger.error(f"Error al seleccionar el checkbox de 128 GB: {e}")
            raise

    def select_first_article(self):
        """Hace click en el primer artículo de la lista de resultados."""
        self.wait.until(EC.element_to_be_clickable(self.first_article)).click()

    def click_add_to_bag(self):
        """Hace click en el botón 'Agregar a mi bolsa' en la página del producto."""
        self.wait.until(EC.element_to_be_clickable(self.add_to_bag)).click()

    def click_on_cart(self):
        """Hace click en el ícono del carrito para ir al carrito de compras."""
        self.wait.until(EC.element_to_be_clickable(self.cart_icon)).click()

    def is_cart_page_displayed(self):
        """Verifica si la página del carrito de compras está visible."""
        return self.wait.until(EC.visibility_of_element_located(self.cart_page)).is_displayed()


