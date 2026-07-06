import pytest
import allure
from utilities.driver_manager import DriverManager


@pytest.fixture(scope="function")
def driver(request):
    driver_manager = DriverManager()
    driver = driver_manager.create_driver(headless=False)

    # Limpiar cache del navegador
    try:
        driver.delete_all_cookies()
    except Exception:
        pass
    try:
        driver.execute_script("window.localStorage.clear();")
        driver.execute_script("window.sessionStorage.clear();")
    except Exception:
        pass

    yield driver

    # Tomar screenshot si el test falló
    if request.node.rep_call and request.node.rep_call.failed:
        try:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(screenshot, name="Screenshot al fallar", attachment_type=allure.attachment_type.PNG)
        except Exception:
            pass

    try:
        driver_manager.quit_driver()
    except Exception:
        pass


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    import pytest
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
