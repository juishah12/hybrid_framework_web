import time

import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from utility import login_data

from base.webdriver_listener import WebDriverWrapper


class TestLiveDemo(WebDriverWrapper):

    @pytest.mark.parametrize('firstname,lastname,email,phone,company',
                          login_data.test_livedemo_data)
    def test_live_demo(self,firstname,lastname,email,phone,company):
     self.driver.find_element(By.XPATH, "//a[normalize-space()='Demo']").click()
     self.driver.implicitly_wait(20)
     self.driver.find_element(By.NAME,"firstname").send_keys(firstname)
     self.driver.find_element(By.NAME, "lastname").send_keys(lastname)
     self.driver.find_element(By.NAME, "email").send_keys(email)
     self.driver.find_element(By.XPATH, "//input[@name='phone']").send_keys(phone)
     self.driver.find_element(By.NAME,"company").send_keys(company)
     # self.driver.find_element(By.NAME,"job_role").click()
     # self.driver.find_element(By.NAME,"biggest_software_challenge").click()
     self.driver.find_element(By.XPATH,"//select[@name='job_role']/option[text()='QA Analyst']").click()
     select_challenge=Select(self.driver.find_element(By.NAME,"biggest_software_challenge"))
     select_challenge.select_by_value("Scalability")
     time.sleep(10)
     self.driver.find_element(By.XPATH,"//input[@value='Submit']").click()
     time.sleep(5)
     self.driver.quit()


