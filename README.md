# Automation Framework - eCommerce Testing

Framework de automatización de pruebas end-to-end para eCommerce utilizando Python, Selenium y Pytest con enfoque BDD (Behavior Driven Development).

## Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| Python | 3.14 | Lenguaje de programación |
| Selenium | 4.45.0 | Automatización de navegador |
| Pytest | 9.1.1 | Framework de pruebas |
| pytest-bdd | 8.1.0 | Soporte BDD (Gherkin) |
| webdriver-manager | 4.1.2 | Gestión automática de drivers |
| pytest-html | 4.2.0 | Generación de reportes HTML |

## Estructura del Proyecto

```
AutomationFramework/
│
├── features/                    # Archivos feature (Gherkin)
│   ├── login.feature           # Escenarios de login
│   ├── inventory.feature       # Escenarios de inventario
│   └── checkout.feature        # Escenarios de checkout
│
├── pages/                       # Page Object Model
│   ├── login_page.py           # Page Object: Login
│   ├── inventory_page.py       # Page Object: Inventario
│   ├── cart_page.py            # Page Object: Carrito
│   └── checkout_page.py        # Page Object: Checkout
│
├── tests/                       # Casos de prueba
│   ├── test_login.py           # Tests tradicionales de login
│   ├── test_inventory.py       # Tests tradicionales de inventario
│   ├── test_checkout.py        # Tests tradicionales de checkout
│   ├── test_bdd_login.py       # Tests BDD de login
│   ├── test_bdd_inventory.py   # Tests BDD de inventario
│   └── test_bdd_checkout.py    # Tests BDD de checkout
│
├── utilities/                   # Utilidades
│   ├── driver_manager.py       # Gestión del WebDriver
│   ├── screenshot_manager.py   # Captura de screenshots
│   └── logger.py               # Sistema de logging
│
├── config/                      # Configuración
│   └── config.py               # Variables centralizadas
│
├── testdata/                    # Datos de prueba
│   └── users.json              # Credenciales de usuarios
│
├── reports/                     # Reportes HTML generados
├── screenshots/                 # Capturas en caso de fallo
├── logs/                        # Logs de ejecución
│
├── conftest.py                  # Fixtures de Pytest
├── pytest.ini                   # Configuración de Pytest
└── requirements.txt             # Dependencias del proyecto
```

## Características

- **Page Object Model (POM)**: Separación de la lógica de UI y negocio
- **BDD con Gherkin**: Tests legibles para todo el equipo
- **Captura automática de screenshots**: Cuando un test falla
- **Logging detallado**: Historial de ejecución
- **Reportes HTML**: Resultados visuales de las pruebas
- **Configuración centralizada**: URLs, credenciales y tiempos de espera
- **Gestión automática de drivers**: No es necesario descargar ChromeDriver

## Sitio de Pruebas

Este framework está configurado para automatizar [SauceDemo](https://www.saucedemo.com), un eCommerce de pruebas con las siguientes funcionalidades:

- Login con múltiples tipos de usuario
- Listado de productos
- Agregar/eliminar productos del carrito
- Proceso de checkout completo

## Instalación

### Prerrequisitos

- Python 3.10 o superior
- pip
- Google Chrome (o cualquier navegador Chromium)

### Pasos

1. Clonar el repositorio:
```bash
git clone https://github.com/ergoala/PythonAutomationProject.git
cd PythonAutomationProject/AutomationFramework
```

2. Crear entorno virtual:
```bash
python -m venv venv
```

3. Activar entorno virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución de Tests

### Todos los tests
```bash
pytest
```

### Tests de un archivo específico
```bash
pytest tests/test_login.py
```

### Tests BDD
```bash
pytest tests/test_bdd_login.py
```

### Por tags (smoke, regression)
```bash
pytest -m smoke
pytest -m regression
```

### Con reporte HTML
```bash
pytest --html=reports/report.html
```

### Modo verbose
```bash
pytest -v
```

## Tipos de Tests

### Tests Tradicionales
Archivos en `tests/test_*.py` que utilizan Page Objects directamente.

### Tests BDD
Archivos en `tests/test_bdd_*.py` que utilizan:
- **Feature files** (`features/*.feature`): Escenarios en Gherkin
- **Step definitions**: Implementación de los pasos en Python

## Etiquetas Disponibles

| Tag | Descripción |
|-----|-------------|
| `@smoke` | Tests rápidos de verificación básica |
| `@regression` | Suite completa de regresión |
| `@login` | Tests relacionados con login |
| `@inventory` | Tests de inventario |
| `@checkout` | Tests de checkout |

## Ejemplo de Feature (Gherkin)

```gherkin
Feature: Login
  As a user
  I want to log in to the application
  So that I can access the products

  @smoke @login
  Scenario: Successful login
    Given the user is on the login page
    When the user enters valid credentials
    Then the user should see the products page
```

## Contribuir

1. Crear una rama para la feature (`git checkout -b feature/nueva-funcionalidad`)
2. Hacer commit de los cambios (`git commit -m 'Add new feature'`)
3. Push a la rama (`git push origin feature/nueva-funcionalidad`)
4. Crear un Pull Request

## Licencia

Proyecto de uso educativo y profesional.
