import time

import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utility import login_data

from base.webdriver_listener import WebDriverWrapper


class TestLogin(WebDriverWrapper):
    # def test_valid_login(self):
    #     self.driver.find_element(By.NAME, "username").send_keys("Admin")
    #     self.driver.find_element(By.NAME, "password").send_keys("admin123")
    #     self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    #     actual_text = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
    #     assert_that("Dashboard").is_equal_to(actual_text)

    @pytest.mark.parametrize('username, password, expected_error',login_data.test_invalid_login_data)
    def test_invalid_login(self,username,password,expected_error):
        self.driver.find_element(By.XPATH,"//a[normalize-space()='LOG In']").click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.NAME,"email").send_keys(username)
        self.driver.find_element(By.NAME,"password").send_keys(password)
        time.sleep(10)
        self.driver.find_element(By.XPATH,"//div[@class='form']//button[@type='button']").click()
        # ele = self.driver.find_element(By.XPATH,"//button[@type='button]")
        # self.driver.execute_script(ele.click())
        time.sleep(10)
        actual_error = self.driver.find_element(By.XPATH, "//div[@class='error failure']//p").text
        assert_that(expected_error).is_equal_to(actual_error)

