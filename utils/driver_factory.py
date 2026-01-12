import os
import platform
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def get_driver(headless: bool = False):
    options = Options()

    # CI-safe flags
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    if headless:
        options.add_argument("--headless=new")

    system = platform.system().lower()

    # On GitHub Actions Ubuntu, we install APT Chromium:
    # - chromium binary: /usr/bin/chromium
    # - chromedriver: /usr/bin/chromedriver
    if system == "linux":
        chrome_bin = shutil.which("chromium") or "/usr/bin/chromium"
        driver_bin = shutil.which("chromedriver") or "/usr/bin/chromedriver"
        options.binary_location = chrome_bin
        service = Service(driver_bin)
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    # On Windows/macOS (your local machine), Selenium Manager will handle driver
    driver = webdriver.Chrome(options=options)
    return driver
