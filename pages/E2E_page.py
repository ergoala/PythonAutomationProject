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
        """
        Inicializa el Page Object con el driver de Selenium.
        
        Args:
            driver: Instancia del webdriver de Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        # Localizadores de elementos
        self.categorys = (By.XPATH, "//span[@class='font-semibold']")
        self.electronica = (By.XPATH, "//nav//span[contains(@class,'line-clamp') and text()='Electrónica']")
        self.celulares = (By.XPATH, "//span[@class='line-clamp-2'][text()='Celulares']")
        self.vermas = (By.XPATH, "//button[contains(@data-testid,'filter-attributes') and .//span[normalize-space()='Ver más']]")
        self.memoria_ram_section = (By.XPATH, "//*[contains(text(), 'Memoria RAM') or contains(text(), 'Memoria Ram')]")
        self.checkbox = (By.XPATH, "//label[contains(., '128 GB')] | //span[contains(., '128 GB')]")
        self.first_article = (By.XPATH, "//h4[@class='text-body-base text-carbon-500 font-bold line-clamp-2']")
        self.add_to_bag = (By.XPATH, "//button[@data-testid='add-to-bag-button']")
        self.no_thanks_btn = (By.XPATH, "//button[contains(., 'No, gracias')]")
        self.add_protection_btn = (By.XPATH, "//button[contains(., 'Agregar protección')]")
        self.cart_icon = (By.XPATH, "//a[@aria-label='shopping cart']")
        self.cart_page = (By.CSS_SELECTOR, "div.cart-container, #mainContainer")
        self.cart_item = (By.CSS_SELECTOR, "[data-testid*='cart-item'], [data-testid*='product-card'], div[class*='cart'] article, div[class*='cart'] [class*='product']")



    def click_on_category(self):
        """
        Hace click en el botón de categorías para abrir el menú principal.
        
        Flujo:
            1. Espera a que el botón de categorías sea clickeable
            2. Realiza click para desplegar el menú de categorías
        """
        self.wait.until(EC.element_to_be_clickable(self.categorys)).click()

    def click_on_electronica(self):
        """
        Realiza hover sobre la categoría Electrónica para desplegar el submenú.
        
        Flujo:
            1. Espera a que el elemento "Electrónica" sea visible
            2. Usa ActionChains para hacer hover sobre el elemento
            3. Esto despliega el submenú de subcategorías de electrónica
        
        Nota:
            Se usa hover en lugar de click porque Liverpool despliega
            el menú al pasar el mouse, no al hacer click.
        """
        element = self.wait.until(EC.visibility_of_element_located(self.electronica))
        ActionChains(self.driver).move_to_element(element).perform()

    def click_on_celulares(self):
        """
        Hace click en la opción Celulares dentro del submenú de Electrónica.
        
        Flujo:
            1. Espera a que "Celulares" sea clickeable
            2. Realiza click para navegar a la página de celulares
        """
        self.wait.until(EC.element_to_be_clickable(self.celulares)).click()

    def click_on_128gb_checkbox(self):
        """
        Selecciona el checkbox de almacenamiento 128 GB en los filtros.
        
        Flujo:
            1. Localiza el panel de filtros (sidebar izquierdo)
            2. Busca la sección de Memoria RAM
            3. Hace scroll hasta Memoria RAM
            4. Hace click en "Ver más" si es necesario
            5. Selecciona el checkbox de 128 GB
        
        Raises:
            TimeoutException: Si no se encuentra el checkbox en el tiempo límite
            Exception: Si ocurre otro error durante la selección
        
        Nota:
            El panel de filtros es sticky (se queda fijo al hacer scroll).
            El checkbox puede no ser visible hasta hacer scroll.
        """
        try:
            logger.info("Iniciando búsqueda del checkbox 128 GB")

            # Localizar el panel de filtros
            filter_panel = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "section[class*='xl:sticky'][class*='xl:overflow-y-auto']")
                )
            )
            logger.info("Panel de filtros encontrado")

            # Buscar la sección de Memoria RAM
            memoria_ram = self.wait.until(
                EC.presence_of_element_located(self.memoria_ram_section)
            )
            logger.info("Sección Memoria RAM encontrada, realizando scroll")

            # Hacer scroll hasta la sección de Memoria RAM
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'start'});", memoria_ram
            )
            logger.info("Scroll realizado hasta la sección Memoria RAM")

            # Esperar un momento para que el contenido se renderice
            self.wait.until(EC.visibility_of(memoria_ram))

            # Hacer click en la opcion Ver mas
            self.wait.until(EC.presence_of_element_located(self.vermas)).click()

            # Hacer click en el checkbox
            self.wait.until(EC.element_to_be_clickable(self.checkbox)).click()
            logger.info("Checkbox 128 GB seleccionado exitosamente")

        except TimeoutException as e:
            logger.error(f"Error al encontrar el checkbox de 128 GB: {e}")
            raise
        except Exception as e:
            logger.error(f"Error al seleccionar el checkbox de 128 GB: {e}")
            raise


    def select_first_article(self):
        """
        Hace click en el primer artículo de la lista de resultados.
        
        Flujo:
            1. Espera a que el primer artículo sea clickeable
            2. Realiza click para ir a la página del producto
        """
        self.wait.until(EC.element_to_be_clickable(self.first_article)).click()

    def click_add_to_bag(self):
        """
        Hace click en el botón 'Agregar a mi bolsa' en la página del producto.
        
        Flujo:
            1. Espera a que la página del producto (PDP) esté cargada
            2. Localiza el botón "Agregar a mi bolsa" por data-testid
            3. Hace scroll hasta el botón
            4. Espera a que sea clickeable
            5. Realiza click para agregar el producto al carrito
            6. Cierra el popup de "Liverpool Care" si aparece
        """
        # Esperar a que el botón aparezca en la página del producto
        self.wait.until(EC.presence_of_element_located(self.add_to_bag))
        
        # Hacer scroll hasta el botón
        button = self.driver.find_element(*self.add_to_bag)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        
        # Esperar a que sea clickeable y hacer click
        self.wait.until(EC.element_to_be_clickable(self.add_to_bag)).click()
        
        # Cerrar popup de Liverpool Care si aparece
        try:
            self.wait.until(EC.element_to_be_clickable(self.add_protection_btn)).click()
            logger.info("Protección agregada exitosamente")
        except TimeoutException:
            logger.info("No apareció popup de Liverpool Care")

    def click_on_cart(self):
        """
        Hace click en el ícono del carrito para ir al carrito de compras.
        
        Flujo:
            1. Espera a que el ícono del carrito sea clickeable
            2. Realiza click para navegar a la página del carrito
        """
        self.wait.until(EC.element_to_be_clickable(self.cart_icon)).click()

    def is_cart_page_displayed(self):
        """
        Verifica si la página del carrito tiene al menos un artículo.
        
        Returns:
            bool: True si hay al menos un artículo en el carrito, False en caso contrario
        
        Flujo:
            1. Espera a que el contenedor del carrito sea visible
            2. Busca todos los elementos de artículos en el carrito
            3. Retorna True si encuentra al menos uno
        
        Nota:
            Este método valida la presencia de productos, no solo
            la carga de la página del carrito.
        """
        try:
            self.wait.until(EC.visibility_of_element_located(self.cart_page))
            cart_items = self.driver.find_elements(*self.cart_item)
            return len(cart_items) > 0
        except (TimeoutException, NoSuchElementException):
            return False


