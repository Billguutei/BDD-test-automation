# -*- coding: UTF-8 -*
import datetime
import os
import os.path
import time

from modules.constants import Constant
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.remote.webelement import WebElement

date_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
date_time_access = datetime.datetime.now().strftime("%m/%d/%Y")
consts = Constant()

global_account_type = None
success_messages = None
task_name = None

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
	
	def search_date(self):
		driver = self.driver
		driver.find_element_by_class_name('icon-calendar22.text-size-small').click()
		# driver.find_element_by_class_name('icon-arrow-left32').click()
		driver.find_element_by_xpath("//td[text()='21']").click()
		driver.find_element_by_xpath("//td[text()='21']").click()
		driver.find_element_by_xpath("//button[text()='Сонгох']").click()			

	def load_page(self, window_name):
		
		driver = self.driver
		window_name_split = window_name.split('-')
		if window_name == "1010":
			Tools.load_page_url(self, 'Гүйлгээ', 'Бэлэн', 'Орлого')
		
		elif window_name == "1060":
			Tools.load_page_url(self, 'Гүйлгээ', 'Бэлэн', 'Зарлага')
		
		elif window_name == "21046":
			Tools.load_page_url(self, 'Гүйлгээ', 'Бэлэн', 'Валют арилжаа')
		
		elif window_name == "1054":
			Tools.load_page_url(self, 'Гүйлгээ', 'Бэлэн бус', 'Банк хооронд')

		elif window_name == "450" or window_name == "400" or window_name == "440":
			Tools.load_page_url(self, 'Лавлагаа', 'Депозит дансны лавлагаа')

		elif window_name == "1042" or window_name == "1043":
			Tools.load_page_url(self, 'Гүйлгээ', 'Бэлэн бус', 'Банк хооронд')
		
		elif window_name == "1360":
			Tools.load_page_url(self, 'Гүйлгээ', 'Бэлэн', 'Х.тай хад зарлага')
		
		elif window_name == "4045" or window_name == "14045":
			Tools.load_page_url(self, 'Гүйлгээ', 'Бэлэн бус', 'Банк дотор')
		
		elif window_name == "3045":
			Tools.load_page_url(self, 'Гүйлгээ', 'Депозит данс хаах')
		
		elif window_name == "20010":
			Tools.load_page_url(self, 'Гүйлгээ', 'Дотоодын гүйлгээ', 'Орлого')
		
		elif window_name == "20060":
			Tools.load_page_url(self, 'Гүйлгээ', 'Дотоодын гүйлгээ', 'Зарлага')

		elif window_name == "11055":
			Tools.load_page_url(self, 'Гүйлгээ', 'Зээлийн гүйлгээ', 'Зээл олголт')

		elif window_name == "11044":
			Tools.load_page_url(self, 'Гүйлгээ', 'Зээлийн гүйлгээ', 'Шугамын зээлийн төлөлт')
		
		elif window_name == "3060":
			Tools.load_page_url(self, 'Гүйлгээ', 'Депозит данс хаах')
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CLASS_NAME, 'modal-header')))
			driver.execute_script("document.querySelector('#modal_form_vertical > div > div > div.modal-header > button').click()")
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CLASS_NAME, 'modal-header')))
			driver.execute_script("document.querySelector('#finger-print > div.modal-header > button').click()")
			Tools.load_page_url(self, 'Бэлнээр')

		elif window_name == "20450" or window_name == "20400":
			Tools.load_page_url(self, 'Лавлагаа', 'Дотоодын дансны лавлагаа')
			
		elif window_name == "60450" or window_name == "9022":
			Tools.load_page_url(self, 'Лавлагаа', 'Харилцагчийн лавлагаа')
		
		elif window_name == "10400" or window_name == "10440" or window_name == "10450" or window_name == "13000":
			Tools.load_page_url(self, 'Лавлагаа', 'Зээлийн дансны лавлагаа')

		elif window_name == "transaction list":
			LoginsClass.login(self)
			WebDriverWait(driver, timeout=30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'nav-item')))
			Tools.load_page_url(self, 'Гүйлгээ', 'Гүйлгээний жагсаалт')
		
		elif window_name == "1345":
			Tools.load_page_url(self, 'Гүйлгээ', 'Бэлэн бус', 'Х.тай хад зарлага')
		
		elif window_name_split[0] == "document":
			if window_name_split[1] == "maintenance":
				Tools.load_page_url(self, 'Бичиг баримт', 'Бичиг баримт засварлах')
			elif window_name_split[1] == "service":
				Tools.load_page_url(self, 'Бичиг баримт', 'Үйлчилгээ')
			elif window_name_split[1] == "definitionDeposit":
				Tools.load_page_url(self, 'Бичиг баримт', 'Дансны тодорхойлолт','Депозит данс')
			elif window_name_split[1] == "definitionLoan":
				Tools.load_page_url(self, 'Бичиг баримт', 'Дансны тодорхойлолт','Зээлийн данс')
			elif window_name_split[1] == "embassyKorea":
				Tools.load_page_url(self, 'Бичиг баримт', 'Элчин сайдын яам','Бүгд Найрамдах Солонгос Улс')
			elif window_name_split[1] == "upgradeBranch":
				Tools.load_page_url(self, 'Бичиг баримт', 'Салбарын тохиргоо')
		#To call consumer loan>Лавлагаа 
		elif window_name_split[0] == "consumerloan":
			if window_name_split[1] == "lavlagaa":
				Tools.load_page_url(self, 'Consumer loan')
				Tools.button_click(self, "/html/body/app-root/app-main/div/div/div/div[1]/lib-sidebar/div/div[2]/div/ul/li[15]/ul/li[1]/a", "click", "",By.XPATH)
				
		
		elif window_name_split[0] == "card":
			if window_name_split[1] == "search":
				Tools.load_page_url(self, 'Карт', 'Хайлт')
			elif window_name_split[1] == "orderOfNewCard":
				Tools.load_page_url(self, 'Карт', 'Шинэ картын захиалга')
			elif window_name_split[1] == "reissue" or window_name_split[1] == "renewal":
				Tools.load_page_url(self, 'Карт', 'Нөхөн авалт,сунгалт')
			elif window_name_split[1] == "close":
				Tools.load_page_url(self, 'Карт', 'Карт хаах')
			elif window_name_split[1] == "changeLimitofTranaction":
				Tools.load_page_url(self, 'Карт', 'Картын гүйлгээний лимит өөрчлөх')
				
		elif window_name_split[0] == "tax":
			if window_name_split[1] == "service":
				Tools.load_page_url(self, 'Татвар', 'Татварын үйлчилгээ')

		elif window_name_split[0] == "forex":
			if window_name_split[1] == "deals":
				Tools.load_page_url(self, 'Хэлцэл', 'Зөвшөөрөгдсөн хэлцлүүд')

		elif window_name == "tax_window":
			Tools.load_page_url(self, 'Татвар', 'Татвар тайлан')

		elif window_name == "account_balance_guarantee":
			Tools.load_page_url(self, 'Бичиг баримт', 'Дансны үлдэгдлийн баталгаа')

		elif window_name == "Salary_loan_report" or window_name == "Savings_loan_report":
			Tools.load_page_url(self, 'Зээл','Гэрээний тайлан')

		elif window_name == "Search_by_partner_organization_code" or window_name == "Add_organization":
			Tools.load_page_url(self, 'Зээл','Хамтран ажиллагч байгууллагын хүү')

		elif window_name == "savings backed loan": 
			Tools.load_page_url(self, 'Зээл', 'Хадгаламж барьцаалсан зээл')			

		elif window_name == "statement":
			Tools.load_page_url(self, 'Дансны хуулга', 'Депозит дансны хуулга')
		
		elif window_name == "loan_statement":
			Tools.load_page_url(self, 'Дансны хуулга', 'Зээлийн дансны хуулга')
		
		elif window_name == "User_IntegratedAmount":
			Tools.load_page_url(self, 'Гүйлгээ', 'Нэгтгэл', 'Хэрэглэгчийн нэгтгэсэн дүн')
		
		elif window_name == "Branch_IntegratedAmount":
			Tools.load_page_url(self, 'Гүйлгээ', 'Нэгтгэл', 'Салбарын нэгтгэсэн дүн')
		
		elif window_name == "request":
			Tools.load_page_url(self, 'Хүсэлт', 'Хүсэлтийн жагсаалт')

		elif window_name == "report":
			Tools.load_page_url(self, 'Тайлан', 'Дансны тодорхойлолт-Хураамж суутгасан')
		elif window_name == "report_contract":
			Tools.load_page_url(self, 'Тайлан', 'Цахим гэрээ шинэчилсэн тайлан')

		elif window_name == "nostro_main":
			Tools.load_page_url(self, 'Ностро данс', 'Ностро дансны зузаатгал')
		
		elif window_name == "nostro_report":
			Tools.load_page_url(self, 'Ностро данс', 'Ностро жагсаалт тайлан')

		elif window_name == "nostro_approved":
			Tools.load_page_url(self, 'Ностро данс', 'Зөвшөөрөгдсөн шийдвэрүүд')

		elif window_name == "nostro_transfer":
			Tools.load_page_url(self, 'Ностро данс', 'Ностро гүйлгээ')
		
		elif window_name == "dispitcher":
			Tools.load_page_url(self, 'Автомат гүйлгээ', 'Тохиргоо')

		elif window_name == "dispitcher_report":
			driver.get("https://192.168.7.64:9001/home/dispitcher/report")

		elif window_name_split[0] == "access":
			Tools.load_page_url(self, 'Хандах эрхийн тохиргоо')
			if window_name_split[1] == "menu":
				Tools.load_page_url(self, 'Цэс')
				
			elif window_name_split[1] == "group":
				Tools.load_page_url(self, 'Эрхийн бүлэг')
				
			elif window_name_split[1] == "module":
				Tools.load_page_url(self, 'Модуль')
				
			elif window_name_split[1] == "product":
				Tools.load_page_url(self, 'Бүтээгдэхүүн')
			
			elif window_name_split[1] == "connection":
				Tools.load_page_url(self, 'Холбоос')
			
			elif window_name_split[1] == "user access":
				Tools.load_page_url(self, "Хэрэглэгч")
		
		elif window_name_split[0] == "Behavioral scoring":
			Tools.load_page_url(self, 'Behavioral скоринг')
			sub_menu = {
				'config': 'Behavioral скоринг тохиргоо ',
				'list': 'Behavioral скоринг жагсаалт ',
				'risk group list': 'Behavioral risk group жагсаалт ',
				'risk group config': 'Behavioral risk group тохиргоо '
			}
			try:
				Tools.load_page(self, sub_menu[window_name_split[1]])
			except:
				raise KeyError(sub_menu.keys())
		
		elif window_name == "branch admin":
			Tools.load_page_url(self, "Catalog admin", "Branch admin")
		
		elif window_name == "organization list":
			Tools.load_page_url(self, "Байгууллагын бүртгэл", "Байгууллагын жагсаалт")

		elif window_name == "organization registry":
			Tools.load_page_url(self, "Байгууллагын бүртгэл", "Тохиргоо хийх")

		elif window_name == "organization registry supList":
			Tools.load_page_url(self, "Байгууллагын бүртгэл", "Албан тушаалтан жагсаалт")

		elif window_name == "organization registry create":
			Tools.load_page_url(self, "Байгууллагын бүртгэл", "Гэрээ байгуулах")
		
		elif window_name == "My_create_task":
				
			Tools.load_page_url(self, "Таск","Миний үүсгэсэн ажлууд")
			
		elif window_name == "Assigned_to_team":
				
			Tools.load_page_url(self, "Таск","Багт хувиарлагдсан ажлууд")
			
		elif window_name == "Assigned_to_me":
				
			Tools.load_page_url(self, "Таск","Надад хувиарлагдсан ажлууд")
		
		elif window_name == "rate show":            
			Tools.load_page_url(self, "Ханш шинэчлэлт","Ханш харах")
		
		elif window_name == "rate modify":
			Tools.load_page_url(self, "Ханш шинэчлэлт", "Ханш шинэчлэх")
			
		elif window_name == "rate history":
			Tools.load_page_url(self, "Ханш шинэчлэлт", "Ханшийн түүх") 

		elif window_name_split[0] == "bulk":
			Tools.load_page_url(self, "Багц гүйлгээ")
			if window_name_split[1] == "list":
				Tools.load_page_url(self, "Багц гүйлгээний жагсаалт")
			elif window_name_split[1] == "branchlist":
				Tools.load_page_url(self, "Түр данс жагсаалт")

		elif window_name == "allowance_customer":
			Tools.load_page_url(self, "Нөхөн төлбөр", "Нөхөн төлбөр лавлах")
		
		elif window_name == "allowance userReport":
			Tools.load_page_url(self, "Нөхөн төлбөр", "Нөхөн төлбөрийн тайлан") 
		
		elif window_name == "inquiry_loan_history_consumerloan":
			Tools.load_page_url(self, 'Consumer loan', 'Зээлийн түүх лавлах')

		elif window_name_split[0] == "mik":
			Tools.load_page_url(self, "Мик систем")
			
			if window_name_split[1] == "xml":
				Tools.load_page_url(self, "XML")
			
			elif window_name_split[1] == "loan account":
				Tools.load_page_url(self, "Зээлийн данс")
			
			elif window_name_split[1] == "add account":
				Tools.load_page_url(self, "Данс нэмэх")
			
			elif window_name_split[1] == "repayment plan":
				Tools.load_page_url(self, "Эргэн төлөлтийн хуваарь")
			
			elif window_name_split[1] == "fee income":
				Tools.load_page_url(self, "Шимтгэлийн орлого")
		
		elif window_name_split[1] == "document":
			Tools.load_page_url(self, "Бичиг баримт")
			if window_name_split[0] == "etc":
				Tools.load_page_url(self, "Бичиг баримт засварлах")
		
	def load_page_url(self, *args):
		
		driver = self.driver
		for window_name in args:
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((By.LINK_TEXT, u"{}".format(window_name))))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.LINK_TEXT, u"{}".format(window_name))))
			driver.find_element_by_link_text(u"{}".format(window_name)).click()

	def refresh_page(self):
		
		driver = self.driver
		driver.refresh()
	
	def check_page_loaded(self, panel_title):
		
		driver = self.driver
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '{}')]".format(panel_title))))
	
	def multi_window_inquiry(self, window_name, account_type, value):
		
		driver = self.driver
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((By.CLASS_NAME, "selection")))
		Tools.button_click(self, driver.find_element_by_xpath("//span[@role='combobox']"), "none", "", By.XPATH)
		ActionChains(driver).send_keys(value).perform()
		ActionChains(driver).send_keys(Keys.ENTER).perform()
		Tools.fill_account_number(self, window_name, account_type)
	
	def multi_window_request(self, value):
		
		driver = self.driver
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((By.CLASS_NAME, "selection")))
		Tools.button_click(self, driver.find_element_by_xpath("//span[@role='combobox']"), "none", "", By.XPATH)
		Tools.button_click(self, driver.find_element_by_xpath("//span[@title=' Бүгд ']"), "none", "", By.XPATH)
		ActionChains(driver).send_keys(value).perform()
		ActionChains(driver).send_keys(Keys.ENTER).perform()
		Tools.button_click(self, '//button[text()=" Шинэчлэх "]', "click", "", By.XPATH)
	
	def button_click(self, element, type, value, locater):
		
		driver = self.driver
		if type == "none":

			actions = ActionChains(self.driver)
			actions.move_to_element(element).click().perform()
		
		elif type == "enter":
			
			actions = ActionChains(self.driver)
			actions.move_to_element(element).click().perform()
			actions.move_to_element(element).send_keys(Keys.ENTER).perform()
		
		elif type == "input_enter":
			
			actions = ActionChains(self.driver)
			actions.move_to_element(element).click().perform()
			actions.move_to_element(element).send_keys("{}".format(value)).perform()
			ActionChains(driver).send_keys(Keys.ENTER).perform()

		elif type == "input_enter_value":
			
			actions = ActionChains(self.driver)
			actions.move_to_element(element).click().perform()
			ActionChains(driver).send_keys("{}".format(value)).perform()
			ActionChains(driver).send_keys(Keys.ENTER).perform()

		elif element == "input_placeholder":

			WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="{}"]'.format(type)))) 
			WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="{}"]'.format(type)))) 
			actions = ActionChains(self.driver)
			actions.move_to_element(driver.find_element_by_xpath('//input[@placeholder="{}"]'.format(type))).click().perform()
			ActionChains(driver).send_keys("{}".format(value)).perform()

		elif element == "input_placeholder_click":

			WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="{}"]'.format(type)))) 
			WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="{}"]'.format(type)))) 
			driver.find_element_by_xpath('//input[@placeholder="{}"]'.format(type)).click()
		
		elif element == "class_name":
			
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((By.CLASS_NAME, "{}".format(type))))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CLASS_NAME, "{}".format(type))))
			driver.find_element_by_class_name("{}".format(type)).click()

		elif element == "id":
			
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((By.ID, "{}".format(type))))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.ID, "{}".format(type))))
			driver.find_element_by_id("{}".format(type)).click()		

		elif element == "class_name_0":
			
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((By.CLASS_NAME, "{}".format(type))))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CLASS_NAME, "{}".format(type))))
			driver.execute_script("document.getElementsByClassName('btn')[0].click()")
		
		elif element == "contains":

			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '{}')]".format(type))))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '{}')]".format(type))))
			actions = ActionChains(self.driver)
			element = driver.find_element_by_xpath("//*[contains(text(), '{}')]".format(type))
			actions.move_to_element(element).click().perform()

		else:
			if type != "nowait_click":
				WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((locater, "{}".format(element))))
				WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((locater, "{}".format(element))))
			if type == "click" or type == "nowait_click":
				element = driver.find_element(locater,"{}".format(element))
				actions = ActionChains(self.driver)
				actions.move_to_element(element)
				actions.move_to_element(element).click().perform()
			elif type == "move" or type == "nowait_click":
				element = driver.find_element(locater,"{}".format(element))
				actions = ActionChains(self.driver)
				actions.move_to_element(element)
			elif type == "click_elements":
				element = driver.find_elements(locater,"{}".format(element))[int(value)]
				actions = ActionChains(self.driver)
				actions.move_to_element(element)
				actions.move_to_element(element).click().perform()
			elif type == "clear":
				driver.find_element_by_xpath("{}".format(element)).clear()
			elif type =="send_keys":
				element = driver.find_element(locater,"{}".format(element))
				actions = ActionChains(self.driver)
				actions.move_to_element(element)
				actions.move_to_element(element).click().perform()
				actions.move_to_element(element).send_keys(value).perform()
			elif type =="send_keys_action":
				element = driver.find_element(locater,"{}".format(element))
				actions = ActionChains(self.driver)
				actions.move_to_element(element)
				actions.move_to_element(element).click().perform()
				ActionChains(driver).send_keys("{}".format(value)).perform()
				ActionChains(driver).send_keys(Keys.ENTER).perform()
		
	def take_screenshot(self, class_name, window_name, take):
		
		driver = self.driver
		
		account_number = ""
		window_name_split = window_name.split("-")
		
		if window_name == "20450" or window_name == "20400":

			while True:
				if window_name == "20450":
					Tools.button_click(self, "body > app-root > app-main > div > div > div > div.content > lib-general-account > div.dialog-body > div > div:nth-child(1) > input", "click", "", By.CSS_SELECTOR)
					account_number = driver.execute_script("""return document.querySelector("body > app-root > app-main > div > div > div > div.content > lib-general-account > div.dialog-body > div > div:nth-child(1) > input").value""")
				elif window_name == "20400":
					WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"], poll_frequency=1).until(EC.presence_of_element_located((By.CLASS_NAME, "form-control.input-xs")))
					account_number = driver.execute_script("""return document.querySelector('input[class="form-control input-xs"]').value""")
				if account_number == consts.ACCOUNTS[global_account_type]:
					break
				time.sleep(1)
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"], poll_frequency=1).until(EC.presence_of_element_located((By.CLASS_NAME, "{}".format(class_name))))
		
		elif window_name == "10440" or window_name == "10450" or window_name == "13000" or window_name_split[0] == "10400":
			Task.all_tasks(self, "approved-loan_inquiry")
			while True:
				if window_name == "10450":
					WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"], poll_frequency=1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#loan-repayment-history > div.panel.panel-flat > div.panel-body > div > div:nth-child(1) > input")))
					account_number = driver.find_element_by_css_selector("#loan-repayment-history > div.panel.panel-flat > div.panel-body > div > div:nth-child(1) > input").get_attribute("value")
				else:
					WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"], poll_frequency=1).until(EC.presence_of_element_located((By.CLASS_NAME, "form-control.input-xs")))
					account_number = driver.execute_script("""return document.querySelector('input[class="form-control input-xs"]').value""")
				if account_number == consts.ACCOUNTS[global_account_type]:
					break

		else:

			if window_name == "60450":
				Task.all_tasks(self, "approved-customer_inquiry")
				if window_name == "60450":
					WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"], poll_frequency=1).until(EC.presence_of_element_located((By.ID, "{}".format("tab160450-1"))))
			
			elif window_name_split[0] == "400" or window_name == "450" or window_name_split[0] == "10400" or window_name_split[0] == "440":
				Task.all_tasks(self, "approved-inquiry")
				while True:
					if window_name_split[0] == "400" or window_name_split[0] == "10400":
						WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"], poll_frequency=1).until(EC.presence_of_element_located((By.CLASS_NAME, "form-control.input-xs")))
						account_number = driver.execute_script("""return document.querySelector('input[class="form-control input-xs"]').value""")	

					elif window_name == "450":			
						WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"], poll_frequency=1).until(EC.presence_of_element_located((By.CLASS_NAME, "{}".format(class_name))))
						account_number = driver.execute_script("""return document.querySelector('input[placeholder="Дансны №:"]').value""")
					
					elif window_name == "440":
						WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"], poll_frequency=1).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#tab3 > lib-customer-more-inquiry > div > div:nth-child(1) > div.col-xs-8 > fieldset > div:nth-child(1) > div.col-xs-4 > input")))
						account_number = driver.execute_script("""return document.querySelector('input[class="form-control input-xs "]').value""")
					
					if account_number == consts.ACCOUNTS[global_account_type]:
						break
		
		if take:			
			with open('{}{}.png'.format(consts.DATA["SCREENSHOT_PATH"], window_name), 'wb') as file:
				elements = driver.find_elements_by_class_name('{}'.format(class_name))

				if len(elements) == 1:					
					file.write(driver.find_elements_by_class_name('{}'.format(class_name))[0].screenshot_as_png)
				
				elif len(elements) > 1:					
					file.write(driver.find_elements_by_class_name('{}'.format(class_name))[-1].screenshot_as_png)
	
	def take_screenshot_by_tag_name(self, id_name, name, take):
		
		driver = self.driver
		if take:
			with open('{}{}.png'.format(consts.DATA["SCREENSHOT_PATH"], name), 'wb') as file:
				file.write(driver.find_element_by_tag_name('{}'.format(id_name)).screenshot_as_png)
	
	def take_screenshot_by_class_name(self, class_name, name, take):
		
		driver = self.driver

		if name == "limited_statement":			
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"], poll_frequency=1).until(EC.presence_of_element_located((By.CLASS_NAME, "{}".format(class_name))))
			with open('{}{}.png'.format(consts.DATA["SCREENSHOT_PATH"], name), 'wb') as file:
				file.write(driver.find_elements_by_class_name('{}'.format(class_name))[0].screenshot_as_png)
		if name == "allowanceResult":			
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"], poll_frequency=1).until(EC.presence_of_element_located((By.CLASS_NAME, "{}".format(class_name))))
			with open('{}{}.png'.format(consts.DATA["SCREENSHOT_PATH"], name), 'wb') as file:
				file.write(driver.find_elements_by_class_name('{}'.format(class_name))[0].screenshot_as_png)
		if name == "unsuccessfull":			
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"], poll_frequency=1).until(EC.presence_of_element_located((By.CLASS_NAME, "{}".format(class_name))))
			with open('{}{}.png'.format(consts.DATA["SCREENSHOT_PATH"], name), 'wb') as file:
				file.write(driver.find_elements_by_class_name('{}'.format(class_name))[0].screenshot_as_png)
		
		if name == "dispitcher_report":			
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"], poll_frequency=1).until(EC.presence_of_element_located((By.CLASS_NAME, "{}".format(class_name))))
			with open('{}{}.png'.format(consts.DATA["SCREENSHOT_PATH"], name), 'wb') as file:
				file.write(driver.find_elements_by_class_name('{}'.format(class_name))[0].screenshot_as_png)
		
		else:
			
			if take:				
				WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"], poll_frequency=1).until(EC.presence_of_element_located((By.CLASS_NAME, "{}".format(class_name))))
				with open('{}{}.png'.format(consts.DATA["SCREENSHOT_PATH"], name), 'wb') as file:
					elements = driver.find_elements_by_class_name('{}'.format(class_name))
					if len(elements) == 1:						
						file.write(driver.find_elements_by_class_name('{}'.format(class_name))[0].screenshot_as_png)
					
					elif len(elements) > 1:						
						file.write(driver.find_elements_by_class_name('{}'.format(class_name))[-1].screenshot_as_png)
	
	def fill_account_number(self, window_name, account_type):
		
		driver = self.driver
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"], poll_frequency=1).until(EC.presence_of_element_located((By.ID, u"{}".format(window_name))))
		driver.find_element_by_id('{}f'.format(window_name)).clear()
		driver.find_element_by_id('{}f'.format(window_name)).send_keys(consts.ACCOUNTS[account_type])
		Tools.button_click(self, "//input[@value='{}']".format(window_name), "click", "", By.XPATH)
		driver.execute_script("document.getElementById('{}').lastChild.querySelector('.icon-search4').click();".format(window_name))
		global global_account_type
		global_account_type = account_type
	
	def close_ui_dialog(self):
		
		driver = self.driver
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"], poll_frequency=1).until(EC.presence_of_element_located((By.CLASS_NAME, "ui-dialog")))
		divLenght = driver.execute_script("return document.getElementsByClassName('ui-dialog').length")
		driver.execute_script("document.getElementsByClassName('ui-dialog')[{}-1].querySelector('[title={}]').click()".format(divLenght,"Close"))
	
	def close_all_ui_dialog(self, number):
		
		driver = self.driver
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"], poll_frequency=1).until(EC.presence_of_element_located((By.CLASS_NAME, "ui-dialog")))
		driver.execute_script("document.getElementsByClassName('ui-dialog')[{}].querySelector('[title={}]').click()".format(number,"Close"))
		time.sleep(1)
	
	def calculate_bill_and_fill(self, path, type, amount, second_amount, currency):
		
		devsgertuud = consts.BILLS
		driver = self.driver
		zadargaa = {}
		assert currency in devsgertuud, "ZUV BICHNE UU"
		for devsgert in devsgertuud[currency]:
			if devsgert != 0.1 or devsgert != 0.01:
				mlt = int(amount / devsgert)
				amount = amount - mlt * devsgert
			if devsgert == 0.1 and second_amount[0] != "0": 
				mlt = int(int(second_amount) / 10)
				second_amount = "0" + second_amount[1]
				print("mlt : " + str(mlt))
			if devsgert == 0.01 and second_amount[0] == "0":
				mlt = int(int(second_amount) / 1)
				second_amount = int(second_amount) - mlt * 1
				print("mlt : " + str(mlt))
			zadargaa.update({
				devsgert: mlt
			})
		devsgert_count = list(zadargaa.values())
		
		if type == "outcome":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), ' Зарлагадах дэвсгэртийн мэдээлэл ')]")))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), ' Зарлагадах дэвсгэртийн мэдээлэл ')]")))
			for mlt in range(len(devsgert_count)):
				cell = '/html/body/app-root/app-main/div/div/div/div[3]/{}/lib-cash-registry/div/div/div/div[2]/div/table/tbody/tr[{}]/td[6]/lib-masked-input/input'.format(path, mlt + 1)
				driver.find_element_by_xpath(cell).clear()
				driver.find_element_by_xpath(cell).send_keys(devsgert_count[mlt])
				time.sleep(0.1)
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
			time.sleep(2)
			driver.execute_script('document.querySelector("body > app-root > app-main > div > div > div > div.content > {} > lib-cash-registry > div > div > div > div.modal-header > div:nth-child(3) > div:nth-child(3) > div > button:nth-child(2)").click()'.format(path))
		
		elif type == "income":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Орлогодох дэвсгэртийн мэдээлэл ')]")))
			for mlt in range(len(devsgert_count)):
				cell = '/html/body/app-root/app-main/div/div/div/div[3]/{}/lib-cash-registry/div/div/div/div[2]/div/table/tbody/tr[{}]/td[4]/lib-masked-input/input'.format(path, mlt + 1)
				driver.find_element_by_xpath(cell).clear()
				driver.find_element_by_xpath(cell).send_keys(devsgert_count[mlt])
				time.sleep(0.1)
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
			time.sleep(2)
			driver.execute_script('document.querySelector("body > app-root > app-main > div > div > div > div.content > {} > lib-cash-registry > div > div > div > div.modal-header > div:nth-child(3) > div:nth-child(3) > div > button:nth-child(2)").click()'.format(path))

