from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
driver.maximize_window()
driver.find_element(By.NAME, 'q').send_keys("university grant commission")
time.sleep(5)
driver.quit()