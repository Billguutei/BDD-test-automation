# -*- coding: UTF-8 -*
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from modules.constants import *
import time
import datetime
from selenium.webdriver.common.action_chains import ActionChains
import os
import datetime

date_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
date_time_access = datetime.datetime.now().strftime("%m/%d/%Y")
consts = Constant()


def download_wait(path_to_downloads):
	seconds = 0
	dl_wait = True
	while dl_wait and seconds < 20:
		time.sleep(1)
		dl_wait = False
		for fname in os.listdir(path_to_downloads):
			if fname.endswith('.crdownload'):
				dl_wait = True
		seconds += 1
	return seconds


class Tools:
	
	def load_page_url(self, *args):
		
		driver = self.driver
		for window_name in args:
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.LINK_TEXT, u"{}".format(window_name))))
			driver.find_element_by_link_text(u"{}".format(window_name)).click()

class LoginsClass:
	
	def login(self):
		driver = self.driver
		driver.get(consts.URLS["IMS_URL"])
		Tools.load_page_url(self, 'Request a certificate', 'advanced certificate request')
		os.chdir('./reports/certs/')
		with open('server.csr','r') as file:
			servercsr = file.read()
			file.close()
		csrFile = servercsr
		driver.find_element_by_id("locTaRequest").send_keys(csrFile)
		driver.find_element_by_id("lbCertTemplateID").click()
		ActionChains(driver).send_keys("KHANBANK Web Server 4096key").perform()
		ActionChains(driver).send_keys(Keys.ENTER).perform()
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.ID, 'btnSubmit')))
		driver.find_element_by_id("btnSubmit").click()
		Tools.load_page_url(self, 'Download certificate', 'Download certificate chain')
		time.sleep(1000)
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.NAME, 'username')))
		driver.find_element(By.NAME, "username").send_keys(consts.AUTH["USERNAME"])
		driver.find_element(By.NAME, "password").send_keys(consts.AUTH["PASSWORD"])
		driver.find_element(By.CSS_SELECTOR, ".btn").click()
		time.sleep(3)
	
	def login_BUAA(self):
		driver = self.driver
		driver.get(consts.URLS["IMS_URL"])
		driver.find_element(By.NAME, "username").send_keys(consts.AUTH["BUAA_USERNAME"])
		driver.find_element(By.NAME, "password").send_keys(consts.AUTH["BUAA_PASSWORD"])
		driver.find_element(By.CSS_SELECTOR, ".btn").click()
		time.sleep(3)
	
	def logout(self):
		driver = self.driver
		time.sleep(2)
		driver.execute_script("""document.querySelector('li[class="dropdown dropdown-user"]').firstElementChild.click()""")
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), ' Гарах')]")))
		driver.execute_script("""document.querySelector('li[class="dropdown dropdown-user open"]').lastElementChild.getElementsByTagName('li')[1].click()""")
	
	def closeNotification(self):
		driver = self.driver
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='brighttheme-icon-closer']")))
		driver.find_element(By.XPATH, "//span[@class='brighttheme-icon-closer']").click()

class certificate: 

	def create_csr_file (self):
		os.chdir('./report')
		with open('server.csr','r') as file:
			servercsr = file.read()
			file.close()
		csrFile = "".join(servercsr.split('\n')[1:-2])