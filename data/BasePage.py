from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def navigate_to(self,url):
        self.driver.get(url)

    def wait_for_element(self, by_type, locator):
        return self.wait.until(EC.presence_of_element_located((by_type, locator)))

    def find_element(self, by_type, locator):
        return self.driver.find_element(by_type, locator)

    def click_element(self, by_type, locator):
        element = self.find_element(by_type, locator)
        element.click()

    def send_keys(self, by_type, locator, keys):
        element = self.find_element(by_type, locator)
        element.send_keys(keys)