class Notification:
	
	def task(self, transaction_type):
		global success_messages
		driver = self.driver

		transaction_type_split = transaction_type.split(' ')
		if len(transaction_type_split) == 1:
			if (transaction_type_split[0] == "correction"):
				success_messages = "АмжилттайЗалруулга амжилттай хийгдлээ."
			
		else:
			if (transaction_type_split[1] == "transaction"):
				if (transaction_type_split[0] == "income"):
					success_messages = "АмжилттайОрлого амжилттай боллоо."
				elif (transaction_type_split[0] == "transfer" or transaction_type_split[0] == "tax"):
					success_messages = "АмжилттайШилжүүлэг амжилттай боллоо."
				elif (transaction_type_split[0] == "outcome"):
					success_messages = "АмжилттайЗарлага амжилттай хийгдлээ."
				elif (transaction_type_split[0] == "close"):
					success_messages = "АмжилттайДанс амжилттай хаагдлаа."
			elif (transaction_type_split[1] == "task"):
				if (transaction_type_split[0] == "create"):
					success_messages = "АмжилттайАжлыг амжилттай нэмлээ."
				elif (transaction_type_split[0] == "create-organization"):
					success_messages = "АмжилттайАжлыг амжилттай нэмлээ."
				elif (transaction_type_split[0] == "approve"):
					success_messages = "АмжилттайБаталгаажуулах үйлдлийг амжилттай хийлээ."
				elif (transaction_type_split[0] == "decline"):
					success_messages = "АмжилттайЦуцлах үйлдлийг амжилттай хийлээ."
			elif (transaction_type_split[1] == "card"):
				if (transaction_type_split[0] == "order"):
					success_messages = "АмжилттайАмжилттай карт захиаллаа"
				elif (transaction_type_split[0] == "reissue" or transaction_type_split[0] == "renewal" ):
					success_messages = "АмжилттайАмжилттай захиалагдлаа"
				elif (transaction_type_split[0] == "close"):
					success_messages = "АмжилттайКарт амжилттай хаалаа"
				elif (transaction_type_split[0] == "change-limit"):
					success_messages = "АмжилттайАмжилттай сольсон"
			elif (transaction_type_split[1] == "settings"):
				if (transaction_type_split[0] == "save"):
					success_messages = "АмжилттайАжлыг амжилттай нэмлээ."
			elif (transaction_type_split[1] == "approve"):
				if (transaction_type_split[0] == "addsupervisor"):
					success_messages = "АмжилттайАлбан тушаал амжилттай нэмэгдлээ!"
			elif (transaction_type_split[1] == "supervisor"):
				if (transaction_type_split[0] == "edit"):
					success_messages = "АмжилттайАлбан тушаал амжилттай шинэчлэгдлээ!"
			elif (transaction_type_split[1] == "selectedsupervisor"):
				if (transaction_type_split[0] == "delete"):
					success_messages = "Албан тушаал амжилттай устгагдлаа."
			elif (transaction_type_split[1] == "success"):
				if (transaction_type_split[0] == "loan"):
					success_messages = "АмжилттайЗээлийн гэрээний хүсэлт амжилттай явууллаа"
			elif (transaction_type_split[1] == "dispitcher"):
				if (transaction_type_split[0] == "add"):
					success_messages = "Автомат гүйлгээний мэдээллийг амжилттай хадгаллаа"
			
			if (transaction_type_split[0] == "create"):
				if (transaction_type_split[1] == "generalNotif"):
					success_messages = "АмжилттайШинэ гэрээ амжилттай бүртгэгдлээ"
				elif (transaction_type_split[1] == "specialNotif"):
					success_messages = "АмжилттайШинэ гэрээ амжилттай бүртгэгдлээ"
				elif (transaction_type_split[1] == "paytransferNotif"):
					success_messages = "АмжилттайШинэ гэрээ амжилттай бүртгэгдлээ"

			elif transaction_type == "transfer loan":
				success_messages = "АмжилттайШилжүүлэг амжилттай боллоо."
			elif transaction_type == "currency exchange":
				success_messages = "АмжилттайГүйлгээ амжилттай хийгдлээ."
			elif transaction_type_split[1] == "menu":
				if transaction_type_split[0] == "add":
					success_messages = "АмжилттайНэмэгдсэн"
				elif transaction_type_split[0] == "delete":
					success_messages = "АмжилттайУстгагдсан"
				elif transaction_type_split[0] == "update":
					success_messages = "АмжилттайЗасагдсан"
			elif transaction_type_split[1] == "user":
				if transaction_type_split[0] == "add":
					success_messages = "АмжилттайНэмэгдсэн"
				elif transaction_type_split[0] == "delete":
					success_messages = "АмжилттайУстгагдсан"
				elif transaction_type_split[0] == "update":
					success_messages = "Амжилттай зассанШинэчилсэн"
			elif transaction_type_split[1] == "group":
				if transaction_type_split[0] == "add":
					success_messages = "АмжилттайЭрх шинээр нэмэгдсэн"
				elif transaction_type_split[0] == "delete":
					success_messages = "АмжилттайУстгагдсан"
				elif transaction_type_split[0] == "update":
					success_messages = "Амжилттай зассанАмжилттай шинэчилсэн"
			elif transaction_type_split[1] == "module":
				if transaction_type_split[0] == "add":
					success_messages = "АмжилттайНэмэгдсэн"
				elif transaction_type_split[0] == "delete":
					success_messages = "АмжилттайУстгагдсан"
				elif transaction_type_split[0] == "update":
					success_messages = "Амжилттай зассанШинэчилсэн"
			elif transaction_type_split[1] == "product":
				if transaction_type_split[0] == "add":
					success_messages = "АмжилттайНэмэгдсэн"
				elif transaction_type_split[0] == "delete":
					success_messages = "АмжилттайУстгагдсан"
				elif transaction_type_split[0] == "update":
					success_messages = "Амжилттай зассанШинэчилсэн"
			elif transaction_type_split[1] == "endpoint":
				if transaction_type_split[0] == "add":
					success_messages = "АмжилттайНэмэгдсэн"
				elif transaction_type_split[0] == "delete":
					success_messages = "АмжилттайУстгагдсан"
				elif transaction_type_split[0] == "update":
					success_messages = "Амжилттай зассанШинэчилсэн"
			elif transaction_type == "add endpoint":
				success_messages = "АмжилттайНэмэгдсэн"
			elif transaction_type == 'edit endpoint':
				success_messages = 'Амжилттай зассанШинэчилсэн'
			elif transaction_type == 'change status':
				ACCESS = {
					"link": {
						"name": "editedTestName",
					}
				}
				success_messages = "{} амжилттай унтарсанАмжилттай унтарсан".format(ACCESS['link']['name'])
			elif transaction_type == 'delete endpoint':
				success_messages = "АмжилттайУстгагдсан"
			elif transaction_type == "add branch":
				success_messages = "АмжилттайАмжилттай нэмэгдлээ."
			elif transaction_type == "add xml":
				success_messages = "АмжилттайАмжилттай нэмлээ"
			elif transaction_type == "edit branch":
				success_messages = 'АмжилттайАмжилттай заслаа.'
			elif transaction_type == "delete_branch":
				success_messages = 'Салбар тооцооны төвАмжилттай устгагдлаа.'
			elif transaction_type_split[0] == "edit-document":
				if transaction_type_split[1] == "add-group": # "edit-document add-group"
					success_messages = "АмжилттайБүлэг амжилттай нэмлээ."
				elif transaction_type_split[1] == "edit-group":
					success_messages = "АмжилттайБүлэг амжилттай заслаа."
				elif transaction_type_split[1] == "add-document":
					success_messages = "АмжилттайБичиг баримт амжилттай нэмлээ."
				elif transaction_type_split[1] == "edit-document":
					success_messages = "АмжилттайБичиг баримт амжилттай заслаа."
				elif transaction_type_split[1] == "add-source":
					success_messages = "АмжилттайСурвалж амжилттай нэмлээ."
				elif transaction_type_split[1] == "delete-source":
					success_messages = "АмжилттайСурвалж амжилттай устгалаа."
				elif transaction_type_split[1] == "add-field":
					success_messages = "АмжилттайНэмэлт талбар амжилттай хадгалагдлаа."
				elif transaction_type_split[1] == "edit-field":
					success_messages = "АмжилттайНэмэлт талбар амжилттай засагдлаа."
				elif transaction_type_split[1] == "delete-field":
					success_messages =  "АмжилттайНэмэлт талбар амжилттай устгагдлаа."
				elif transaction_type_split[1] == "change-order":
					success_messages = "АмжилттайШаардагдах утгын дарааллыг амжилттай хадгаллаа."
				elif transaction_type_split[1] == "document-inputs":
					success_messages = "АмжилттайНэмэлт талбарыг амжилттай заслаа."
				elif transaction_type_split[1] == "edit-html":
					success_messages = "АмжилттайБичиг баримт амжилттай заслаа."
				elif transaction_type_split[1] == "add-related-form":
					success_messages = "АмжилттайДагах бичиг баримтуудыг амжилттай хадгаллаа."
				elif transaction_type_split[1] == "change-configs":
					success_messages = "АмжилттайБичиг баримтын тохиргоо амжилттай хадгалагдлаа."
			elif transaction_type == "nostro success":
				success_messages = "АмжилттайАмжилттай баталгаажууллаа"
				success_messages = "АмжилттайАмжилттай хадгаллаа"

			elif transaction_type == "mikSystem xml add-information":
				success_messages = "АмжилттайАмжилттай нэмлээ"
			
			elif transaction_type == "mikSystem loanAccount delete-loan-account":
				success_messages = "АмжилттайАмжилттай устгалаа"

			elif transaction_type == "mikSystem addAccount deleteAccount":
				success_messages = "АмжилттайАмжилттай устгалаа"
					
			elif transaction_type == "order card":
				success_messages = "АмжилттайАмжилттай карт захиаллаа"

			elif transaction_type == "mikSystem fee income":
				success_messages = "АнхааруулгаФайл олдсонгүй"
			#######conusmer loan -д ашиглагдана.########
			elif transaction_type == "null cif loanhistory":
				success_messages = "АнхаарХоосон утга оруулсан байна?"

			elif transaction_type == "null cif customer":
				success_messages = "АнхаарХоосон утга оруулсан байна"

			elif transaction_type == "string value":
				success_messages = "АлдааХяналтын орон шалгахад алдаа гарлаа!"

			elif transaction_type == "number value":
				success_messages = "АлдааХяналтын орон таарсангүй"
			
			elif transaction_type == "empty register":
				success_messages = "АмжилтгүйХарилцагчийн регистер олдсонгүй"

			elif transaction_type == "no checkdigit cif":
				success_messages = "АлдааХяналтын орон таарсангүй"

			elif transaction_type == "no customer cif":
				success_messages = "АмжилтгүйХарилцагч олдсонгүй!"

		
			###########################################


		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.CLASS_NAME, "ui-pnotify")))
		notification_msg = ""
		while True:
			notification_msg = driver.execute_script('return document.querySelector(".ui-pnotify").textContent')
			print(notification_msg)
			if notification_msg != "":
				break
			time.sleep(1)
		print("notification_msg: " + str(notification_msg) + '\nmessage:' + str(success_messages))
		assert (notification_msg == success_messages), notification_msg


