import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def humalect_login():
    driver = webdriver.Chrome()
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

    time.sleep(2)
    
    ele4 = driver.find_element(By.XPATH, '//span[text() = "Clusters"]')
    ele4.click()
    time.sleep(1)
    ele5 = driver.find_element(By.XPATH, '//button[text() = "Create New Cluster"]')
    ele5.click()
    time.sleep(1)
    
    cluster_name = driver.find_element(By.NAME, "cluster")
    cluster_name.clear()
    cluster_name.send_keys("priyansh" + str(random.randint(0,9000)) + "selenium-test-cluster" + str(random.randint(0,9000)))
    
    domain_name = driver.find_element(By.NAME, "domains.0.name")
    domain_name.clear()
    domain_name.send_keys("test.humalect.com")
    
    instance = driver.find_element(By.XPATH, '//span[text() = "T3a medium"]')
    instance.click()
    time.sleep(1)
    
    create_cluster = driver.find_element(By.XPATH, '//button[text() = "Create Cluster"]')
    # create_cluster.click()
    time.sleep(5)
# humalect_login()

def cluster():
    driver = webdriver.Chrome()
    # ele1 = driver.find_element_by_xpath("//span[contains(@class,'Trsdu')]")
    # ele1= driver.find_element_by_xpath("//*[contains(text(), 'Cluters')]") 
    ele4 = driver.find_element_by_xpath('//span[text() = "Cluster"]')

    ele1.click()
    time.sleep(20)
    
humalect_login()
# cluster()