import pytest
from utilities.driver_manager import DriverManager


@pytest.fixture(scope="function")
def driver(request):
    driver_manager = DriverManager()
    driver = driver_manager.create_driver(headless=False)

    yield driver

    driver_manager.quit_driver()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    import pytest
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
