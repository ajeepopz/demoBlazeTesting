import unittest
from selenium import webdriver
from HomePage import HomePage
from bugLogger import bugLogger

class TestHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.home_page = HomePage(self.driver)
        self.bug_logger = bugLogger

    def test_open_contact(self):
        self.home_page.navigate_to("https://www.demoblaze.com/.")
        try:
            self.home_page.open_contact()
        except Exception as e:
            self.bug_logger.log_bug(f"contact form not opening: {str(e)}")


    def test_open_about_us(self):
        self.home_page.navigate_to("https://www.demoblaze.com/.")
        try:
            self.home_page.open_about_us()
        except Exception as e:
            self.bug_logger.log_bug(f"About us section not opening: {str(e)}")

    def test_open_cart(self):
        self.home_page.navigate_to("https://www.demoblaze.com/.")
        try:
            self.home_page.open_cart()
        except Exception as e:
            self.bug_logger.log_bug(f"cart page not opening: {str(e)}")

    def test_open_login_form(self):
        self.home_page.navigate_to("https://www.demoblaze.com/.")
        try:
            self.home_page.open_login_form()
        except Exception as e:
            self.bug_logger.log_bug(f"login form form not opening: {str(e)}")

    def test_open_signup_form(self):
        self.home_page.navigate_to("https://www.demoblaze.com/.")
        try:
            self.home_page.open_signup_form()
        except Exception as e:
            self.bug_logger.log_bug(f"signup form not opening: {str(e)}")

    def test_select_first_product(self):
        self.home_page.navigate_to("https://www.demoblaze.com/.")
        try:
            self.home_page.select_first_product()
        except Exception as e:
            self.bug_logger.log_bug(f"product details page not opening: {str(e)}")

    def tearDown(self):
        self.bug_logger.save_to_file()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()