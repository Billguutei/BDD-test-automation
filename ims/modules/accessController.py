# -*- coding: UTF-8 -*
import datetime

from modules.constants import *
from modules.utils import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

date_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
date_time_access = datetime.datetime.now().strftime("%m/%d/%Y")
consts = Constant()

class Access:
	
	def menu(self, menu_type):
		
		driver = self.driver
		
		if menu_type == "add":
			Tools.button_click(self, "class_name_0", "btn", "", By.CLASS_NAME)
			Access.addmenu(self, "test xvrlee", "test xvrlee", "user", "1", "Admin", " Цэс нэмэх ")
		
		if menu_type == "open" or menu_type == "delete" or menu_type == "update":
			
			Access.search(self, "menu_table", "test xvrlee", "")
			Tools.button_click(self, "class_name", "icon-menu9", "", By.XPATH)
			if (menu_type == "open"):
				Tools.button_click(self, "contains", " Харах", "", By.XPATH)
				WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Холбоосын нэр')]")))
			elif (menu_type == "delete"):
				Tools.button_click(self, "contains", " Устгах", "", By.XPATH)
				Tools.button_click(self, "class_name", "icon-menu9", "", By.XPATH)
				Tools.button_click(self, "contains", " Устгах", "", By.XPATH)  # BUG 2 удаа дарж байж Устгах нь болж байна.
				Tools.button_click(self, "contains", " Устгах ", "", By.XPATH)
			elif (menu_type == "update"):
				Tools.button_click(self, "contains", " Шинэчлэх", "", By.XPATH)
				Access.addmenu(self, "test2", "test2", "user", "2", "Admin", " Засах ")  # BUG combobox дээр нь дарагдахгүй байна, мөн засах button дээр дарахаар алдаа гарч байна.
	
	def addmenu(self, name, description, picture, queue_number, url, button_name):
		
		driver = self.driver
		
		if (button_name == " Засах "):

			lenght = 1
			WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#menu_edit_modal > div > div > div.modal-body > div:nth-child(1) > div > div:nth-child(1) > input')))
		
		if (button_name == " Цэс нэмэх "):

			lenght = 0
			WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#menu_modal > div > div > form > div > div:nth-child(1) > div > div:nth-child(1) > input')))
		driver.find_elements_by_xpath('//input[@placeholder="Нэр"]')[lenght].send_keys('{}'.format(name))
		driver.find_elements_by_xpath('//input[@placeholder="Нэмэлт мэдээлэл"]')[lenght].send_keys('{}'.format(description))
		driver.find_elements_by_xpath('//input[@placeholder="Зураг"]')[lenght].send_keys('{}'.format(picture))
		driver.find_elements_by_xpath('//input[@placeholder="Дарааллын дугаар"]')[lenght].send_keys('{}'.format(queue_number))
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((By.CLASS_NAME, "selection")))
		
		if lenght == 0:

			Tools.button_click(self, driver.find_element_by_xpath("//span[@role='combobox']"), "input_enter", url, By.XPATH)

		Tools.button_click(self, '//button[text()="{}"]'.format(button_name), "click", "", By.XPATH)
		Tools.button_click(self, '//button[text()="{}"]'.format(button_name), "click", "", By.XPATH)
	
	def module(self, module_type):
		
		driver = self.driver
		
		if module_type == "add":
			Tools.button_click(self, "class_name_0", "btn", "", By.CLASS_NAME)
			Access.addmodule(self, "test", "test", " Нэмэх ")
		
		if module_type == "search" or module_type == "delete" or module_type == "update":

			if (module_type == "delete"):
				Access.search(self, "module_table", "test2", "")
				Tools.button_click(self, '//i[@class="icon-trash text-danger-600"]', "click", "", By.XPATH)
				Tools.button_click(self, '//i[@class="icon-trash text-danger-600"]', "click", "", By.XPATH)  # BUG 2 удаа дарж байж Устгах нь болж байна.
				Tools.button_click(self, "contains", " Устгах ", "", By.XPATH)
			elif (module_type == "update"):
				Access.search(self, "module_table", "test", "")
				Tools.button_click(self, '//i[@class="icon-pencil7 text-primary-600"]', "click", "", By.XPATH)
				Access.addmodule(self, "test2", "test2", " Засах ")
		
		elif module_type == "search_added":
			
			LoginsClass.login(self)
			Tools.load_page(self, "access-module")
			Tools.check_page_loaded(self, "Нэр")
			Access.search(self, "module_table", "test", "")
		
		elif module_type == "search_updated":
			
			LoginsClass.login(self)
			Tools.load_page(self, "access-module")
			Tools.check_page_loaded(self, "Нэр")
			Access.search(self, "module_table", "test2", "")
		
		elif module_type == "search_deleted":
			
			LoginsClass.login(self)
			Tools.load_page(self, "access-module")
			Tools.check_page_loaded(self, "Нэр")
			Access.search(self, "module_table", "test", "Утга олдсонгүй")
	
	def product(self, product_type):
		
		driver = self.driver
		
		if product_type == "add":
			Tools.button_click(self, "class_name_0", "btn", "", By.CLASS_NAME)
			Access.addproduct(self, "test xvrlee", "test xvrlee", "Active", "Ажилтан", " Нэмэх ")
		
		if product_type == "search" or product_type == "delete" or product_type == "update":
			
			
			if (product_type == "delete"):
				Access.search(self, "product_table", "test xvrlee2", "")
				Tools.button_click(self, '//i[@class="icon-trash text-danger-600"]', "click", "", By.XPATH)
				Tools.button_click(self, "contains", " Устгах ", "", By.XPATH)
			elif (product_type == "update"):
				Access.search(self, "product_table", "test xvrlee", "")
				Tools.button_click(self, '//i[@class="icon-pencil7 text-primary-600"]', "click", "", By.XPATH)
				Access.addproduct(self, "test xvrlee2", "test xvrlee2", "Active", "Ажилтан", " Засах ")
		
		elif product_type == "search_added":
			
			LoginsClass.login(self)
			Tools.load_page(self, "access-product")
			Tools.check_page_loaded(self, "Нэр")
			Access.search(self, "product_table", "test xvrlee", "")
		
		elif product_type == "search_updated":
			
			LoginsClass.login(self)
			Tools.load_page(self, "access-product")
			Tools.check_page_loaded(self, "Нэр")
			Access.search(self, "product_table", "test xvrlee2", "")
		
		elif product_type == "search_deleted":
			
			LoginsClass.login(self)
			Tools.load_page(self, "access-product")
			Tools.check_page_loaded(self, "Нэр")
			Access.search(self, "product_table", "test xvrlee", "Утга олдсонгүй")
	
	def addproduct(self, name, description, isActive, userType, button_name):
		
		driver = self.driver
		
		if (button_name == " Засах "):

			lenght = 1
			WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#product_edit_modal > div > div > div.modal-body > div.form-group > div > div:nth-child(1) > input')))
		
		if (button_name == " Нэмэх "):

			lenght = 0
			WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#product_modal > div > div > div.modal-body > form > div.form-group > div > div:nth-child(1) > input')))
		driver.find_elements_by_xpath('//input[@placeholder="Product-ын нэр"]')[lenght].clear()
		driver.find_elements_by_xpath('//input[@placeholder="Product-ын нэр"]')[lenght].send_keys('{}'.format(name))
		driver.find_elements_by_xpath('//input[@placeholder="Тайлбар"]')[lenght].clear()
		driver.find_elements_by_xpath('//input[@placeholder="Тайлбар"]')[lenght].send_keys('{}'.format(description))
		Tools.button_click(self, driver.find_elements_by_xpath('//select[@name="status"]')[lenght], "input_enter", isActive, By.XPATH)
		if (button_name == " Засах "):
			Tools.button_click(self, driver.find_element_by_xpath('//select[@name="authType"]'), "input_enter", userType, By.XPATH)
		if (button_name == " Нэмэх "):
			Tools.button_click(self, driver.find_element_by_xpath('//select[@name="userType"]'), "input_enter", userType, By.XPATH)
		Tools.button_click(self, '//button[text()="{}"]'.format(button_name), "click", "", By.XPATH)
	
	def search(self, element, compValue, message):
		
		driver = self.driver
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.ID, '{}_filter'.format(element))))
		Tools.button_click(self, driver.find_element_by_xpath('//input[@aria-controls="{}"]'.format(element)), "input_enter", "{}".format(compValue), By.XPATH)

		for x in range(10):
			
			if message == "Утга олдсонгүй":
				WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"], poll_frequency=1).until(EC.presence_of_element_located((By.CLASS_NAME, "dataTables_empty")))
				text = driver.execute_script("""return document.getElementsByClassName("dataTables_empty")[0].innerText""")
				if text == "Утга олдсонгүй":
					print("Утга олдсонгүй")
					break
			else:
				WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"], poll_frequency=1).until(EC.presence_of_element_located((By.CLASS_NAME, "sorting_1")))
				text = driver.execute_script("""return document.querySelector('td[class="sorting_1"]').innerText""")
				if text == compValue:
					print(compValue)
					break
			
			time.sleep(1)

	def addmodule(self, name, description, button_name):
		
		driver = self.driver
		
		if (button_name == " Засах "):
			lenght = 1
			WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.CSS_SELECTOR ,'#module_edit_modal > div > div > div.modal-body > div:nth-child(1) > div > div > input')))
		
		if (button_name == " Нэмэх "):
			lenght = 0
			WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#module_modal > div > div > form > div > div:nth-child(1) > div > div > input')))
		driver.find_elements_by_xpath('//input[@placeholder="Module-ын нэр"]')[lenght].clear()
		driver.find_elements_by_xpath('//input[@placeholder="Module-ын нэр"]')[lenght].send_keys('{}'.format(name))
		driver.find_elements_by_xpath('//input[@placeholder="Тайлбар"]')[lenght].clear()
		driver.find_elements_by_xpath('//input[@placeholder="Тайлбар"]')[lenght].send_keys('{}'.format(description))
		Tools.button_click(self, '//button[text()="{}"]'.format(button_name), "click", "", By.XPATH)
	
	def group(self, group_type):
		
		driver = self.driver
		
		if group_type == "add":
			Tools.button_click(self, "class_name_0", "btn", "", By.CLASS_NAME)
			Access.addgroup(self, "test xvrlee", "test", "internal", "Тийм", "Active", " Эрх нэмэх ")
		
		if group_type == "open" or group_type == "delete" or group_type == "update":
			
			Access.search(self, "prodRole_table", "test xvrlee", "")
			if (group_type == "open"):
				Tools.button_click(self, '//i[@class="icon-eye text-success-600"]', "click", "", By.XPATH)
			elif (group_type == "delete"):
				Tools.button_click(self, '//i[@class="icon-trash text-danger-600"]', "click", "", By.XPATH)
				Tools.button_click(self, '//i[@class="icon-trash text-danger-600"]', "click", "", By.XPATH)  # BUG 2 удаа дарж байж Устгах нь болж байна.
				Tools.button_click(self, "contains", " Устгах", "", By.XPATH)
			elif (group_type == "update"):
				Tools.button_click(self, '//i[@class="icon-pencil7 text-primary-600"]', "click", "", By.XPATH)
				Access.addgroup(self, "test xvrlee2", "test2", "internal", "Тийм", "Active", " Засах ")
	
	def addgroup(self, name, description, product, isDefault, isActive, button_name):
		
		driver = self.driver
		
		if (button_name == " Засах "):

			lenght = 2
			min_lenght = 1
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#role_edit_modal > div > div > div.modal-body > div:nth-child(1) > div > div:nth-child(1) > input")))
			driver.find_elements_by_xpath('//input[@placeholder="Нэр"]')[min_lenght].clear()
			driver.find_elements_by_xpath('//input[@placeholder="Нэр"]')[min_lenght].send_keys("{}".format(name))
		
		if (button_name == " Эрх нэмэх "):

			lenght = 1
			min_lenght = 0
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Role Нэр"]')))
			driver.find_element_by_xpath('//input[@placeholder="Role Нэр"]').send_keys('{}'.format(name))
		driver.find_elements_by_xpath('//input[@placeholder="Тайлбар"]')[lenght].send_keys('{}'.format(description))
		print(date_time_access)
		driver.find_elements_by_xpath('//input[@name="issuedAt"]')[min_lenght].send_keys('{}'.format(date_time_access))
		driver.find_elements_by_xpath('//input[@name="expiresIn"]')[min_lenght].send_keys('{}'.format("07/28/2021"))
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_element_located((By.CLASS_NAME, "selection")))
		
		if lenght == 1:

			Tools.button_click(self, driver.find_element_by_id("productId"), "input_enter", product, By.XPATH)

		Tools.button_click(self, driver.find_elements_by_xpath('//select[@name="isDefault"]')[min_lenght], "input_enter", isDefault, By.XPATH)
		Tools.button_click(self, driver.find_elements_by_xpath('//select[@name="status"]')[min_lenght], "input_enter", isActive, By.XPATH)
		Tools.button_click(self, '//button[text()="{}"]'.format(button_name), "click", "", By.XPATH)

	def endpoint(self, endpoint_type):

		driver = self.driver
		
		if endpoint_type == "add":
			Tools.button_click(self, "class_name_0", "btn", "", By.CLASS_NAME)
			Access.addendpoint(self, "test xvrlee", "test", "1", "GET", "account-service-1", "test", " Нэмэх ")

	def addendpoint(self, name, description, status, method, module, endpoint, button_name):
		
		driver = self.driver
		
		# if (button_name == " Засах "):

		# 	lenght = 2
		# 	min_lenght = 1
		# 	WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#role_edit_modal > div > div > div.modal-body > div:nth-child(1) > div > div:nth-child(1) > input")))
		# 	driver.find_elements_by_xpath('//input[@placeholder="Нэр"]')[min_lenght].clear()
		# 	driver.find_elements_by_xpath('//input[@placeholder="Нэр"]')[min_lenght].send_keys("{}".format(name))
		
		# if (button_name == " Эрх нэмэх "):

		# 	lenght = 1
		# 	min_lenght = 0
		# 	WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Role Нэр"]')))
		# 	driver.find_element_by_xpath('//input[@placeholder="Role Нэр"]').send_keys('{}'.format(name))
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Endpoint-ын нэр"]')))
		driver.find_element_by_xpath('//input[@placeholder="Endpoint-ын нэр"]').send_keys('{}'.format(name))
		driver.find_element_by_xpath('//input[@placeholder="Тайлбар"]').send_keys('{}'.format(description))
		Tools.button_click(self, driver.find_element_by_xpath('//select[@name="status"]'), "input_enter", status, By.XPATH)
		Tools.button_click(self, driver.find_element_by_xpath('//select[@name="method"]'), "input_enter", method, By.XPATH)
		driver.find_element_by_xpath('//input[@placeholder="/yourUrl"]').send_keys('{}'.format(endpoint))
		Tools.button_click(self, '#endpoint_modal > div > div > form > div > div:nth-child(3) > div > div:nth-child(2) > select2 > span > span.selection > span', "send_keys_action", "{}".format(module), By.CSS_SELECTOR)
		Tools.button_click(self, '//button[text()="{}"]'.format(button_name), "click", "", By.XPATH)

		
	# 	if endpoint_type == "open" or group_type == "delete" or group_type == "update":
			
	# 		Access.search(self, "prodRole_table", "test xvrlee", "")
	# 		if (group_type == "open"):
	# 			Tools.button_click(self, '//i[@class="icon-eye text-success-600"]', "click", "", By.XPATH)
	# 		elif (group_type == "delete"):
	# 			Tools.button_click(self, '//i[@class="icon-trash text-danger-600"]', "click", "", By.XPATH)
	# 			Tools.button_click(self, '//i[@class="icon-trash text-danger-600"]', "click", "", By.XPATH)  # BUG 2 удаа дарж байж Устгах нь болж байна.
	# 			Tools.button_click(self, "contains", " Устгах", "", By.XPATH)
	# 		elif (group_type == "update"):
	# 			Tools.button_click(self, '//i[@class="icon-pencil7 text-primary-600"]', "click", "", By.XPATH)
	# 			Access.addgroup(self, "test xvrlee2", "test2", "internal", "Тийм", "Active", " Засах ")
	

	# 	driver = self.driver
	# 	ACCESS = {
	# 		"link": {
	# 			"name": "testName",
	# 			"description": "testDescription",
	# 			"status": "1 - Active",
	# 			"module": "behavioral-service-1",
	# 			"request_method": "GET",
	# 			"url_endpoint": "/some/endpoint",
	# 		}
	# 	}
		
	# 	if operation == "add":
	# 		driver.find_element_by_xpath('//button[text()=" Холбоос нэмэх "]').click()
	# 		WebDriverWait(driver, consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Endpoint-ын нэр"]')))
	# 		driver.find_element_by_xpath('//input[@placeholder="Endpoint-ын нэр"]').send_keys(ACCESS['link']['name'])
	# 		WebDriverWait(driver, consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Тайлбар"]')))
	# 		driver.find_element_by_xpath('//input[@placeholder="Тайлбар"]').send_keys(ACCESS['link']['description'])
	# 		WebDriverWait(driver, consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='status']/option[text()='0 - Inactive']")))
	# 		driver.find_element_by_xpath("//select[@name='status']/option[text()='{}']".format(ACCESS['link']['status'])).click()
	# 		WebDriverWait(driver, consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="/yourUrl"]')))
	# 		driver.find_element_by_xpath('//input[@placeholder="/yourUrl"]').send_keys(ACCESS['link']['url_endpoint'])
	# 		WebDriverWait(driver, consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='method']/option[text()='GET']")))
	# 		driver.find_element_by_xpath("//select[@name='method']/option[text()='{}']".format(ACCESS['link']['request_method'])).click()
	# 		module_xpath = "/html/body/app-root/app-main/div/div/div/div[3]/endpoint/div[2]/div/div/form/div/div[3]/div/div[2]/select2/span/span[1]/span/span[1]"
	# 		WebDriverWait(driver, consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, module_xpath)))
	# 		driver.find_element_by_xpath(module_xpath).click()
	# 		ActionChains(driver).send_keys(ACCESS['link']['module']).perform()
	# 		ActionChains(driver).send_keys(Keys.RETURN).perform()
	# 		driver.find_element_by_xpath('//button[text()=" Нэмэх "]').click()
			
	# 	elif operation == "edit":
			
	# 		ACCESS = {
	# 			"link": {
	# 				"edit_name": "editedTestName",
	# 				"edit_description": "editedTestDescription",
	# 				"edit_status": "Inactive",
	# 				"edit_request_method": "POST",
	# 				"edit_end_point": "edited/some/endpoint"
	# 			}
	# 		}
			
	# 		driver = self.driver
	# 		driver.execute_script("document.getElementsByTagName('tr')[1].children[5].getElementsByTagName('i')[0].click()")
	# 		name_xpath = '//*[@id="endpoint_edit_modal"]/div/div/div[2]/div[1]/div/div/input'
	# 		description_xpath = '//*[@id="endpoint_edit_modal"]/div/div/div[2]/div[2]/div/div/input'
	# 		url_xpath = '//*[@id="endpoint_edit_modal"]/div/div/div[2]/div[4]/div/div/input'
	# 		method_xpath = '//*[@id="endpoint_edit_modal"]/div/div/div[2]/div[3]/div/div[1]/select'
	# 		status_xpath = '//*[@id="endpoint_edit_modal"]/div/div/div[2]/div[3]/div/div[2]/select'
			
	# 		WebDriverWait(driver, consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, name_xpath)))
	# 		driver.find_element_by_xpath(name_xpath).clear()
	# 		driver.find_element_by_xpath(name_xpath).send_keys(ACCESS['link']['edit_name'])
			
	# 		WebDriverWait(driver, consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, description_xpath)))
	# 		driver.find_element_by_xpath(description_xpath).clear()
	# 		driver.find_element_by_xpath(description_xpath).send_keys(ACCESS['link']['edit_description'])
			
	# 		WebDriverWait(driver, consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, url_xpath)))
	# 		driver.find_element_by_xpath(url_xpath).clear()
	# 		driver.find_element_by_xpath(url_xpath).send_keys(ACCESS['link']['edit_end_point'])
			
	# 		WebDriverWait(driver, consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, method_xpath)))
	# 		driver.find_element_by_xpath(method_xpath).click()
	# 		ActionChains(driver).send_keys(ACCESS['link']['edit_request_method']).perform()
	# 		ActionChains(driver).send_keys(Keys.RETURN).perform()
			
	# 		WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, status_xpath)))
	# 		driver.find_element_by_xpath(status_xpath).click()
	# 		ActionChains(driver).send_keys(ACCESS['link']['edit_status']).perform()
	# 		ActionChains(driver).send_keys(Keys.RETURN).perform()
		
	# 		driver.find_element_by_xpath('//button[text()=" Засах "]').click()
		
	# 	elif operation == "change":
	# 		driver.execute_script("document.querySelector('.switchery').click()")
			
	# 	elif operation == "delete":
	# 		WebDriverWait(self.driver, consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='editedTestName']")))
	# 		for x in range(2):
	# 			driver.execute_script("document.getElementsByTagName('tr')[1].children[5].getElementsByTagName('i')[1].click()")  # BUG 2 udaa darahgui l bol bolohgui baisan
	# 		driver.execute_script('document.querySelector("#endpoint_delete_modal > div > div > div.modal-footer > button.btn.btn-danger").click()')
	
	# def inquire_endpoint(self, name):
	# 	if name == "testName":
	# 		ACCESS = {
	# 			"link": {
	# 				"name": "testName",
	# 				"module": "behavioral-service-1"
	# 			}
	# 		}
		
	# 	elif name == "editedTestName":
	# 		ACCESS = {
	# 			"link": {
	# 				"name": "editedTestName",
	# 				"module": "behavioral-service-1"
	# 			}
	# 		}
		
	# 	driver = self.driver
	# 	WebDriverWait(driver, consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Модуль сонгох"]')))
	# 	driver.find_element_by_xpath('//span[text()="Модуль сонгох"]').click()
	# 	ActionChains(driver).send_keys(ACCESS['link']['module']).perform()
	# 	ActionChains(driver).send_keys(Keys.RETURN).perform()
	# 	WebDriverWait(driver, consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@aria-controls="modEndpoint_table"]')))
	# 	driver.find_element_by_xpath('//input[@aria-controls="modEndpoint_table"]').send_keys(ACCESS['link']['name'])
		
	# 	try:
			
	# 		return driver.find_elements_by_tag_name('tr')[1].text.split()
		
	# 	except:
			
	# 		return []
	
	def user_access(self, operation):

		driver = self.driver

		if operation == "edit":

			driver.find_element_by_xpath('//input[@placeholder="Domain ID"]').send_keys(17325)
			driver.find_elements_by_class_name('btn')[1].click()
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'icon-pencil7')))
			driver.find_element_by_class_name('icon-pencil7').click()
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Засах "]')))
			driver.find_element_by_xpath('//button[text()=" Засах "]').click()

		elif operation == "change status":

			driver.find_element_by_xpath('//input[@placeholder="Domain ID"]').send_keys(17325)
			driver.find_elements_by_class_name('btn')[1].click()
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'icon-pencil7')))
			driver.find_elements_by_class_name('switchery')[1].click()

		elif operation == "inquire access":

			driver.find_element_by_xpath('//input[@placeholder="Domain ID"]').send_keys(17325)
			driver.find_elements_by_class_name('btn')[1].click()
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'icon-pencil7')))
			driver.find_element_by_class_name('icon-eye').click()

		elif operation == "add access":

			driver.find_element_by_xpath('//input[@placeholder="Domain ID"]').send_keys(17325)
			driver.find_elements_by_class_name('btn')[1].click()
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'icon-pencil7')))
			driver.find_element_by_class_name('icon-eye').click()
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Эрх нэмэх "]')))
			driver.find_element_by_xpath('//button[text()=" Эрх нэмэх "]').click()
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Хаах "]')))
			driver.find_elements_by_xpath('//button[text()=" Эрх нэмэх "]')[1].click()

		elif operation == "delete access":

			driver.find_element_by_xpath('//input[@placeholder="Domain ID"]').send_keys(17325)
			driver.find_elements_by_class_name('btn')[1].click()
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'icon-pencil7')))
			driver.find_element_by_class_name('icon-eye').click()
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="userRole_table_filter"]/label/input')))
			driver.find_elements_by_xpath("//input[@type='search']")[1].send_keys('smart')

			for x in range(2):

				driver.find_element_by_class_name('icon-trash').click()
				
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Устгах ']")))
			driver.find_element_by_xpath("//button[text()=' Устгах ']").click()