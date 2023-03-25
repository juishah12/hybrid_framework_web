import time

import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utility import login_data

from base.webdriver_listener import WebDriverWrapper


class TestLogin(WebDriverWrapper):

    @pytest.mark.parametrize('username, password, expected_error',
                             login_data.test_blank_login_data)
    def test_blank_login(self,username,password,expected_error):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='LOG In']").click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.NAME,"email").send_keys(username)
        self.driver.find_element(By.NAME,"password").send_keys(password)
        #self.driver.find_element(By.XPATH, "//div[@class='form']//button[@type='button']").click()
        time.sleep(10)
        actual_text = self.driver.find_element(By.XPATH,"//div[@role='alert']//div[contains(@class,'v-messages__wrapper')]//div[normalize-space()='This field is required.']").text
        assert_that(expected_error).is_equal_to(actual_text)

    @pytest.mark.parametrize('username, password, expected_error',
                             login_data.test_invalid_login_data)
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

    def test_forget_password(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='LOG In']").click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH,"//a[text()=' Forgot Password?']").click()
        self.driver.find_element(By.XPATH,"//input[@placeholder='Enter your email']").send_keys('neha@rapcaps.com')
        self.driver.find_element(By.XPATH, "//div[@class='form']//button[@type='button']").click()
        time.sleep(10)
        actual_text = self.driver.find_element(By.XPATH,"//p[contains(@class,'fs-14')]").text
        assert_that('A password reset link has been sent to your email if it exists in our system. Please contact your sales or support representative '
                    'in case you are still having problems signing in.').is_equal_to(actual_text)
