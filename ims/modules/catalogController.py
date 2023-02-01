# -*- coding: UTF-8 -*
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from modules.constants import *
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
import os

date_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
date_time_access = datetime.datetime.now().strftime("%m/%d/%Y")
consts = Constant()


class Catalog:
	
	def menu_operation(self, operation):
		
		driver = self.driver
		if operation == "add":
			driver.find_element_by_xpath('//button[text()=" Салбар тооцооны төв нэмэх "]').click()
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.CLASS_NAME, "modal")))
			driver.find_element_by_xpath('//input[@placeholder="Салбарын код оруулна уу"]').send_keys(90057)
			driver.find_element_by_xpath('//input[@placeholder="Аймгийн код оруулна уу"]').send_keys(90057)
			driver.find_element_by_xpath('//input[@placeholder="Монгол нэрээ оруулна уу"]').send_keys("MONGOL NER")
			driver.find_element_by_xpath('//input[@placeholder="Англи нэрээ оруулна уу"]').send_keys("ANGLI NER")
			driver.find_element_by_xpath('//input[@placeholder="Хаягийн монгол нэрээ оруулна уу"]').send_keys("MONGOL")
			driver.find_element_by_xpath('//button[text()=" Хадгалах "]').click()
			time.sleep(5)
		elif operation == "edit":
			driver.execute_script('''
			function getElementByXpath(path) {
                return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
			}
			getElementByXpath('//*[text()="MONGOL NER"]').parentElement.children[11].children[0].click();
			''')
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-main/div/div/div/div[3]/app-admin/div/div[3]/div/div/div[2]/div/div/div/div[3]/div/input")))
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/app-admin/div/div[3]/div/div/div[2]/div/div/div/div[3]/div/input").clear()
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/app-admin/div/div[3]/div/div/div[2]/div/div/div/div[3]/div/input").send_keys('EDITED MONGOL NER')
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/app-admin/div/div[3]/div/div/div[2]/div/div/div/div[4]/div/input").clear()
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/app-admin/div/div[3]/div/div/div[2]/div/div/div/div[4]/div/input").send_keys('EDITED MONGOL NER')
			driver.find_element_by_id('pnotify-sucess1').click()
		elif operation == "delete":
			driver.execute_script('''
			function getElementByXpath(path) {
			    return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
			}
			getElementByXpath('//*[text()="EDITED MONGOL NER"]').parentElement.children[11].children[1].click();
			''')
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.ID, "pnotify-success2")))
			driver.find_element_by_id('pnotify-success2').click()
	
	def check_operation(self, status):
		driver = self.driver
		driver.refresh()
		if status == "new":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='MONGOL NER']")))
			driver.find_element_by_xpath("//*[text()='MONGOL NER']")
		
		elif status == "edited":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='EDITED MONGOL NER']")))
			driver.find_element_by_xpath("//*[text()='EDITED MONGOL NER']")
		elif status == "deleted":
			try:
				WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='MONGOL NER']")))
				driver.find_element_by_sxpath("//*[text()='EDITED MONGOL NER']")
			except Exception as e:
				print('OK')

