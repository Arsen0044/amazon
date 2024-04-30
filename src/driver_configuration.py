from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class DriverConfiguration:

    @staticmethod
    def create_driver():
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver


a = DriverConfiguration()
driver = a.create_driver()