class Task:
	
	def all_tasks(self, task_type):
		
		driver = self.driver
		task_type_split = task_type.split('-')
		if (task_type_split[0] == "create"):
			
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Регистрийн дугаар оруулна уу']")))
			driver.execute_script("document.querySelector('#modal_form_vertical > div > div > div.modal-header > button').click()")
			Tools.button_click(self, "#senior-teller > div > div", "click", "", By.CSS_SELECTOR)
			# Tools.button_click(self, "btn.btn-default.btn-link", "click_elements", "1", By.CLASS_NAME)
			while True:

				WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"], poll_frequency=1).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Регистрийн дугаар']")))
				register_no = driver.execute_script("""return document.querySelector('input[placeholder="Регистрийн дугаар"]').value""")
				element = driver.find_element_by_xpath("//input[@placeholder='Регистрийн дугаар']")
				if register_no == consts.DATA["REGISTER_NO"]:
					
					break
				elif element.is_enabled():
					
					driver.find_element_by_xpath("//input[@placeholder='Регистрийн дугаар']").send_keys(consts.DATA["REGISTER_NO"])
					break
				time.sleep(1)

			Tools.button_click(self, "//*[contains(text(), ' Хүсэлт илгээх ')]", "click", "", By.XPATH)
			Task.wait_responsibility_group_task(self)
			Tools.button_click(self, "//*[contains(text(), 'Хадгалах ')]", "click", "", By.XPATH)
		
		elif (task_type_split[0] == "create organization"):
			
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Регистрийн дугаар оруулна уу']")))
			driver.execute_script("document.querySelector('#modal_form_vertical > div > div > div.modal-header > button').click()")
			Tools.button_click(self, "contains", "БҮАА Зөвшөөрөл", "", By.XPATH)
			
			while True:
				
				WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"], poll_frequency=1).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Регистрийн дугаар']")))
				register_no = driver.execute_script("""return document.querySelector('input[placeholder="Регистрийн дугаар"]').value""")
				element = driver.find_element_by_xpath("//input[@placeholder='Регистрийн дугаар']")
				time.sleep(1)
				
				if register_no == consts.DATA["ORGANIZATION_NO"]:
					
					break
				
				elif element.is_enabled():
					
					driver.find_element_by_xpath("//input[@placeholder='Регистрийн дугаар']").send_keys(consts.DATA["ORGANIZATION_NO"])
					break
			
			Tools.button_click(self, "contains", " Хүсэлт илгээх ", "", By.XPATH)
			#WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//span[@title=' БҮА Ахлах ']")))
			Task.wait_responsibility_group_task(self)
			Tools.button_click(self, "//*[contains(text(), 'Хадгалах ')]", "click", "", By.XPATH)
		
		elif (task_type_split[0] == "task"):
			
			task_number = task_name.split('-')[1]
			LoginsClass.logout(self)
			LoginsClass.login_BUAA(self)
			Tools.load_page_url(self, "Таск", "Багт хувиарлагдсан ажлууд")
			print(task_number)
			WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '#{}'.format(task_number))))
			WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, '#{}'.format(task_number))))
			driver.find_element_by_link_text('#{}'.format(task_number)).click()
			#WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//span[@title=' БҮА Ахлах ']")))
			Task.wait_responsibility_group_task(self)
			
			if task_type_split[1] == "approve":
				
				Tools.button_click(self, "contains", "Баталгаажуулах ", "", By.XPATH)
				Tools.button_click(self, "contains", " Үйлдлийг хийх ", "", By.XPATH)
			
			elif task_type_split[1] == "decline":
				
				driver.find_element_by_xpath("//*[contains(text(), 'Цуцлах ')]").click()
				Tools.button_click(self, "contains", " Үйлдлийг хийх ", "", By.XPATH)
		
		elif task_type_split[0] == "approved":
			
			task_number = task_name.split("-")[-1]
			print(task_number)
			Tools.load_page_url(self, "Таск", "Миний үүсгэсэн ажлууд")
			WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, '#{}'.format(task_number))))
			driver.find_element_by_link_text('#{}'.format(task_number)).click()
			# WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//span[@title=' БҮА Ахлах ']")))
			Task.wait_responsibility_group_task(self)
			
			if (task_type_split[1] == "transaction" or task_type_split[1] == "tax"):				
				Tools.load_page_url(self, 'Гүйлгээ хийх')								 							
														
			elif (task_type_split[1] == "correction"):
				Tools.load_page_url(self, 'Залруулга хийх')
				Tools.button_click(self, '//button[text()=" Залруулах "]', "click", "", By.XPATH)
			
			elif (task_type_split[1] == "document"):				
				driver.find_element_by_link_text('Гэрээ, маягт бэлтгэх').click()
			elif (task_type_split[1] == "document"):
				Tools.load_page_url(self, 'Гэрээ, маягт бэлтгэх')

			elif (task_type_split[1] == "definitionDeposit"):				
				Tools.load_page_url(self, 'Депозит дансны тодорхойлолт бэлтгэх')

			elif (task_type_split[1] == "definitionLoan"):
				Tools.load_page_url(self, 'Зээлийн дансны тодорхойлолт бэлтгэх')
			
			elif (task_type_split[1] == "embassyKorea"):				
				driver.find_element_by_link_text('БНСУ тодорхойлолт бэлтгэх').click()
			
			elif (task_type_split[1] == "tax"):				
				driver.find_element_by_link_text('Гүйлгээ хийх').click()
			
			elif (task_type_split[1] == "embassyKorea"):
				Tools.load_page_url(self, 'БНСУ тодорхойлолт бэлтгэх')
			
			elif (task_type_split[1] == "statement"):
				Tools.load_page_url(self, 'Депозит дансны хуулга бэлтгэх')
					
			elif (task_type_split[1] == "loan_statement"):
				Tools.load_page_url(self, 'Зээлийн дансны хуулга бэлтгэх')
			
			elif (task_type_split[1] == "inquiry"):
				Tools.load_page_url(self, 'Депозит дансны лавлагаа авах')
			
			elif (task_type_split[1] == "loan_inquiry"):
				Tools.load_page_url(self, 'Зээлийн дансны лавлагаа авах')
			
			elif (task_type_split[1] == "account_balance_guarantee"):
				Tools.load_page_url(self, 'Дансны үлдэгдлийн баталгаа')

			elif (task_type_split[1] == "customer_inquiry"):
				Tools.load_page_url(self, 'Харилцагчийн лавлагаа авах')
		
		else:			
			return False
			
	def wait_responsibility_group_task(self):
		for x in range(10):
			title = ""
			try:
				title = driver.execute_script("""return document.querySelector("body > app-root > app-main > div > div > div > div.content > task-manage > div > div > div.col-lg-9 > div > div.panel-body.pt-10 > form > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div > lib-select > div > span > span.selection > span").textContent""")
			except Exception:
				print("error")
			if title == " БҮА Ахлах " or title == " Senior relationship manager ":
				break
			time.sleep(1)

	
	def get_task_number(self):
		
		driver = self.driver
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, "//i[@class='icon-info22 text-info cursor-pointer position-right']")))
		global task_name
		task_name = driver.execute_script("return document.getElementsByClassName('icon-info22 text-info cursor-pointer position-right')[0].getAttribute('id')")
	
	def do_correction(self, window_name):
		driver = self.driver
		Task.all_tasks(self, "approved-correction")	
		if window_name == "1060" or window_name == "20060":			
			Tools.calculate_bill_and_fill(self, "lib-cash-correction", "{}".format("income"), consts.DATA["AMOUNT"], "00","MNT")
		
		elif (window_name == "3060"):			
			Tools.calculate_bill_and_fill(self, "lib-cash-correction", "{}".format("income"), DISCOUNT_AMOUNT, "00", "MNT")
		
		elif window_name == "1010" or window_name == "20010":			
			Tools.calculate_bill_and_fill(self, "lib-cash-correction", "{}".format("outcome"), consts.DATA["AMOUNT"], "00","MNT")
		
		elif window_name == "21046":
			amount = driver.execute_script("""return document.getElementsByClassName("form-control ng-untouched ng-pristine ng-valid")[2].value.replace(",","")""")
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((By.TAG_NAME, 'table')))
			Tools.calculate_bill_and_fill(self, "lib-cash-correction", "outcome", consts.DATA["EXHANGE_AMOUNT"], "00",  "AUD")
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.TAG_NAME, 'table')))
			Tools.calculate_bill_and_fill(self, "lib-cash-correction", "income", int(amount.split(".")[0]), amount.split(".")[1],  "MNT")
		
		elif window_name == "3045" or window_name == "4045" or window_name == "14045":			
			pass
	
	# Khurelchuluun 06/19 fix
	def close_approved_task_process(self):
		
		""""
		Ahlah BUA-aar uusgesen task-iig batalgaajuulah
		"""
		driver = self.driver
		Task.all_tasks(self, "approved-transaction")
		Tools.button_click(self, "", "button")
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#accounts-panel_filter > label > input[type=search]')))
		driver.find_element_by_css_selector('#accounts-panel_filter > label > input[type=search]').send_keys("5163354301")
		driver.execute_script("document.querySelector('#accounts-panel > tbody:nth-child(2) > tr').click()")
		time.sleep(2)
		driver.find_element_by_xpath('/html/body/app-root/app-main/div/div/div/div[3]/lib-close-account/div/div[1]/form/div/div[2]/div[1]/fieldset/div[1]/div/div[1]/input').send_keys('5429556169')
		time.sleep(1)
		driver.find_element_by_xpath('/html/body/app-root/app-main/div/div/div/div[3]/lib-close-account/div/div[1]/form/div/div[2]/div[1]/fieldset/div[4]/div/input').send_keys(consts.DATA["DESCRIPTION"] + ' ' + date_time)
		time.sleep(1)
		driver.execute_script('document.querySelector("#transaction-panel > div:nth-child(1) > form > div > div.panel-body > div.text-right.mt-10 > button").click()')
		time.sleep(3)
		driver.find_element_by_class_name('close').click()
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CLASS_NAME, 'modal-header')))
		driver.execute_script("document.querySelector('#modal_form_vertical > div > div > div.modal-header > button').click()")
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CLASS_NAME, 'modal-header')))
		driver.execute_script("document.querySelector('#finger-print > div.modal-header > button').click()")

	def task_menus_filter(self, filter_type):

		""""
		Task menu deeh 3n menug shalgah 
		"""
		driver = self.driver	
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="1"]')))
		driver.find_element_by_class_name('select2').click()
		driver.find_element_by_xpath("//input[@role='textbox']").send_keys('Төлөв')
		driver.find_element_by_xpath("//input[@role='textbox']").send_keys(Keys.ENTER)
		driver.find_element_by_xpath("//input[@placeholder='Шүүх утгаа бичнэ үү...']").clear()
		driver.find_element_by_xpath("//input[@placeholder='Шүүх утгаа бичнэ үү...']").send_keys('{}'.format(filter_type))
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="1"]')))
		time.sleep(5)

