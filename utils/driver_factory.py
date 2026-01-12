from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver(headless: bool = False):
    options = Options()

    # always safe for CI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    if headless:
        options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    return driver
