import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class WebDriverWrapper:
    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def browser_config(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.functionize.com/")
        yield
        self.driver.quit()