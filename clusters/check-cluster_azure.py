import unittest
import time
import random
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def humalect_login():
    driver = webdriver.Chrome()
    driver.get("https://console.dev.humalect.com/")
    time.sleep(2)

    try:
        elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        elem.send_keys("priyansh@humalect.com")

        elem2 = driver.find_element(By.NAME, "password")
        elem2.send_keys("xxxxxxx")
    # retry factory 
        elem3 = driver.find_element(By.XPATH, '//button').click()

        time.sleep(2)
        print("Login successful!!")
        time.sleep(2)

        try:
            cluster_click = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[text() = "Clusters"]'))
            )
            cluster_click.click()
            # ele4 = driver.find_element(By.XPATH, '//span[text() = "Clusters"]').click()

            # time.sleep(1)
            print("Clicked on Cluster Tab")
            time.sleep(2)
            
            cluster_name = "dev-azure-3"
            click_cluster = driver.find_element(By.XPATH, '//span[text() = "dev-azure-3"]').click()
            print("Clicked on 1 cluster")

            nodes_value = driver.find_elements(By.CLASS_NAME, 'flex.gap-x-1.items-center.text-sm.font-normal.max-w-max.bg-hm-accent-lightest-2.text-hm-accent.px-1.rounded-sm ')[0].text

            print(nodes_value)

            # vnet_value = driver.find_elements(By.XPATH, '//*[text()="dev-azure-3-net"]')

            # # xpath=//div[2]/div[4]/span
            # if(vnet_value):
            #     print("found")
            # else: 
            #     print("vnet not found")

            get_source = driver.page_source
            soup = BeautifulSoup(get_source, "html.parser")
            tag = soup.body
            pattern = re.compile(r"\b(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\.){3}(?:(?:2([0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9]))\b", re.IGNORECASE)
            
            for x in tag:
                print(x)
                # print("\n")
                # if(pattern.match(x)):
                #     print(pattern.match(x))
                # else:
                #     print("dns value not found")

            # print(dns_value)

            time.sleep(3)

        finally:
            driver.quit()

    finally:
            driver.quit()

    # elem = driver.find_element(By.NAME, "email")
    
    

humalect_login()

# /[subnet-].



# PR - clsuter creating and desc check, wait for 15 min, 1 min check 