class Transaction:
	
	# Khurelchuluun 06/19 fix
	def search_transaction_by_description(self):
		driver = self.driver
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//span[@title=' № ']")))
		driver.find_element_by_xpath("//span[@title=' № ']").click()
		driver.find_element_by_xpath("//input[@role='textbox']").send_keys(' Гүйлгээний утга ')
		driver.find_element_by_xpath("//input[@role='textbox']").send_keys(Keys.ENTER)
		driver.find_element_by_xpath("//input[@placeholder='Шүүх утгаа бичнэ үү...']").send_keys(consts.DATA["DESCRIPTION"] + ' ' + date_time)
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='icon-pencil7 text-success-600']")))
		driver.find_element_by_xpath("//i[@class='icon-pencil7 text-success-600']").click()
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn")))
		driver.find_element(By.CLASS_NAME, "btn").click()
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//span[@title=' БҮА Ахлах ']")))
		driver.find_element(By.XPATH, "//*[contains(text(), 'Хадгалах ')]").click()
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, "//i[@class='icon-info22 text-info cursor-pointer position-right']")))
		global task_name
		task_name = driver.execute_script("return document.getElementsByClassName('icon-info22 text-info cursor-pointer position-right')[0].getAttribute('id')")

	def operation(self, type):
			driver = self.driver
			if type == "unsuccessful":
				Tools.button_click(self, '//span[text()=" Амжилттай гүйлгээ "]', "send_keys", " Амжилтгүй гүйлгээ ", By.XPATH)
				ActionChains(driver).send_keys(Keys.ENTER).perform()
				driver.find_element_by_xpath('//button[text()=" Хайх "]').click()

			elif type == "date":
				Tools.button_click(self, '//span[text()=" Амжилттай гүйлгээ "]', "send_keys", " Амжилтгүй гүйлгээ ", By.XPATH)
				ActionChains(driver).send_keys(Keys.ENTER).perform()
				Tools.search_date(self)
				driver.find_element_by_xpath('//button[text()=" Хайх "]').click()

