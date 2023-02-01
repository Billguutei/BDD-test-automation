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
import os

date_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
date_time_access = datetime.datetime.now().strftime("%m/%d/%Y")
consts = Constant()


class Loan:


	def loan_contract_report(self , loan_report_type):
		"""
		Зээлийн гэрээний тайлан 
		"""
		driver = self.driver
		if (loan_report_type == "Salary_loan_report"):
			WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((By.CLASS_NAME, "text-semibold")))
			driver.find_elements_by_link_text('Гэрээ эхлэх огноо')[0].click()
			driver.find_element_by_link_text('Тооцооны төв').click()
			driver.find_elements_by_class_name('input-group-btn')[1].click()   
			WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Excel']")))
			driver.find_elements_by_link_text('Excel')[0].click()
			

		elif(loan_report_type == "Savings_loan_report"):
			WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((By.CLASS_NAME, "text-semibold")))
			driver.find_elements_by_link_text('Гэрээ эхлэх огноо')[1].click()
			driver.find_element_by_link_text('Тооцооны төв').click()
			driver.find_elements_by_class_name('input-group-btn')[3].click()   
			WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Excel']")))
			driver.find_elements_by_link_text('Excel')[0].click()    

	def loan_interest_of_partner_organization(self , loan_interest_of_partner_organization_type):
		"""
		Хамтран ажиллагч байгууллагын хүү цэсний хийх 2 үйлдэл 
		"""
		driver = self.driver
		if (loan_interest_of_partner_organization_type == "Search_by_partner_organization_code" ):
					
			WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#DataTables_Table_0_filter > label > input[type=search]')))
			driver.find_elements_by_tag_name('input')[2].send_keys('FH568601')
			
			while True:
				
				partner_organization_code = driver.execute_script("""return document.querySelector("#DataTables_Table_0 > tbody > tr > td:nth-child(3)").textContent""")			
				if partner_organization_code == "FH568601":
					print("amjilttai")
					break
		time.sleep(1)

	def loan_send_request(self):

		driver = self.driver
		WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="РД оруулна уу"]')))
		driver.find_element_by_xpath('//input[@placeholder="РД оруулна уу"]').send_keys(consts.DATA["REGISTER_NO"])
		WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Хайх "]')))	
		driver.find_element_by_xpath('//button[text()=" Хайх "]').click()
		WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="spinner"]/div/form/div[1]/div/select/option[2]')))	
		driver.find_element_by_xpath('//*[@id="spinner"]/div/form/div[1]/div/select/option[2]').click()				
		WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Дүн оруулах"]')))	
		driver.find_element_by_xpath('//input[@placeholder="Дүн оруулах"]').send_keys("100000")				
		time.sleep(3)
		WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Илгээх "]')))			
		driver.find_element_by_xpath('//button[text()=" Илгээх "]').click()

	def	loan_search_register(self):
		driver = self.driver
		WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="РД оруулна уу"]')))
		driver.find_element_by_xpath('//input[@placeholder="РД оруулна уу"]').send_keys(consts.DATA["REGISTER_NO"])
		WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Хайх "]')))	
		driver.find_element_by_xpath('//button[text()=" Хайх "]').click()
		time.sleep(5)