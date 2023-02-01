# -*- coding: UTF-8 -*
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from modules.constants import *
from modules.utils import Tools
import time
import datetime
from selenium.webdriver.common.action_chains import ActionChains

date_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
consts = Constant()

DATA = {
		"CARD_NUMBER_DEBIT": "9496188176781156",
		"card_name": "TEST CARD",
		"phoneNumber": "19070149",
		"phoneNumber2": "19884271",
		"email": "rasuka0502@gmail.com",
		"postAddress":  "Хан-уул дүүрэг , наадам сентэр , Хаан банк цамхаг 20-20-107",
		"CHANGE_LIMIT":  {
			"number": "1",
			"size": "2000000",
			"description": "test test test test test test "
			
		
		}
	}
# main class of CardController
class card:

	def customer_search(self,account_type):
		driver = self.driver
		if account_type == "new-card":
			Tools.button_click(self, "input_placeholder", "Харилцагчийн дансны дугаар", consts.ACCOUNTS["ACCOUNT_OF_NEW_CARD"],"")
		elif account_type == "reissue":
			Tools.button_click(self, "input_placeholder", "Харилцагчийн дансны дугаар", consts.ACCOUNTS["ACCOUNT_OF_REISSIE_CARD"],"")
		elif account_type == "renewal":
			Tools.button_click(self, "input_placeholder", "Харилцагчийн дансны дугаар", consts.ACCOUNTS["ACCOUNT_OF_RENEWAL_CARD"],"")
		elif account_type == "close":
			Tools.button_click(self, "input_placeholder", "Харилцагчийн дансны дугаар", consts.ACCOUNTS["ACCOUNT_OF_CLOSE_CARD"],"")
		elif account_type == "changeLimitofTranaction":
			Tools.button_click(self, "input_placeholder", "Харилцагчийн дансны дугаар", consts.ACCOUNTS["ACCOUNT_OF_CHANGE_LIMIT_TRANSACTION"],"")
		
		Tools.button_click(self, '//button[text()=" Хайх "]', "click", "",By.XPATH)
		
	def card_search(self, search_type):
		driver = self.driver

		if search_type == "account_number":
			Tools.button_click(self, "input_placeholder", "Харилцагчийн дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"],"")

		elif search_type == "card_number":
			Tools.button_click(self, "//*[@id='block-page']/div[2]/div/div/div/div[1]/button/a", "click", "", By.XPATH)
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#block-page > div.panel-body > div > div > div > div.input-group-btn.open > ul > li:nth-child(2) > a"))).click()
			Tools.button_click(self, "input_placeholder", "Харилцагчийн картын дугаар оруулах", DATA['CARD_NUMBER_DEBIT'],"")

		elif search_type == "cif_number":
			Tools.button_click(self, "//*[@id='block-page']/div[2]/div/div/div/div[1]/button/a", "click", "", By.XPATH)
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#block-page > div.panel-body > div > div > div > div.input-group-btn.open > ul > li:nth-child(3) > a"))).click()
			Tools.button_click(self, "input_placeholder", "Харилцагчийн cif оруулах", consts.ACCOUNTS["CIF"],"")

		Tools.button_click(self, '//button[text()=" Хайх "]', "click", "",By.XPATH)

    #order new card
	def card_order_new(self, field_type):
		driver = self.driver
		Tools.button_click(self, "//*[@id='card-search']/div[1]/div/div[2]/div/div/div[1]/select", "click", "", By.XPATH)
		card.click_arrow_down(self , 3)
		Tools.button_click(self, "//*[@id='card-search']/div[1]/div/div[2]/div/div/div[2]/select", "click", "",By.XPATH)
		card.click_arrow_down(self , 1)

		if field_type == "fee-manaul":
			Tools.button_click(self, "//*[@id='card-search']/div[1]/div/div[2]/div/div/div[4]/label[3]/input", "click", "",By.XPATH)

		Tools.button_click(self,"input_placeholder","example@example.com", DATA['email'],"")
		Tools.button_click(self, "//input[@name='Pname']", "clear", "", By.XPATH)
		Tools.button_click(self, "//input[@name='Pname']", "send_keys", DATA['card_name'], By.XPATH)
	
		Tools.button_click(self, "//input[@name='contactNo']", "clear", "", By.XPATH)
		Tools.button_click(self, "//input[@name='contactNo']", "send_keys", DATA['phoneNumber'], By.XPATH)
		Tools.button_click(self, "//select[@name='selectedLocation']", "click", "", By.XPATH)

		if field_type == "branch":
			card.address_branch(self)
		else:
			card.address_post(self)
		Tools.button_click(self, '//button[text()=" Захиалах "]', "click", "",By.XPATH)

	#Function of order reissue card
	def card_order_reissue_renewal(self,field_type):

		driver = self.driver
		WebDriverWait(driver,timeout=30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="blocks-page"]/div[2]/div/div[1]/select/option')))
		driver.find_element_by_xpath("//*[@id='blocks-page']/div[2]/div/div[1]/select/option").click()

		WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="blocks-page"]/div[2]/div/div[2]/select/option')))
		driver.find_element_by_xpath("//*[@id='blocks-page']/div[2]/div/div[2]/select/option").click()

		WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="block-pagess"]/div[2]/div/div[1]/select/option[1]')))
		driver.find_element_by_xpath("//*[@id='block-pagess']/div[2]/div/div[1]/select/option[1]").click()

		WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="block-pagess"]/div[2]/div/div[5]/input')))
		driver.find_element_by_xpath("//*[@id='block-pagess']/div[2]/div/div[5]/input").click()

		if field_type == "fee-manaul":
			Tools.button_click(self, "//*[@id='block-pagess']/div[2]/div/div[2]/label[3]/input", "click", "", By.XPATH)

		Tools.button_click(self, "//input[@name='Pname']", "clear", "", By.XPATH)
		Tools.button_click(self, "//input[@name='Pname']", "send_keys", DATA['card_name'], By.XPATH)

		Tools.button_click(self, "//input[@name='contactNo']", "send_keys", DATA['phoneNumber'], By.XPATH)
		Tools.button_click(self, "//select[@name='selectedLocation']", "click", "", By.XPATH)

		if field_type == "branch":
			card.address_branch(self)
		else:
			card.address_post(self)
		
		Tools.button_click(self, '//button[text()=" Оруулах "]', "click", "",By.XPATH)
	

	#close card function
	def close_card(self):
		driver = self.driver
		Tools.button_click(self, "//*[@id='block-pages']/div/div/div[2]/table/tbody/tr[1]/td[7]/i", "click", "", By.XPATH)
		Tools.button_click(self, '//button[text()=" Карт хаах "]', "click", "",By.XPATH)

	# Change limit of Transaction Fuction
	def change_limit(self,cash_type):
		driver = self.driver
		Tools.button_click(self, "//*[@title=' Сонгоно уу ']", "click", "",By.XPATH)
		card.click_arrow_down(self , 1)
		Tools.button_click(self, "//*[@id='blocks1-page']/div[2]/div/div[1]/div[1]/div/select", "click", "", By.XPATH)
		if cash_type == "cash":
			card.click_arrow_down(self , 1)
		elif cash_type == "non-cash":
			card.click_arrow_down(self , 2)
		
		Tools.button_click(self, "//*[@id='blocks1-page']/div[2]/div/div[1]/div[2]/div/input", "send_keys", DATA['CHANGE_LIMIT']['number'], By.XPATH)
		Tools.button_click(self, "//*[@id='blocks1-page']/div[2]/div/div[1]/div[3]/div/input", "send_keys", DATA['CHANGE_LIMIT']['size'], By.XPATH)
		Tools.button_click(self, "//*[@id='blocks1-page']/div[2]/div/div[2]/div/div/input", "send_keys", DATA['CHANGE_LIMIT']['description'], By.XPATH)
		Tools.button_click(self, '//button[text()=" Өөрчлөх "]', "click", "",By.XPATH)

		
	# card order choose address is branch function
	def address_branch(self):
		driver = self.driver
		card.click_arrow_down(self , 1)
		Tools.button_click(self, "//*[@title=' Аймаг/Хот сонгоно уу ']", "click", "",By.XPATH)
		card.click_arrow_down(self , 1)
		time.sleep(1)
		Tools.button_click(self, "//*[@title=' Сум/Дүүрэг сонгоно уу ']", "click", "",By.XPATH)
		card.click_arrow_down(self , 2)

	# card order choose  address is post function
	def address_post(self):
		driver = self.driver
		card.click_arrow_down(self , 2)
		Tools.button_click(self, "//*[@title=' Аймаг/Хот сонгоно уу ']", "click", "",By.XPATH)								  
		card.click_arrow_down(self , 1)
		time.sleep(1)
		Tools.button_click(self, "//*[@title=' Сум/Дүүрэг сонгоно уу ']", "click", "",By.XPATH)
		card.click_arrow_down(self , 1)
		Tools.button_click(self, "//textarea[@placeholder='Зөвхөн крилл үсгээр бичнэ']", "send_keys", DATA['postAddress'], By.XPATH)
		Tools.button_click(self, "//input[@name='phoneNumber1']", "send_keys", DATA['phoneNumber'], By.XPATH)
		Tools.button_click(self, "//input[@name='phoneNumber2']", "send_keys", DATA['phoneNumber2'], By.XPATH)

	def click_arrow_down(self , length):
		driver = self.driver
		for x in range(length):
			ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
		ActionChains(driver).send_keys(Keys.RETURN).perform()
