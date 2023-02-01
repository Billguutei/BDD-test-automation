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
import random as rn

date_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
date_time_access = datetime.datetime.now().strftime("%m/%d/%Y")
consts = Constant()


class MikSystem:

	
	def xml_add_information(self):
		driver = self.driver
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Огноо сонгох:"]')))
		driver.find_element_by_xpath('//input[@placeholder="Огноо сонгох:"]').click()
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Today"]')))
		driver.find_element_by_xpath('//button[text()="Today"]').click()
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//span[text()=" Мик актив сонгоно уу "]')))
		driver.find_element_by_xpath('//span[text()=" Мик актив сонгоно уу "]').click()
		ActionChains(driver).send_keys('МИК Актив 1').perform()
		ActionChains(driver).send_keys(Keys.RETURN).perform()
		driver.find_element_by_xpath('//button[text()=" Нэмэх "]').click()
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.NAME, 'description')))
		driver.find_element_by_name('key').send_keys(1234567890)
		driver.find_element_by_name('mikTxnCode').send_keys(1)
		driver.find_element_by_name('amount').send_keys(69420)
		driver.find_element_by_name('description').send_keys("some kind of description")
		driver.find_element_by_xpath('//button[text()=" Хадгалах "]').click()
	
	def fee_income(self):
		driver = self.driver
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Эхлэх огноо сонгох:"]')))
		driver.find_element_by_xpath('//input[@placeholder="Эхлэх огноо сонгох:"]').click()
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Today"]')))
		driver.find_element_by_xpath('//button[text()="Today"]').click()
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Дуусах огноо сонгох:"]')))
		driver.find_element_by_xpath('//input[@placeholder="Дуусах огноо сонгох:"]').click()
		driver.find_element_by_xpath('/html/body/app-root/app-main/div/div/div/div[3]/lib-mik/div[1]/div/div/div[2]/lib-datepicker/div/div/div/div/div/div/div[2]/button[1]').click()
		driver.find_element_by_xpath('//span[text()=" Сонголтоо хийнэ үү "]').click()
		ActionChains(driver).send_keys(' Хаан МИК Актив ').perform()
		ActionChains(driver).send_keys(Keys.RETURN).perform()
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.ID, 'downloadIncomeBtn')))
		driver.find_element_by_xpath('//button[text()=" Хайх "]').click()
		driver.find_element_by_xpath('//button[text()=" Тайлан татах "]').click()
		



	
	def xml_menu_operation(self, operation):
		driver = self.driver
		driver.refresh()
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Огноо сонгох:"]')))
		driver.find_element_by_xpath('//input[@placeholder="Огноо сонгох:"]').click()
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Today"]')))
		driver.find_element_by_xpath('//button[text()="Today"]').click()
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//span[text()=" Мик актив сонгоно уу "]')))
		driver.find_element_by_xpath('//span[text()=" Мик актив сонгоно уу "]').click()
		ActionChains(driver).send_keys('МИК Актив 1').perform()
		ActionChains(driver).send_keys(Keys.RETURN).perform()
		if operation == "download excel":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Хайх "]')))
			driver.find_element_by_xpath('//button[text()=" Хайх "]').click()
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-main/div/div""/div/div[3]/lib-mik/div[2]/div/div[""2]/div/div/div/div[2]/table/tbody/tr[""1]/td[7]/div/div[1]/button/i")))
			driver.execute_script('document.querySelector("#xml_table_wrapper > div.datatable-header > div.dt-buttons > a").click()')
		elif operation == "inquiry":
			driver.find_element_by_xpath('//button[text()=" Хайх "]').click()
			assert driver.execute_script("return document.getElementsByTagName('tr')[8].textContent") != ""
		elif operation == "download excel":
			driver.find_element_by_xpath('//button[text()=" Нэмэх "]').click()
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.NAME, 'description')))
			driver.find_element_by_name('key').send_keys(1234567890)
			driver.find_element_by_name('mikTxnCode').send_keys(1)
			driver.find_element_by_name('amount').send_keys(69420)
			driver.find_element_by_name('description').send_keys("some kind of description")
			driver.find_element_by_xpath('//button[text()=" Хадгалах "]').click()
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Хайх "]')))
			driver.execute_script('document.querySelector("#xml_table_wrapper > div.datatable-header > div.dt-buttons > a").click()')
		
		elif operation == "check excel":
			from datetime import datetime
			import os
			file_name = "МИК Актив 1_" + str(datetime.now()).split(' ')[0].replace('-', '') + ".xlsx"
			#import subprocess as sp
			#assert sp.call(['find','.','-name','download.xlsx'], stdout=sp.PIPE) == 1, 'file not found' #for linux
			#assert file_name in os.listdir('../../downloads/')
	
	def loan_account(self, operation):
		driver = self.driver
		if operation == "add account":
			driver.find_element_by_xpath("//button[text()=' Данс нэмэх ']").click()
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal')))
			driver.find_element_by_xpath('//*[@id="modal_new"]/div/div/div[2]/div/div/div/div/div[1]/input').send_keys(1234567890)
			driver.find_element_by_xpath('//*[@id="modal_new"]/div/div/div[2]/div/div/div/div/div[2]/input').send_keys("hahah")
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pnotify-sucess1"]')))
			driver.find_element_by_xpath('//*[@id="pnotify-sucess1"]').click()
		elif operation == "inquire loan account":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="trust_table_filter"]/label/input')))
			driver.find_element_by_xpath('//*[@id="trust_table_filter"]/label/input').send_keys('hahah')
			ActionChains(driver).send_keys(Keys.RETURN).perform()
			driver.find_element_by_xpath('//*[text()="hahah"]')
		elif operation == "delete loan account":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "trust_table"] / tbody / tr / td[3] / div / div / button / i')))
			driver.find_element_by_xpath('// *[ @ id = "trust_table"] / tbody / tr / td[3] / div / div / button / i').click()
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Устгах ']")))
			driver.find_element_by_xpath('//*[@id="modal_delete"]/div/div/div[3]/button[2]').click()
		elif operation == "download excel file":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Excel')))
			driver.find_element_by_link_text('Excel').click()
			time.sleep(3)
			from datetime import datetime
			import os
			file_name = "MIK_trust_account_" + str(datetime.now()).split(' ')[0].replace('-', '') + ".xlsx"
			#import subprocess as sp
			#assert sp.call(['find','.','-name','download.xlsx'], stdout=sp.PIPE) == 1, 'file not found' #for linux
			#assert file_name in os.listdir('../../downloads/') #Windowns
	
	def repayment_plan(self, operation):
		driver = self.driver
		if operation == "download excel":
			time.sleep(3)
			driver.find_element_by_link_text('Excel').click()
			#file_name = "Ergen data_" + str(datetime.datetime.now()).split(' ')[0].replace('-', '') + ".xlsx"
			#seconds = 0
			#dl_wait = True
			#while dl_wait and seconds < 20:
			#	time.sleep(1)
			#	dl_wait = False
			#	for fname in os.listdir("../../downloads/"):
			#		if fname.endswith('.crdownload'):
			#			dl_wait = True
			#	seconds += 1
			#import subprocess as sp
			#assert sp.call(['find','.','-name','download.xlsx'], stdout=sp.PIPE) == 1, 'file not found' #for linux
			#assert file_name in os.listdir('../../downloads/')
		elif operation == "inquire repayment":
			driver.find_element_by_link_text('Эргэн төлөлт харах').click()
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bottom-justified-tab2"]/div[1]/div/button[2]')))
			driver.execute_script('document.querySelector("#bottom-justified-tab2 > div:nth-child(1) > div > button:nth-child(2)").click()')
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nrs_table_filter"]/label/input')))
			driver.execute_script('document.querySelector("#nrs_table_wrapper > div.datatable-header > div.dt-buttons > a").click()')
			time.sleep(2)
		
		elif operation == "calculate repayment plan":
			driver.find_element_by_link_text('Эргэн төлөлт харах').click()
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bottom-justified-tab2"]/div[1]/div/button[2]')))
			driver.execute_script('document.querySelector("#bottom-justified-tab2 > div:nth-child(1) > div > button:nth-child(1)").click()')
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nrs_table_filter"]/label/input')))
		
		elif operation == "download example excel":
			driver.execute_script('document.querySelector("#bottom-justified-tab1 > div:nth-child(1) > div > div:nth-child(3) > button").click()')
		#	seconds = 0
		#	dl_wait = True
		#	while dl_wait and seconds < 20:
		#		time.sleep(1)
		#		dl_wait = False
		#		for fname in os.listdir("../../downloads/"):
		#		#import subprocess as sp
		#		#assert sp.call(['find','.','-name','download.xlsx'], stdout=sp.PIPE) == 1, 'file not found' #for linux
		#			if fname.endswith('.crdownload'):
		#				dl_wait = True
		#		seconds += 1

		elif operation == "create xml":
			driver.find_element_by_link_text('Эргэн төлөлт харах').click()
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bottom-justified-tab2"]/div[1]/div/button[2]')))
			driver.execute_script('document.querySelector("#bottom-justified-tab2 > div:nth-child(1) > div > button:nth-child(3)").click()')
			
			time.sleep(2)
	
	def add_account(self, operation):
		
		driver = self.driver
		if operation == "delete account":
			import random as rn
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CLASS_NAME, 'icon-trash')))
			accounts = [x.split(' ')[0] for x in [x.text for x in driver.find_elements_by_tag_name('tr')][1:10]]
			driver.find_element_by_xpath('//input[@placeholder="Хайх утгаа бичнэ үү..."]').send_keys(rn.choice(accounts))
			ActionChains(driver).send_keys(Keys.RETURN).perform()
			driver.find_element_by_class_name('icon-trash').click()
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Устгах "]')))
			driver.find_element_by_xpath('//button[text()=" Устгах "]').click()
		
		elif operation == "inquire account":
			driver.find_element_by_xpath('//span[text()=" Trust данс сонгоно уу "]').click()
			ActionChains(driver).send_keys(5118005852).perform()
			ActionChains(driver).send_keys(Keys.RETURN).perform()
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Хайх "]')))
			driver.find_element_by_xpath('//button[text()=" Хайх "]').click()
		
		elif operation == "add account":
			pass
		
		elif operation == "download excel":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CLASS_NAME, 'icon-trash')))
			driver.find_element_by_link_text('Excel').click()
			