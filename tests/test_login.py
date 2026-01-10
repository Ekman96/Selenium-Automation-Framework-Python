from utils.driver_factory import get_driver
from pages.login_page import LoginPage

def test_valid_login():
    driver = get_driver()
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("Admin", "admin123")

    assert login_page.is_dashboard_visible(), "Dashboard not visible - login failed"
    driver.quit()
