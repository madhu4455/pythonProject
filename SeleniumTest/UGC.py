from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.ugc.gov.in/')
driver.maximize_window()

driver.find_element(By.xpath("//a[contains(text(),'Guidelines']")).click();

time.sleep(10)
driver.quit