class LoginsClass:
	
	def login(self):
		driver = self.driver
		driver.get(consts.URLS["IMS_URL"] + "/home/login")
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.NAME, 'username')))
		driver.find_element(By.NAME, "username").send_keys(consts.AUTH["USER_NAME"])
		driver.find_element(By.NAME, "password").send_keys(consts.AUTH["USER_PASSWORD"])
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn")))
		driver.find_element(By.CSS_SELECTOR, ".btn").click()
		
	def login_BUAA(self):
		driver = self.driver
		driver.get(consts.URLS["IMS_URL"])
		driver.find_element(By.NAME, "username").send_keys(consts.AUTH["BUAA_USERNAME"])
		driver.find_element(By.NAME, "password").send_keys(consts.AUTH["BUAA_PASSWORD"])
		driver.find_element(By.CSS_SELECTOR, ".btn").click()
	
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

class Transactions:

	def all_transactions(self, transaction_menu, account_type):

		"""All transaction function
		"""
		driver = self.driver

		if (transaction_menu == "1010" or transaction_menu == "20010"):

			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Дансны №"]')))
			driver.find_element_by_xpath('//input[@placeholder="Дансны №"]').clear()
			driver.find_element_by_xpath('//input[@placeholder="Дансны №"]').send_keys(consts.ACCOUNTS["{}".format(account_type)])
			driver.find_element_by_xpath('//input[@placeholder="Орлогын дүн"]').clear()
			driver.find_element_by_xpath('//input[@placeholder="Орлогын дүн"]').send_keys(consts.DATA["AMOUNT"])
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Гүйлгээний утга"]')))
			driver.find_element_by_xpath('//input[@placeholder="Гүйлгээний утга"]').send_keys(consts.DATA["DESCRIPTION"] + ' ' + date_time)
			Tools.button_click(self, '//button[text()=" Орлогодох "]', "click", "", By.XPATH)
			Tools.calculate_bill_and_fill(self,  "{}".format("lib-cash-income"), "income", consts.DATA["AMOUNT"], "00", "MNT")
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CLASS_NAME, 'close')))
			driver.find_element_by_class_name('close').click()
		
		
			

		elif (transaction_menu == "20060"):

			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Зарлагадах данс"]')))
			driver.find_element_by_xpath('//input[@placeholder="Зарлагадах данс"]').clear()
			driver.find_element_by_xpath('//input[@placeholder="Зарлагадах данс"]').send_keys(consts.ACCOUNTS["{}".format(account_type)])
			driver.find_element_by_xpath('//input[@placeholder="Зарлагын дүн"]').clear()
			driver.find_element_by_xpath('//input[@placeholder="Зарлагын дүн"]').send_keys(consts.DATA["AMOUNT"])
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Гүйлгээний утга"]')))
			driver.find_element_by_xpath('//input[@placeholder="Гүйлгээний утга"]').send_keys(consts.DATA["DESCRIPTION"] + ' ' + date_time)
			Tools.button_click(self, '//button[text()=" Зарлагадах "]', "click", "", By.XPATH)
			Tools.calculate_bill_and_fill(self,  "lib-cash-transaction", "outcome", consts.DATA["AMOUNT"], "00", "MNT")
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CLASS_NAME, 'close')))
			driver.find_element_by_class_name('close').click()

		


		else:

			Task.all_tasks(self, "approved-transaction")
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accounts-panel_filter > label > input[type=search]')))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#accounts-panel_filter > label > input[type=search]')))
			if transaction_menu == "1042" or transaction_menu == "1043" or transaction_menu == "1054" or transaction_menu == "4045" or transaction_menu == "14045" :
				driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх данс"]').send_keys(consts.ACCOUNTS['DEPOSIT_ACCOUNT'])
				driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх дүн"]').clear()
				if transaction_menu == "1042":
					driver.find_element_by_class_name('select2-selection').click()
					ActionChains(driver).send_keys(" 320000:").perform()
					ActionChains(driver).send_keys(Keys.RETURN).perform()
					driver.find_element_by_xpath("//input[@placeholder='Хүлээн авах данс']").send_keys(consts.ACCOUNTS[account_type])
					driver.find_element_by_xpath("//input[@placeholder='Хүлээн авагчийн нэр']").send_keys(consts.DATA["RECIPIENT"])
					driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх дүн"]').send_keys(consts.DATA['HIGH_AMOUNT'])
				elif transaction_menu == "1043":
					driver.find_element_by_class_name('select2-selection').click()
					ActionChains(driver).send_keys(" 900000:").perform()
					ActionChains(driver).send_keys(Keys.RETURN).perform()
					driver.find_element_by_xpath('//input[@placeholder="Төрийн сангын данснаас хайх утга"]').send_keys(100010000944)
					Tools.button_click(self, '//button[text()=" Хайх "]', "click", "", By.XPATH)
					WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#fund-panel > tbody > tr')))
					driver.execute_script('document.querySelector("#fund-panel > tbody > tr").click()')
					driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх дүн"]').send_keys(consts.DATA['AMOUNT'])
				elif transaction_menu == "1054":
					WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CLASS_NAME, 'select2-selection')))
					driver.find_element_by_class_name('select2-selection').click()
					ActionChains(driver).send_keys(consts.DATA["RECEIVING_BANK"]).perform()
					ActionChains(driver).send_keys(Keys.RETURN).perform()
					driver.find_element_by_xpath("//input[@placeholder='Хүлээн авах данс']").send_keys(consts.ACCOUNTS[account_type])
					driver.find_element_by_xpath("//input[@placeholder='Хүлээн авагчийн нэр']").send_keys(consts.DATA["RECIPIENT"])
					driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх дүн"]').send_keys(consts.DATA['AMOUNT'])
				elif transaction_menu == "4045" or transaction_menu == "14045":
					for x in range(10):
						getAccountValue = driver.execute_script("""return document.querySelector("#transaction-panel > div:nth-child(1) > form > div > div.panel-body > fieldset > div:nth-child(2) > div > div:nth-child(2) > input").value""")
						if getAccountValue != "":
							break
						time.sleep(1)
					Tools.button_click(self, "input_placeholder", "Хүлээн авах данс", consts.ACCOUNTS[account_type], By.XPATH)
					for x in range(10):
						getAccountValue = driver.execute_script("""return document.querySelector("#receiver-panel > fieldset > div:nth-child(3) > div > div:nth-child(2) > input").value""")
						if getAccountValue != "":
							break
						time.sleep(1)
					Tools.button_click(self, "input_placeholder", "Шилжүүлэх дүн", consts.DATA['AMOUNT'], By.XPATH)
				elif transaction_menu == "1054":
					WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CLASS_NAME, 'select2-selection')))
					driver.find_element_by_class_name('select2-selection').click()
					ActionChains(driver).send_keys(consts.DATA["RECEIVING_BANK"]).perform()
					ActionChains(driver).send_keys(Keys.RETURN).perform()
					driver.find_element_by_xpath("//input[@placeholder='Хүлээн авах данс']").send_keys(consts.ACCOUNTS[account_type])
					driver.find_element_by_xpath("//input[@placeholder='Хүлээн авагчийн нэр']").send_keys(consts.DATA["RECIPIENT"])
					driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх дүн"]').send_keys(consts.DATA['AMOUNT'])

				WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Хүлээн авах дүн"]')))
				Tools.button_click(self, '//input[@placeholder="Хүлээн авах дүн"]', "click", "", By.XPATH)
				driver.find_element_by_xpath("//input[@placeholder='Гүйлгээний утга']").send_keys(consts.DATA["DESCRIPTION"] + ' ' + date_time)
				WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Шилжүүлэх "]')))
				driver.execute_script("""document.querySelector("#transaction-panel > div:nth-child(1) > form > div > div.panel-body > div.text-right.mt-10 > button").click()""")
			

			elif transaction_menu == "11055":
				driver.find_elements_by_xpath("//input[@type='search']")[1].send_keys(consts.ACCOUNTS[account_type])
				Tools.button_click(self, driver.find_element_by_id("accounts-panel_filter"), "enter", "", By.XPATH)
				driver.execute_script('document.querySelector("#accounts-panel > tbody > tr").click()')
				WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Шилжүүлэх дүн"]')))
				WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Хүлээн авах дүн"]')))
				driver.find_element_by_xpath("//input[@placeholder='Хүлээн авах данс']").send_keys(consts.ACCOUNTS['DEPOSIT_ACCOUNT'])
				WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Хүлээн авагчийн нэр"]')))
				WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CLASS_NAME, 'select2-selection')))
				driver.find_element_by_class_name('select2-selection').click()
				ActionChains(driver).send_keys(" NF:Хураамж авахгүй ").perform()
				ActionChains(driver).send_keys(Keys.RETURN).perform()
				driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх дүн"]').clear()
				WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Шилжүүлэх дүн"]')))
				driver.find_element_by_xpath("//input[@placeholder='Гүйлгээний утга']").send_keys(consts.DATA["DESCRIPTION"] + ' ' + date_time)
				driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх дүн"]').clear()
				driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх дүн"]').send_keys(consts.DATA['AMOUNT'])
				driver.find_element_by_xpath('//input[@placeholder="Хүлээн авах дүн"]').click()
				WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Шилжүүлэх "]')))
				driver.find_element_by_xpath('//button[text()=" Шилжүүлэх "]').click()

			elif transaction_menu == "11044":
				driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх данс"]').send_keys(consts.ACCOUNTS['DEPOSIT_ACCOUNT'])
				driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх дүн"]').clear()
				driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх дүн"]').send_keys(consts.DATA['AMOUNT'])
				driver.find_element_by_xpath("//input[@placeholder='Хүлээн авах данс']").send_keys(consts.ACCOUNTS[account_type])
				WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Хүлээн авагчийн нэр"]')))
				driver.find_element_by_xpath("//input[@placeholder='Гүйлгээний утга']").send_keys(consts.DATA["DESCRIPTION"] + ' ' + date_time)
				WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Шилжүүлэх "]')))
				driver.find_element_by_xpath('//button[text()=" Шилжүүлэх "]').click()
				time.sleep(3)



				

			elif transaction_menu == "1345":
				Tools.button_click(self, driver.find_element_by_id("accounts-panel_filter"), "input_enter_value", consts.ACCOUNTS[account_type], By.ID)	
				
				# driver.execute_script("""document.getElementById("accounts-panel_filter").querySelector('input[type="search"]').value = {}""".format(consts.ACCOUNTS[account_type]))
				driver.execute_script('document.querySelector("#accounts-panel > tbody > tr").click()')
				driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх дүн"]').clear()
				driver.find_element_by_xpath("//input[@placeholder='Хүлээн авах данс']").send_keys(consts.ACCOUNTS["DEPOSIT_ACCOUNT"])
				driver.find_element_by_xpath("//input[@placeholder='Хүлээн авагчийн нэр']").send_keys(consts.DATA["RECIPIENT"])
				driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх дүн"]').send_keys(consts.DATA['AMOUNT'])
				driver.find_element_by_xpath('//input[@placeholder="Хүлээн авах дүн"]').click()
				
				driver.find_element_by_xpath("//input[@placeholder='Гүйлгээний утга']").send_keys(consts.DATA["DESCRIPTION"] + ' ' + date_time)
				WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Шилжүүлэх "]')))
				driver.find_element_by_xpath('//button[text()=" Шилжүүлэх "]').click()
			elif transaction_menu == "1360":
				Tools.button_click(self, driver.find_element_by_id("accounts-panel_filter"), "input_enter_value", consts.ACCOUNTS[account_type], By.ID)	
				# driver.execute_script("""document.getElementById("accounts-panel_filter").querySelector('input[type="search"]').value = {}""".format()
				driver.execute_script('document.querySelector("#accounts-panel > tbody > tr").click()')
				driver.find_element_by_xpath('//input[@placeholder="Зарлагын дүн"]').clear()
				driver.find_element_by_xpath('//input[@placeholder="Зарлагын дүн"]').send_keys(consts.DATA['AMOUNT'])
				driver.find_element_by_xpath("//input[@placeholder='Гүйлгээний утга']").send_keys(consts.DATA["DESCRIPTION"] + ' ' + date_time)
				WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Зарлагадах "]')))
				driver.find_element_by_xpath('//button[text()=" Зарлагадах "]').click()
				Tools.calculate_bill_and_fill(self,  "lib-cash-transaction", "outcome", consts.DATA['AMOUNT'], "00",  "MNT")
			elif transaction_menu == "3045" or transaction_menu == "3060":
				driver.find_elements_by_xpath("//input[@type='search']")[1].send_keys(consts.ACCOUNTS[account_type])
				Tools.button_click(self, driver.find_element_by_id("accounts-panel_filter"), "enter", "", By.XPATH)
				driver.execute_script('document.querySelector("#accounts-panel > tbody > tr").click()')
				if transaction_menu == "3045":
					driver.find_element_by_xpath("//input[@placeholder='Гүйлгээний утга']").send_keys(consts.DATA["DESCRIPTION"] + ' ' + date_time)
					driver.find_element_by_xpath('//input[@placeholder="Хүлээн авах данс"]').send_keys(consts.ACCOUNTS['TIME_DEPOSIT_ACCOUNT'])
					Tools.button_click(self, '//button[text()=" Данс хаах "]', "click", "", By.XPATH)
				elif transaction_menu == "3060":
					driver.find_element_by_xpath("//input[@placeholder='Гүйлгээний утга']").send_keys(consts.DATA["DESCRIPTION"] + ' ' + date_time)
					for x in range(10):
						getAmount = int(driver.execute_script("""return document.querySelector('input[placeholder="Зарлагын дүн"]').value""").split('.')[0].replace(',', ''))
						time.sleep(1)
						if getAmount != 0:
							break
					print(getAmount)
					Tools.button_click(self, driver.find_element_by_xpath('//button[text()=" Зарлагадах "]'), "none", "", By.XPATH)
					global DISCOUNT_AMOUNT
					DISCOUNT_AMOUNT = getAmount - 3000
					Tools.calculate_bill_and_fill(self, "lib-cash-transaction", "outcome", DISCOUNT_AMOUNT, "00", "MNT")
			elif transaction_menu == "1060":
				driver.execute_script("""document.getElementById("accounts-panel_filter").querySelector('input[type="search"]').value = {}""".format(consts.ACCOUNTS[account_type]))
				driver.execute_script('document.querySelector("#accounts-panel > tbody > tr").click()')
				driver.find_element_by_xpath('//input[@placeholder="Зарлагын дүн"]').clear()
				driver.find_element_by_xpath('//input[@placeholder="Зарлагын дүн"]').send_keys(consts.DATA['AMOUNT'])
				driver.find_element_by_xpath('//input[@placeholder="Гүйлгээний утга"]').send_keys(consts.DATA["DESCRIPTION"] + ' ' + date_time)
				Tools.button_click(self, '//button[text()=" Зарлагадах "]', "click", "", By.XPATH)
				Tools.calculate_bill_and_fill(self, "lib-cash-transaction",  "outcome", consts.DATA['AMOUNT'], "00", "MNT")
			
			

	def exchange_transactions(self, transaction_menu):
		"""All exchange transaction function
		"""
		driver = self.driver
		in_currency, out_currency = transaction_menu.split("-")
		if out_currency == "MNT":

			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((By.CLASS_NAME, 'select2-selection.select2-selection--single.select-sm')))
			Tools.button_click(self, driver.find_element_by_css_selector("#transaction-panel > div > form > div > div.panel-body > fieldset > div:nth-child(2) > div > div:nth-child(2) > lib-rate > lib-select > div > span > span.selection > span"), "input_enter_value", in_currency, By.CSS_SELECTOR)	
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.ID, 'input')))
			driver.find_element_by_id("input").clear()
			driver.find_element_by_id("input").send_keys(consts.DATA["EXHANGE_AMOUNT"])
			Tools.button_click(self, "input_placeholder", "Гүйлгээний утга", consts.DATA["DESCRIPTION"] + ' ' + date_time, By.XPATH)
			Tools.button_click(self, "contains", "Гүйлгээ хийх", "", By.XPATH)
			amount = driver.execute_script("""return document.querySelector('input[placeholder="Зарах валютын дүн"]').value.replace(",","")""")
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((By.TAG_NAME, 'table')))
			Tools.calculate_bill_and_fill(self, "lib-currency-exchange", "income", consts.DATA["EXHANGE_AMOUNT"], "00",  in_currency)
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.TAG_NAME, 'table')))
			Tools.calculate_bill_and_fill(self, "lib-currency-exchange", "outcome", int(amount.split(".")[0]), amount.split(".")[1],  "MNT")
		else:
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((By.CLASS_NAME, 'select2-selection.select2-selection--single.select-sm')))
			Tools.button_click(self, driver.find_element_by_css_selector("#transaction-panel > div > form > div > div.panel-body > fieldset > div:nth-child(3) > div > div:nth-child(2) > lib-rate > lib-select > div > span > span.selection > span"), "input_enter_value", out_currency, By.CSS_SELECTOR)	
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.ID, 'input')))
			driver.find_element_by_xpath('//input[@placeholder="Зарах валютын дүн"]').clear()
			driver.find_element_by_xpath('//input[@placeholder="Зарах валютын дүн"]').send_keys(consts.DATA["EXHANGE_AMOUNT"])
			Tools.button_click(self, "input_placeholder", "Гүйлгээний утга", consts.DATA["DESCRIPTION"] + ' ' + date_time, By.XPATH)
			Tools.button_click(self, "//*[contains(text(), 'Гүйлгээ хийх')]", "click", "", By.XPATH)
			amount = driver.execute_script("""return document.querySelector('input[placeholder="Авах валютын дүн"]').value.replace(",","")""")
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((By.TAG_NAME, 'table')))
			Tools.calculate_bill_and_fill(self, "lib-currency-exchange", "income", int(amount.split(".")[0]), amount.split(".")[1],  "MNT")
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.TAG_NAME, 'table')))
			Tools.calculate_bill_and_fill(self, "lib-currency-exchange", "outcome", consts.DATA["EXHANGE_AMOUNT"], "00", out_currency)

	# Khurelchuluun 06/19 fix
	def search_transaction_by_description(self):
		driver = self.driver
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((By.XPATH, "//span[@title=' № ']")))
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//span[@title=' № ']")))
		# Tools.button_click(self, "select2-selection.select2-selection--single.select-md", "click", "", By.CLASS_NAME)
		Tools.button_click(self, "//span[@title=' № ']", "click", "", By.XPATH)
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > span > span > span.select2-search.select2-search--dropdown > input')))
		driver.find_element_by_css_selector('body > span > span > span.select2-search.select2-search--dropdown > input').send_keys(' Гүйлгээний утга ')
		driver.find_element_by_xpath("//input[@role='textbox']").send_keys(Keys.ENTER)
		driver.find_element_by_xpath("//input[@placeholder='Шүүх утгаа бичнэ үү...']").send_keys(consts.DATA["DESCRIPTION"] + ' ' + date_time)
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='icon-pencil7 text-success-600']")))
		driver.find_element_by_xpath("//i[@class='icon-pencil7 text-success-600']").click()
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn")))
		driver.find_element(By.CLASS_NAME, "btn").click()
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//span[@title=' БҮА Ахлах ']")))
		Tools.button_click(self, "//*[contains(text(), 'Хадгалах ')]", "click", "", By.XPATH)
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, "//i[@class='icon-info22 text-info cursor-pointer position-right']")))
		global task_name
		task_name = driver.execute_script("return document.getElementsByClassName('icon-info22 text-info cursor-pointer position-right')[0].getAttribute('id')")
