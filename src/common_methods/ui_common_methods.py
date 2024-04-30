import time
from selenium.webdriver.common.by import By
from src.driver_configuration import driver
from src.locators.locators import Locators
from test_data.data_container import DataContainer


class CommonMethods:

    def __init__(self):
        self.driver = driver
        self.locators_type = By
        self.locators = Locators()
        self.data = DataContainer()

    @staticmethod
    def decrease_implicitly_wait_for_func(func):

        def wrapper(*args, **kwargs):
            driver.implicitly_wait(1)
            result = func(*args, **kwargs)
            driver.implicitly_wait(10)
            return result if result is not None else None

        return wrapper

    def click_on_element_by_id(self, id_):
        element = self.get_element_by_id(id_)
        element.click()

    def input_text_by_id(self, text, id_):
        element = self.get_element_by_id(id_)
        element.send_keys(text)

    def get_element_by_id(self, id_):
        element = self.get_element_by_locator(self.locators_type.ID, id_)
        return element

    def get_element_by_locator(self, locator_type, locator, is_many=False):
        element = self.driver.find_elements(locator_type, locator) if is_many else self.driver.find_element(locator_type, locator)
        return element

    def go_to_url(self, url):
        self.driver.get(url)

    @staticmethod
    def waiter(seconds):
        time.sleep(seconds)
