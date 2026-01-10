from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_invalid_login_shows_error():
    driver = get_driver()
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("Admin", "wrong_password")

    # OrangeHRM shows an "Invalid credentials" message
    wait = WebDriverWait(driver, 10)
    error = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(@class,'alert-content-text')]")))

    assert "Invalid credentials" in error.text
    driver.quit()
