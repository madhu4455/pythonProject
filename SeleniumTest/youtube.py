from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.orangehrm.com')
driver.maximize_window()

driver.find_element(By.CLASS_NAME, 'btn btn-ohrm btn-contact-sales').click()
driver.find_element(By.NAME, 'FullName').send_keys("Madhu Sudhan Reddy Tadigotla")
driver.find_element(By.NAME, 'Email').send_keys('madhu4455@gmail.com')
driver.find_elements(By.xpath("//select")).click()
time.sleep(10)
driver.quit





