
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome
driver.implicitly_wait(10)
driver.get('https://app.hubspot.com')

driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, '#username').send_keys("madhu4455@gmail.com")
driver.find_element(By.CSS_SELECTOR, 'login-password').send_keys("<admin@1234>")




