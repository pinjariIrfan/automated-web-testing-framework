"""
Utility functions for the automation framework
"""
import time

def take_screenshot(driver, filename):
    driver.save_screenshot(f"screenshots/{filename}.png")

def wait_for_element(driver, locator, timeout=10):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))