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

class Statement:


	def customer_search(self, account_type, type):

		driver = self.driver
		if account_type == "LOAN_ACCOUNT":
			Task.all_tasks(self, "approved-loan_statement")
		elif account_type == "DEPOSIT_ACCOUNT":
			Task.all_tasks(self, "approved-statement")
		
		if(type == "name"):
			WebDriverWait(driver, timeout=30).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Хайх')]")))
			#driver.find_element_by_xpath("//button[text()='Хайх']").click()
			Tools.button_click(self, "//button[text()='Хайх']", "click", "",By.XPATH)
			time.sleep(2)
			driver.find_element_by_xpath('//span[text()="Овог нэрээр хайх"]')
			driver.find_elements_by_class_name('ui-dialog')[-1].find_elements_by_tag_name('input')[0].send_keys(consts.USER['FIRST_NAME'])
			driver.find_elements_by_class_name('ui-dialog')[-1].find_elements_by_tag_name('input')[1].send_keys(consts.USER['LAST_NAME'])
			driver.find_elements_by_class_name('ui-dialog')[-1].find_elements_by_tag_name('button')[-1].click()		
			time.sleep(2)
			driver.find_elements_by_tag_name('tr')[-1].click()
			#WebDriverWait(driver, timeout=30).until(EC.visibility_of_element_located((By.CLASS_NAME, "//span[text(), 'ХАРИЛЦАГЧИЙН ЛАВЛАГАА')]")))
			#driver.find_element_by_link_text('Харилцагчийн мэдээлэл').click()
			#float(driver.execute_script('return document.querySelector("#tab260450-6 > div:nth-child(8) > div:nth-child(1) > input").value').replace(',',''))
			time.sleep(2)
			driver.find_elements_by_class_name('ui-dialog')[-1].find_elements_by_tag_name('tr')[1].click()
			#open dansni dugarig songoh heseg
			driver.find_elements_by_class_name('ui-dialog')[-1].find_elements_by_tag_name('button')[0].click()
			driver.find_elements_by_class_name('ui-dialog')[-2].find_elements_by_tag_name('button')[0].click()
		elif(type == "account"):
			WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Дансны дугаараа оруулна уу...."]')))
			driver.find_element_by_xpath('//input[@placeholder="Дансны дугаараа оруулна уу...."]').send_keys(consts.ACCOUNTS['ACCOUNT'])
			time.sleep(1.5)
		driver.find_element_by_xpath('//*[@id="statement-panel"]/div[2]/form/div/div/div[2]/div/lib-date-range-picker/div/input').clear()
		driver.find_element_by_xpath('//*[@id="statement-panel"]/div[2]/form/div/div/div[2]/div/lib-date-range-picker/div/input').send_keys(consts.DATE['START_DATE'])
		driver.find_element_by_xpath('//*[@id="statement-panel"]/div[2]/form/div/div/div[2]/div/lib-date-range-picker/div/input').send_keys(Keys.ENTER)
		driver.find_element_by_xpath('//*[@id="statement-panel"]/div[2]/form/div/div/div[3]/div/lib-date-range-picker/div/input').clear()
		driver.find_element_by_xpath('//*[@id="statement-panel"]/div[2]/form/div/div/div[3]/div/lib-date-range-picker/div/input').send_keys(consts.DATE['END_DATE'])
		driver.find_element_by_xpath('//*[@id="statement-panel"]/div[2]/form/div/div/div[3]/div/lib-date-range-picker/div/input').send_keys(Keys.ENTER)
		driver.find_element_by_xpath('//span[text()=" 02: Монгол "]').click()
		ActionChains(driver).send_keys('01').perform()
		ActionChains(driver).send_keys(Keys.ENTER).perform()
		"""
		beltgeh der darah heseg
		"""
		driver.execute_script("document.querySelector('#statement-panel > div:nth-child(2) > form > div > div > div.text-right.mt-10 > button').click()")
		
		WebDriverWait(driver, timeout=30).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), ' Шинэчлэх ')]")))
		#driver.find_element_by_xpath("//*[contains(text(), ' Шинэчлэх ')]").click()
		Tools.button_click(self, "xpath", " Шинэчлэх ", "")
		WebDriverWait(driver, timeout=30).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), ' Хэвлэх ')]")))
		#driver.find_element_by_xpath("//*[contains(text(), ' Хэвлэх ')]").click()
		Tools.button_click(self, "xpath", " Хэвлэх ", "")
		WebDriverWait(driver, timeout=30).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), ' Хэвлэх ')]")))
		#driver.find_element_by_xpath("//button[text()=' Хэвлэх ']").click()
		Tools.button_click(self, "xpath", " Хэвлэх ", "")
		time.sleep(2)
		driver.switch_to_window(driver.window_handles[-1])
		driver.execute_script('document.querySelector("body > print-preview-app").shadowRoot.querySelector("#sidebar").shadowRoot.querySelector("print-preview-button-strip").shadowRoot.querySelector("cr-button.cancel-button").click()')
		#WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.ID, 'plugin')))
		#EC.number_of_windows_to_be(2)
		time.sleep(5)
		driver.switch_to_window(driver.window_handles[-1])
		#WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.TAG_NAME, 'print-preview-app')))
		#Tools.take_screenshot_by_tag_name(self, "print-preview-app", "statement", True)
		select = driver.execute_script("return document.querySelector('print-preview-app').shadowRoot.querySelector('print-preview-sidebar').shadowRoot.querySelector('print-preview-destination-settings').root.querySelector('print-preview-destination-select').root.querySelector('select.md-select');") 
		options = select.find_elements_by_tag_name('option')
		save_pdf_by_index = [x.text for x in options].index('    Save as PDF\n  ' )
		options[save_pdf_by_index].click()
		time.sleep(3)
		driver.execute_script('document.querySelector("body > print-preview-app").shadowRoot.querySelector("#sidebar").shadowRoot.querySelector("print-preview-button-strip").shadowRoot.querySelector("cr-button.action-button").click();')
		time.sleep(5)
		pyautogui.press('enter')
		time.sleep(10)

	def status_statement(self):

		driver = self.driver
		Task.all_tasks(self, "dep_statement")

		WebDriverWait(driver, timeout=30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#accounts-panel_filter > label > input[type=search]')))
		driver.find_element_by_css_selector('#accounts-panel_filter > label > input[type=search]').send_keys(consts.ACCOUNTS["DEPOSIT_ACCOUNT"])
		driver.execute_script("document.querySelector('#accounts-panel > tbody:nth-child(2) > tr').click()")
		time.sleep(1.5)
		driver.find_element_by_xpath('//*[@id="statement-panel"]/div[2]/form/div/div/div[2]/div/lib-date-range-picker/div/input').clear()
		driver.find_element_by_xpath('//*[@id="statement-panel"]/div[2]/form/div/div/div[2]/div/lib-date-range-picker/div/input').send_keys(consts.DATE['START_DATE_LIMIT'])
		driver.find_element_by_xpath('//*[@id="statement-panel"]/div[2]/form/div/div/div[2]/div/lib-date-range-picker/div/input').send_keys(Keys.ENTER)
		driver.find_element_by_xpath('//*[@id="statement-panel"]/div[2]/form/div/div/div[3]/div/lib-date-range-picker/div/input').clear()
		driver.find_element_by_xpath('//*[@id="statement-panel"]/div[2]/form/div/div/div[3]/div/lib-date-range-picker/div/input').send_keys(consts.DATE['END_DATE_LIMIT'])
		driver.find_element_by_xpath('//*[@id="statement-panel"]/div[2]/form/div/div/div[3]/div/lib-date-range-picker/div/input').send_keys(Keys.ENTER)
		#driver.find_element_by_xpath('//span[text()=" 02: Монгол "]').click()
		Tools.button_click(self, driver.find_element_by_xpath('//span[text()=" 02: Монгол "]'), "none", "")
		ActionChains(driver).send_keys('01').perform()
		ActionChains(driver).send_keys(Keys.ENTER).perform()
		"""
		beltgeh der darah heseg
		"""
		driver.execute_script("document.querySelector('#statement-panel > div:nth-child(2) > form > div > div > div.text-right.mt-10 > button').click()")
		
		WebDriverWait(driver, timeout=30).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), ' Шинэчлэх ')]")))
		#driver.find_element_by_xpath("//*[contains(text(), ' Шинэчлэх ')]").click()
		Tools.button_click(self, "xpath", " Шинэчлэх ", "")
		time.sleep(5)
		#driver.find_element_by_xpath("//*[contains(text(), ' Шинэчлэх ')]").click()
		Tools.button_click(self, "xpath", " Шинэчлэх ", "")
		Tools.take_screenshot_by_class_name(self, "odd", "limited_statement", True)

