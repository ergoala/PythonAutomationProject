import pytest
from utilities.driver_manager import DriverManager
from utilities.screenshot_manager import ScreenshotManager
from utilities.logger import Logger


@pytest.fixture(scope="function")
def driver(request):
    logger = Logger()
    screenshot_manager = ScreenshotManager()
    driver_manager = DriverManager()

    driver = driver_manager.create_driver(headless=False)

    test_name = request.node.name
    logger.info(f"Iniciando test: {test_name}")

    yield driver

    if request.node.rep_call and request.node.rep_call.failed:
        logger.error(f"Test FALLÓ: {test_name}")
        screenshot_manager.take_screenshot(driver, test_name)
        logger.info(f"Screenshot guardado para: {test_name}")
    else:
        logger.info(f"Test FINALIZÓ: {test_name}")

    driver_manager.quit_driver()
    logger.info(f"Navegador cerrado para: {test_name}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    import pytest
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
