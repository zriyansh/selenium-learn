
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

        try:
            cluster_click = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[text() = "Projects"]'))
            )
            cluster_click.click()

            print("Clicked on Projects Tab")
            time.sleep(2)
            
            create_db_btn  = driver.find_element(By.XPATH, '//button[text() = "Create New Project"]')
            create_db_btn.click()
            time.sleep(1)

            print("Clicked on Create New Project button")
            time.sleep(2)

            # driver.find_element(By.XPATH,"//div[@id='__next']/section/aside/div[3]/ul/li[6]/span/div/a/span/span[2]").click()
            # time.sleep(2)
            # driver.find_element(By.XPATH,"//div[@id='__next']/section/section/main/div[2]/div/div/button").click()
            driver.find_element(By.NAME,"name").click()
            driver.find_element(By.NAME,"name").clear()
            driver.find_element(By.NAME,"name").send_keys("priyansh-test-1")
            time.sleep(1)
            driver.find_element(By.NAME,"description").click()
            driver.find_element(By.NAME,"description").clear()
            driver.find_element(By.NAME,"description").send_keys("abcd")
            time.sleep(1)
            abc = driver.find_element(By.XPATH,"//div[@id='__next']/section/section/main/div[2]/div/div[2]/form/div[4]/div/div/div").click()
            # abc = driver.find_element(By.ID,"react-select-11-option-0")
            # abc.click()
            # abc.send_keys(Keys.RETURN)
            time.sleep(1)
            driver.find_element(By.XPATH,"//div[@id='__next']/section/section/main/div[2]/div/div[2]/form/div[5]/div/div/div/div[2]").click()
            driver.find_element(By.ID,"react-select-12-option-0-0").click()
            time.sleep(1)
            driver.find_element(By.XPATH,"//div[@id='__next']/section/section/main/div[2]/div/div[2]/form/div[6]").click()
            driver.find_element(By.XPATH,"//div[@id='__next']/section/section/main/div[2]/div/div[2]/form/div[6]/div/div/div/div[2]").click()
            driver.find_element(By.ID,"react-select-13-option-0").click()
            driver.find_element(By.XPATH,"//button[@type='submit']").click()
        
        finally:
            driver.quit()
    
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
