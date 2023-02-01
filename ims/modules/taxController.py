# -*- coding: UTF-8 -*
import datetime
import time
from modules.constants import *
from modules.utils import Tools
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

consts = Constant()

#IMS-n Tatvar tsesen deerkh uildluudiig ene classaar hiij baigaa
class Tax:
	#Tatvar-Tatvariin uilhilgee tsesen deer hiigddeg uildluudiig ene function -r hiij baigaa
	def tax_service(self):
		driver = self.driver					
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Гүйлгээний жагсаалт "]')))		
		driver.find_element_by_xpath('//button[text()=" Гүйлгээний жагсаалт "]').click()
		Tools.search_date(self)					

	def tax_transaction(self):
		driver = self.driver
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Татвар төлөгчийн invoice дугаар"]')))
		driver.find_element_by_xpath('//input[@placeholder="Татвар төлөгчийн invoice дугаар"]').send_keys("3190300110240")
		driver.find_element_by_xpath('//button[text()=" Хайх "]').click()
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Татвар төлөх "]')))			
		driver.find_element_by_xpath('//button[text()=" Татвар төлөх "]').click()
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Шилжүүлэх данс"]')))			
		driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх данс"]').send_keys("5154084503")
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Шилжүүлэх дүн"]')))
		driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх дүн"]').clear()
		driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэх дүн"]').send_keys("1000")
		driver.find_element_by_xpath('//input[@placeholder="Утасны дугаар"]').send_keys("95598874")
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Шилжүүлэх "]')))
		driver.find_element_by_xpath('//button[text()=" Шилжүүлэх "]').click()


	def tax_report(self):
		driver = self.driver					
		WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Хайх "]')))
		driver.execute_script('document.querySelector("body > app-root > app-main > div > div > div > div.content > app-report > div.panel.panel-flat > div > div > div:nth-child(4) > lib-date-range-picker > div > span > i").click()')
		driver.find_element_by_xpath("//*[text()='29']").click()
		driver.find_element_by_xpath("//*[text()='29']").click()
		driver.find_element_by_xpath("//*[text()='Сонгох']").click()
		driver.find_element_by_xpath("//*[text()=' Хайх ']").click()
		WebDriverWait(driver, timeout=30).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '4')]")))								
		driver.find_element_by_xpath("//*[text()='Амжилттай']").click()
		a = driver.find_element_by_xpath("//table[@id='DataTables_Table_1']").screenshot_as_png
		with open('screenshot/screenshot_invoice_number.png', 'wb') as file:
    			file.write(a)
		time.sleep(5)

	def tax_report(self, type):
		driver = self.driver
		if(type == "invoice_number"):					
			WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Хайх "]')))
			driver.execute_script('document.querySelector("body > app-root > app-main > div > div > div > div.content > app-report > div.panel.panel-flat > div > div > div:nth-child(4) > lib-date-range-picker > div > span > i").click()')
			driver.find_element_by_xpath("//*[text()='29']").click()
			driver.find_element_by_xpath("//*[text()='29']").click()
			driver.find_element_by_xpath("//*[text()='Сонгох']").click()
			driver.find_element_by_xpath("//*[text()=' Хайх ']").click()
			WebDriverWait(driver, timeout=30).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '4')]")))								
			driver.find_element_by_xpath("//*[text()='Амжилттай']").click()
			a = driver.find_element_by_xpath("//table[@id='DataTables_Table_1']").screenshot_as_png
			with open('screenshot/screenshot_invoice_number.png', 'wb') as file:
    				file.write(a)
			time.sleep(5)

		elif(type == "state_registration_certificate_number"):
			WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Хайх "]')))
			driver.find_element_by_xpath('//span[text()=" Нэхэмжлэлийн дугаар "]').click()
			ActionChains(driver).send_keys(' ҮХЭХ-ийн улсын бүртгэлийн гэрчилгээний дугаар ').perform()
			ActionChains(driver).send_keys(Keys.ENTER).perform()
			driver.execute_script('document.querySelector("body > app-root > app-main > div > div > div > div.content > app-report > div.panel.panel-flat > div > div > div:nth-child(4) > lib-date-range-picker > div > span > i").click()')
			driver.find_element_by_xpath("//*[text()='29']").click()
			driver.find_element_by_xpath("//*[text()='29']").click()
			driver.find_element_by_xpath("//*[text()='Сонгох']").click()
			driver.find_element_by_xpath("//*[text()=' Хайх ']").click()
			WebDriverWait(driver, timeout=30).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '2')]")))								
			driver.find_element_by_xpath("//*[text()='Амжилттай']").click()
			a = driver.find_element_by_xpath("//table[@id='DataTables_Table_0']").screenshot_as_png
			with open('screenshot/screenshot_state_registration certificate_number.png', 'wb') as file:
    				file.write(a)
			time.sleep(5)

		elif(type == "vehicle_number"):
			WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Хайх "]')))
			driver.find_element_by_xpath('//span[text()=" Нэхэмжлэлийн дугаар "]').click()
			ActionChains(driver).send_keys(' Тээврийн хэрэгслийн арлын дугаар ').perform()
			ActionChains(driver).send_keys(Keys.ENTER).perform()
			driver.execute_script('document.querySelector("body > app-root > app-main > div > div > div > div.content > app-report > div.panel.panel-flat > div > div > div:nth-child(4) > lib-date-range-picker > div > span > i").click()')
			driver.find_element_by_xpath("//*[text()='29']").click()
			driver.find_element_by_xpath("//*[text()='29']").click()
			driver.find_element_by_xpath("//*[text()='Сонгох']").click()
			driver.find_element_by_xpath("//*[text()=' Хайх ']").click()
			WebDriverWait(driver, timeout=30).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '1')]")))
			driver.find_element_by_xpath("//*[text()='Амжилттай']").click()
			a = driver.find_element_by_xpath("//table[@class='table table-bordered table-framed table-hover reportSuccessTable']").screenshot_as_png
			with open('screenshot/screenshot_vehicle_number.png', 'wb') as file:
    				file.write(a)
			time.sleep(5)

		elif(type == "vehicle_state_registration_number"):
			WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Хайх "]')))
			driver.find_element_by_xpath('//span[text()=" Нэхэмжлэлийн дугаар "]').click()
			ActionChains(driver).send_keys(' Тээврийн хэрэгслийн улсын бүртгэлийн дугаар ').perform()
			ActionChains(driver).send_keys(Keys.ENTER).perform()
			driver.execute_script('document.querySelector("body > app-root > app-main > div > div > div > div.content > app-report > div.panel.panel-flat > div > div > div:nth-child(4) > lib-date-range-picker > div > span > i").click()')
			driver.find_element_by_xpath("//*[text()='29']").click()
			driver.find_element_by_xpath("//*[text()='29']").click()
			driver.find_element_by_xpath("//*[text()='Сонгох']").click()
			driver.find_element_by_xpath("//*[text()=' Хайх ']").click()
			WebDriverWait(driver, timeout=30).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '1')]")))		
			driver.find_element_by_xpath("//*[text()='Амжилттай']").click()
			a = driver.find_element_by_xpath("//table[@class='table table-bordered table-framed table-hover reportSuccessTable']").screenshot_as_png
			with open('screenshot/screenshot_vehicle_state_registration_number.png', 'wb') as file:
    				file.write(a)
			time.sleep(5)


		elif(type == "main_iron_number_of_the_firearm"):
			WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Хайх "]')))
			driver.find_element_by_xpath('//span[text()=" Нэхэмжлэлийн дугаар "]').click()
			ActionChains(driver).send_keys(' Галт зэвсгийн гол төмрийн дугаар ').perform()
			ActionChains(driver).send_keys(Keys.ENTER).perform()
			driver.execute_script('document.querySelector("body > app-root > app-main > div > div > div > div.content > app-report > div.panel.panel-flat > div > div > div:nth-child(4) > lib-date-range-picker > div > span > i").click()')
			driver.find_element_by_xpath("//*[text()='29']").click()
			driver.find_element_by_xpath("//*[text()='29']").click()
			driver.find_element_by_xpath("//*[text()='Сонгох']").click()
			driver.find_element_by_xpath("//*[text()=' Хайх ']").click()
			WebDriverWait(driver, timeout=30).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), ' Тухайн өдрөөр хайсан тайлан байхгүй байна. ')]")))
			driver.find_element_by_xpath("//*[text()='Амжилттай']").click()
			a = driver.find_element_by_xpath("//*[@id='table']").screenshot_as_png
			with open('screenshot/screenshot_main_iron_number_of_the_firearm.png', 'wb') as file:
    				file.write(a)
			time.sleep(5)

		elif(type == "firearms_certificate_number"):
			WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Хайх "]')))
			driver.find_element_by_xpath('//span[text()=" Нэхэмжлэлийн дугаар "]').click()
			ActionChains(driver).send_keys(' Галт зэвсгийн гэрчилгээний дугаар ').perform()
			ActionChains(driver).send_keys(Keys.ENTER).perform()
			driver.execute_script('document.querySelector("body > app-root > app-main > div > div > div > div.content > app-report > div.panel.panel-flat > div > div > div:nth-child(4) > lib-date-range-picker > div > span > i").click()')
			driver.find_element_by_xpath("//*[text()='29']").click()
			driver.find_element_by_xpath("//*[text()='29']").click()
			driver.find_element_by_xpath("//*[text()='Сонгох']").click()
			driver.find_element_by_xpath("//*[text()=' Хайх ']").click()
			WebDriverWait(driver, timeout=30).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), ' Тухайн өдрөөр хайсан тайлан байхгүй байна. ')]")))	
			a = driver.find_element_by_xpath("//*[@id='table']").screenshot_as_png
			with open('C:/Users/90058/Desktop/testscreenshotfolder/screenshotAll.png', 'wb') as file:
    				file.write(a)
			time.sleep(5)

