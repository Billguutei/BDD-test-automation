from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

@When('login to ims')
def step(self):
		driver = self.driver
		driver.get("https://192.168.7.64:9001")
		WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.NAME, 'username')))
		driver.find_element(By.NAME, "username").send_keys("15974")
		driver.find_element(By.NAME, "password").send_keys("kb2020*")
		WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn")))
		driver.find_element(By.CSS_SELECTOR, ".btn").click()
		time.sleep(1000)