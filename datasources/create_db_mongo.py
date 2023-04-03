# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.maximize_window()


    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get(self.base_url + "chrome://newtab/")
        driver.get("https://console.dev.humalect.com/")

        time.sleep(2)
        elem = driver.find_element(By.NAME, "email")
        elem.clear()
        elem.send_keys("priyansh@humalect.com")
        elem2 = driver.find_element(By.NAME, "password")
        elem2.clear()
        elem2.send_keys("xxx")
        elem3 = driver.find_element(By.XPATH, '//button')
        elem3.click()    

        driver.find_element(By.XPATH, "//div[@id='__next']/section/aside/div[3]/ul/li[4]/span/div/a/span/span[2]").click()

        driver.get("https://console.dev.humalect.com/user/datasources")
        driver.find_element(By.XPATH, "//div[@id='__next']/section/section/main/div[2]/div/div/button").click()
        driver.find_element(By.NAME,"releaseName").click()
        
        driver.find_element(By.NAME,"releaseName").clear()
        driver.find_element(By.NAME,"releaseName").send_keys("abc")
      
        
        
        abc = driver.find_element(By.XPATH,"//form[@id='create-datasource-form']/div/div[2]/div/div/div/div/div[2]")
        # abc.send_keys(Keys.RETURN)
        # driver.find_element(By.XPATH, "//form[@id='create-datasource-form']/div/div[2]/div").click()
        # driver.find_element(By.ID,"react-select-3-option-1").click()
        # driver.find_element(By.ID,"react-select-2-listbox").click()
        # driver.find_element(By.XPATH, "//input[@value='63eb5b58df81ff73c5408ede']").click()
        
        
        # driver.find_element(By.ID,"react-select-2-option-0").click().send_keys(Keys.RETURN)
        
        # driver.find_element(By.XPATH,"//form[@id='create-datasource-form']/div[2]/div/div[2]/div/div/div/div/div[2]").click()
        # driver.find_element(By.ID,"react-select-4-option-1").click()
        # driver.find_element(By.XPATH,"//form[@id='create-datasource-form']/div[2]/div[2]/div/div/div/div/div[2]").click()
        # driver.find_element(By.ID,"react-select-5-option-0").click()
        # driver.find_element(By.XPATH,"//form[@id='create-datasource-form']/div[2]/div[3]/div/div/div/div/div[2]").click()
        # driver.find_element(By.ID,"react-select-6-option-0").click()


        driver.find_element(By.NAME,"customValuesData['persistence.existingClaim']").click()
        driver.find_element(By.NAME,"customValuesData['persistence.existingClaim']").clear()
        driver.find_element(By.NAME,"customValuesData['persistence.existingClaim']").send_keys("abc")
        driver.find_element(By.NAME,"customValuesData['auth.rootPassword']").click()
        driver.find_element(By.NAME,"customValuesData['auth.rootPassword']").clear()
        driver.find_element(By.NAME,"customValuesData['auth.rootPassword']").send_keys("password")
        # driver.find_element(By.XPATH,"//button[@type='submit']").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
