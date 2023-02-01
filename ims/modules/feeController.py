# -*- coding: UTF-8 -*
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from modules.constants import *
from modules.utils import *
import time
import datetime
from selenium.webdriver.common.action_chains import ActionChains

date_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
consts = Constant()

class FeeService:

	def transfer(self, from_account):
			driver = self.driver
			if from_account == "EMPLOYEE_ACCOUNT":
				Task.all_tasks(self, "approved-transaction")
				WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="search"]')))
				driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх данс"]').send_keys(consts.ACCOUNTS['ACCOUNT'])
				driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх дүн"]').clear()
				time.sleep(2)
				driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх дүн"]').send_keys(consts.DATA['AMOUNT'])
				driver.find_element_by_xpath("//input[@placeholder='Хүлээн авах данс']").send_keys(consts.ACCOUNTS["INTERNAL_ACCOUNT"])
				driver.find_element_by_xpath("//input[@placeholder='Гүйлгээний утга']").send_keys(consts.DATA["DESCRIPTION"] + ' ' + date_time)
				WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Шилжүүлэх "]')))
				driver.execute_script("""document.querySelector("#transaction-panel > div:nth-child(1) > form > div > div.panel-body > div.text-right.mt-10 > button").click()""")
				time.sleep(3)
			elif account_type == "DEPOSIT_ACCOUNT":
				Task.all_tasks(self, "approved-transaction")
				WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="search"]')))
				driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх данс"]').send_keys(consts.ACCOUNTS['ACCOUNT'])
				driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх дүн"]').clear()
				time.sleep(2)
				driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх дүн"]').send_keys(consts.DATA['AMOUNT'])
				driver.find_element_by_xpath("//input[@placeholder='Хүлээн авах данс']").send_keys(consts.ACCOUNTS["INTERNAL_ACCOUNT"])
				driver.find_element_by_xpath("//input[@placeholder='Гүйлгээний утга']").send_keys(consts.DATA["DESCRIPTION"] + ' ' + date_time)
				WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Шилжүүлэх "]')))
				driver.execute_script("""document.querySelector("#transaction-panel > div:nth-child(1) > form > div > div.panel-body > div.text-right.mt-10 > button").click()""")
				time.sleep(3)
			elif from_account == "DEMAND_DEPOSIT_ACCOUNT":
				Task.all_tasks(self, "approved-transaction")
				time.sleep(10)
				WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(
					EC.element_to_be_clickable((By.XPATH, '//input[@type="search"]')))
				driver.find_element_by_xpath(
					'//input[@placeholder="Шилжүүлэх данс"]').send_keys(consts.ACCOUNTS['ACCOUNT'])
				driver.find_element_by_xpath(
					'//input[@placeholder="Шилжүүлэх дүн"]').clear()
				time.sleep(2)
				driver.find_element_by_xpath(
					'//input[@placeholder="Шилжүүлэх дүн"]').send_keys(consts.DATA['AMOUNT'])
				driver.find_element_by_xpath(
					"//input[@placeholder='Хүлээн авах данс']").send_keys(consts.ACCOUNTS["DEMAND_ACCOUNT"])
				driver.find_element_by_xpath("//input[@placeholder='Гүйлгээний утга']").send_keys(
					consts.DATA["DESCRIPTION"] + ' ' + date_time)
				WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(
					EC.element_to_be_clickable((By.XPATH, '//button[text()=" Шилжүүлэх "]')))
				driver.execute_script(
					"""document.querySelector("#transaction-panel > div:nth-child(1) > form > div > div.panel-body > div.text-right.mt-10 > button").click()""")
				time.sleep(3)