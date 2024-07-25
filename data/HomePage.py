from BasePage import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.contact_link = (By.ID, "exampleModel")
        self.about_us_link = (By.LINK_TEXT, "About us")
        self.cart_link = (By.ID, "cartur")
        self.login_button = (By.ID, "login2")
        self.signup_button = (By.ID, "signin2")
        self.product_list = (By.CLASS_NAME, "hrefch")

    def open_contact(self):
        self.click_element(*self.contact_link)

    def open_about_us(self):
        self.click_element(*self.about_us_link)

    def open_cart(self):
        self.click_element(*self.cart_link)

    def open_login_form(self):
        self.click_element(*self.login_button)

    def open_signup_form(self):
        self.click_element(*self.signup_button)

    def select_first_product(self):
        self.find_element(*self.product_list).click()


