import os
from datetime import datetime
from config.config import SCREENSHOTS_DIR


class ScreenshotManager:
    def __init__(self):
        if not os.path.exists(SCREENSHOTS_DIR):
            os.makedirs(SCREENSHOTS_DIR)

    def take_screenshot(self, driver, test_name):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{test_name}_{timestamp}.png"
        filepath = os.path.join(SCREENSHOTS_DIR, filename)

        driver.save_screenshot(filepath)
        return filepath
