import time

import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from utility import login_data

from base.webdriver_listener import WebDriverWrapper
class Test_trial(WebDriverWrapper):

    @pytest.mark.parametrize('firstname,lastname,email,phone,company,checkbox',
                          login_data.test_trial_data)
    def test_trial(self,firstname,lastname,email,phone,company,checkbox):
     self.driver.find_element(By.XPATH, "//a[normalize-space()='Free Trial']").click()
     self.driver.implicitly_wait(20)
     self.driver.find_element(By.NAME,"firstname").send_keys(firstname)
     self.driver.find_element(By.NAME, "lastname").send_keys(lastname)
     self.driver.find_element(By.NAME, "email").send_keys(email)
     self.driver.find_element(By.XPATH, "//input[@name='phone']").send_keys(phone)
     self.driver.find_element(By.NAME,"company").send_keys(company)
     self.driver.find_element(By.XPATH, "//select[@name='job_role']/option[text()='QA Manager / Lead']").click()
     select_challenge = Select(self.driver.find_element(By.NAME, "total_size_of_test_suite"))
     select_challenge.select_by_value("0-500")
     select_project = Select(self.driver.find_element(By.NAME,"any_upcoming_projects_that_require_test_automation_"))
     select_project.select_by_value("Upgrades")
     time.sleep(5)
     checkboxdata=self.driver.find_element(By.XPATH,"//span[normalize-space()='Modernizing Test Automation with AI']").text
     assertvalue=assert_that(checkboxdata).contains(checkbox)
     if assertvalue == 'Modernizing Test Automation with AI':
         self.driver.find_element(By.NAME,"i_m_interested_in_learning_more_about").click()
     else:
         self.driver.find_element(By.XPATH,"//input[@value='Moving from Manual Testing to Test Automation with AI']").click()
     time.sleep(5)
     self.driver.find_element(By.NAME,"terms_and_conditions").click()
     self.driver.find_element(By.XPATH,"//input[@name='hs_context']").click()
     time.sleep(3)
     self.driver.quit()