class IntegratedAmount:


	def integrate_service(self, type):

		driver = self.driver
		if(type == "Search"):
			WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='text-semibold']")))
			Tools.button_click(self, "xpath", " Хайх ", "")
			WebDriverWait(driver,consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.CLASS_NAME, "table")))
			Tools.take_screenshot_by_class_name(self, "content", "Integrated_amount", True)
			time.sleep(5)
		elif(type == "Download"):
			WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='text-semibold']")))
			#driver.find_element_by_xpath("//button[text()=' PDF ']").click()
			Tools.button_click(self, "xpath", " PDF ", "")
			time.sleep(5)
		elif(type == "Print"):
			WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='text-semibold']")))
			#driver.find_element_by_xpath("//button[text()=' Хэвлэх ']").click()
			Tools.button_click(self, "xpath", " Хэвлэх ", "")
			driver.switch_to_window(driver.window_handles[0])
			WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.CLASS_NAME, 'action-button')))
			driver.execute_script('document.querySelector("body > print-preview-app").shadowRoot.querySelector("#sidebar").shadowRoot.querySelector("print-preview-button-strip").shadowRoot.querySelector("cr-button.action-button").click()')
			time.sleep(5)
			
class Cash_drawer:


	def CashExchange(self, type):

		driver = self.driver
		if(type == "Change_banknotes"):
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn")))
			#driver.find_element(By.XPATH, "//*[contains(text(), 'Дэвсгэрт солих')]").click()
			Tools.button_click(self, "xpath", "Дэвсгэрт солих", "")
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CLASS_NAME, 'modal-content')))
			driver.find_element_by_xpath('//*[@id="cash-registry"]/div/div/div[2]/div/table/tbody/tr[1]/td[4]/input').clear()
			driver.find_element_by_xpath('//*[@id="cash-registry"]/div/div/div[2]/div/table/tbody/tr[1]/td[4]/input').send_keys(1)
			driver.find_element_by_xpath('//*[@id="cash-registry"]/div/div/div[2]/div/table/tbody/tr[2]/td[6]/input').clear()
			driver.find_element_by_xpath('//*[@id="cash-registry"]/div/div/div[2]/div/table/tbody/tr[2]/td[6]/input').send_keys(2)
			driver.find_element_by_xpath('//*[@id="cash-registry"]/div/div/div[2]/div/table/tbody/tr[2]/td[6]/input').send_keys(Keys.ENTER)
			driver.execute_script('document.querySelector("#cash-registry > div > div > div.modal-header > div > div.col-xs-3.mt-7 > div > button.btn.btn-default.btn-xs.mr-7").click()')
			#print("notification_msg: " + notification_msg + '\nsuccess_messages:' + success_messages)
			#assert (notification_msg == success_messages)
			time.sleep(10)
		elif(type == "Open_CashList"):
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn")))
			Tools.button_click(self, "contains", "Дэвсгэртийн жагсаалт нээх", "")