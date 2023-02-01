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


class Nostro:


	def nostro_account_replenishment(self , choose_tab):
		"""
		Nostro  dansnii zuzaatgal "2 tabaar yalgagdaj hiigdene tab name - eer angilagdana " 
		"""
		driver = self.driver
		if (choose_tab == "MID_office_approve"):
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.ID, 'order_midconfirm_table_wrapper')))
			time.sleep(2)
			driver.execute_script('document.querySelector("#order_midconfirm_table > tbody > tr:nth-child(1) > td.text-center > div > div:nth-child(1) > button > i").click()')
			time.sleep(2)
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Шийдвэр баталгаажуулах')]")))
			time.sleep(2)
			driver.find_element(By.XPATH, "//*[contains(text(), ' Баталгаажуулах ')]").click()

	def nostro_list_report(self, search_type):
		"""
		Nostro jagsaalt tailan Tailan harahad 5 torol baidag ba torol bureer n nohtsol shalgaad haina 5 scenario baina gesen ug  
		"""
		driver = self.driver
		if (search_type == "Shiidveruud"):
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.ID, 'startDate')))
			driver.find_element(By.XPATH, "//*[contains(text(), ' Хайх ')]").click()
			time.sleep(5)

	def nostro_approved_decisions(self):
		"""
		Nostro zovshoorogdson shiidveruud
		"""
		driver = self.driver
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.ID, 'nostro_approved_table')))
		time.sleep(2)
		driver.execute_script('document.querySelector("#nostro_approved_table > tbody > tr > td.sorting_1").click()')
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.ID, 'modal_view_nostro_approved')))
		driver.find_element_by_xpath("//button[@type='submit']").click()
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Хүлээн авагчийн бүтэн нэр:')]")))
		driver.find_element(By.NAME, "receiverFullName").send_keys(17325)
		driver.find_element(By.NAME, "receiverBankName").send_keys(123123)
		driver.find_element_by_xpath('//button[text()=" Шалгах "]').click()
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Мессеж төрөл:')]")))
		driver.find_element_by_xpath('//button[text()=" Оруулах "]').click()
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), ' :57: Account with Institution ')]")))	
		driver.find_element_by_xpath("//button[@type='submit']").click()
		time.sleep(2)

	def nostro_transfer_type(self, type ):
		"""
		Nostro guilgee tses n 4n torol haruuldag 
		"""
		driver = self.driver
		if (type == "Successed"):
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.NAME, 'selectedStatus')))
			driver.find_element_by_xpath('/html/body/app-root/app-main/div/div/div/div[3]/lib-nostro-transfer/div/div[1]/div/div/div/div/select/option[4]').click()
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#transfer_table > tbody > tr:nth-child(1) > td.sorting_1')))
			driver.execute_script('document.querySelector("#transfer_table > tbody > tr:nth-child(1)").click()')
			driver.find_element_by_xpath("//button[@type='submit']").click()
			driver.find_element_by_xpath('//button[text()=" Принтер"]').click()
			
		 