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

date_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
date_time_access = datetime.datetime.now().strftime("%m/%d/%Y")
consts = Constant()

#IMS-n Bichig  barimt tsesend deerh uildluudiig ene classaar hiij baigaa
class Document_personal:

	#Function of Upgrade to Branch
	def upgrade_branch(self):
		driver=self.driver

		Tools.button_click(self, "//*[@id='role_modal']/div/div/form/div/div[1]/div/div[1]/input", "clear", "", By.XPATH)
		Tools.button_click(self, "//*[@id='role_modal']/div/div/form/div/div[1]/div/div[1]/input", "send_keys", "This is upgrade to Branch", By.XPATH)
		Tools.button_click(self, "//*[@id='role_modal']/div/div/div[2]/button[2]", "click", "", By.XPATH)


	#Function of Visa account statement at the Embassy of Korea
	def embassy_korea(self, window_name):
		driver=self.driver
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'БНСУ-н виз хүсэгчдийн дансны хуулганы хураангуй маягт авах үйлчилгээ')]")))
		driver.execute_script("""document.evaluate("//*[text()='{}']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.parentElement.children[1].click()""".format(window_name))
		Tools.button_click(self, "//button[text()='Үргэлжлүүлэх ']", "click", "",By.XPATH)

		if window_name == "БНСУ-н виз хүсэгчдийн дансны хуулганы хураангуй маягт авах үйлчилгээ":
			Tools.button_click(self, "//*[@id='input-variables']/div[2]/div[1]/div[3]/fieldset/div[2]/div/div/lib-multi-select/div/div/button", "click", "",By.XPATH)
			Tools.button_click(self, "//*[@id='input-variables']/div[2]/div[1]/div[3]/fieldset/div[2]/div/div/lib-multi-select/div/div/div/label[1]/span", "click", "",By.XPATH)

		Tools.button_click(self, '//button[text()=" Элчин сайдын яам "]', "click", "",By.XPATH)
		
		#below code is check load page BUA after print preview
		# WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'БҮАА Зөвшөөрөл')]")))


	def definition(self, window_name):
		driver = self.driver
		
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Стандарт бус дансны үлдэгдэлгүй тодорхойлолт')]")))
		driver.execute_script("""document.evaluate("//*[text()='{}']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.parentElement.children[1].click()""".format(window_name))
		Tools.button_click(self, "//button[text()='Үргэлжлүүлэх ']", "click", "",By.XPATH)
		
		if window_name == "Стандарт бус дансны үлдэгдэлгүй тодорхойлолт":

			Tools.button_click(self, '//*[@title=" Данс сонгоно уу! "]', "click", "",By.XPATH)
			ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
			ActionChains(driver).send_keys(Keys.RETURN).perform()
			Tools.button_click(self, "input_placeholder", "Нэмэлт тайлбар ", "test","")
			Tools.button_click(self, "input_placeholder", "Зориулалт", "test","")

		elif window_name == "Стандарт бус тодорхойлолт ":

			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[@title=' Данс сонгоно уу! ']")))
			Tools.button_click(self, '//*[@title=" Данс сонгоно уу! "]', "click", "",By.XPATH)
			ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
			ActionChains(driver).send_keys(Keys.RETURN).perform()
			Tools.button_click(self, "input_placeholder", "Нэмэлт тайлбар", "test","")
			Tools.button_click(self, "input_placeholder", "Зориулалт", "test","")

		elif window_name == "Стандарт дансны үлдэгдэлгүй тодорхойлолт":

			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[@title=' Данс сонгоно уу! ']")))
			Tools.button_click(self, '//*[@title=" Данс сонгоно уу! "]', "click", "", By.XPATH)
			ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
			ActionChains(driver).send_keys(Keys.RETURN).perform()
			Tools.button_click(self, "input_placeholder", "Зориулалт ", "test","")

		elif window_name == "Стандарт тодорхойлолт":

			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[@title=' Данс сонгоно уу! ']")))
			Tools.button_click(self, '//*[@title=" Данс сонгоно уу! "]', "click", "",By.XPATH)
			ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
			ActionChains(driver).send_keys(Keys.RETURN).perform()

		Tools.button_click(self, "//button[text()=' Тодорхойлолт бэлтгэх ']", "click", "",By.XPATH)
		Tools.button_click(self, "//button[text()=' Хураамж авах ']", "click", "",By.XPATH)

		time.sleep(5)

	def definition_loan(self, window_name):
		driver = self.driver
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Өр зээлтэй (үлдэгдэлтэй')]")))
		driver.execute_script("""document.evaluate("//*[text()='{}']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.parentElement.children[1].click()""".format(window_name))
		Tools.button_click(self, "//button[text()='Үргэлжлүүлэх ']", "click", "",By.XPATH)
		Tools.button_click(self, "//button[text()=' Тодорхойлолт бэлтгэх ']", "click", "",By.XPATH)
		time.sleep(5)

	######Geree maygt beltgekh, Danstai holbootoi geree maygt beltgekh funtion
	def chooseProductAccount(self, window_name):
		driver = self.driver
		DATA = {
			"lastname": "lastname",
			"description": "tailbar oruulakh",
			"changeToProductName": "uurchlukh buteegdekhvvn",
			"startDate": "2020-05-05",
			"endDate": "2020-06-05",
			"reason": "Shaltgaan oruulakh",
			"changeToType": "Change to Type",
			"changeSegment": "Segment", 
			"finishidToChangeProduct": "3000-1",
			"day1": "1",
			"day2": "2",
			"money1": "10000000",
			"money2": "20000000",
			"nuuts-hariult": "nuuts-hariult"
		}
		
		Tools.button_click(self, "contains", "Дансны үйлчилгээ", "",By.XPATH)
		Tools.button_click(self, "contains", "Дансны үйлчилгээ", "",By.XPATH)
		
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Баталгаат гарын үсэг шинэчлэх')]")))
		
		driver.execute_script("""document.evaluate("//*[text()='{}']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.parentElement.children[1].click()""".format(window_name))
		Tools.button_click(self, "//button[text()='Үргэлжлүүлэх ']", "click", "",By.XPATH)

		if window_name == "Баталгаат гарын үсэг шинэчлэх":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"],"")

		elif window_name == "Буруу үүссэн, давхардсан CIF засварлах":
			Tools.button_click(self, "input_placeholder", "Харилцагчийн CIF дугаар", consts.ACCOUNTS["CIF"],"")
			Tools.button_click(self, "input_placeholder", "Шалтгаан", DATA["reason"],"")

		elif window_name == "Данс лавлах" or window_name == "Данс хаах":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар 1", consts.ACCOUNTS["DEPOSIT_ACCOUNT"],"")
			Tools.button_click(self, "input_placeholder", "Дансны дугаар 2", consts.ACCOUNTS["DEPOSIT_ACCOUNT_2"],"")

		elif window_name == "Дансанд зогсоолт хийх ":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар 2", consts.ACCOUNTS["DEPOSIT_ACCOUNT_2"],"")
			Tools.button_click(self, "input_placeholder", "Дансны дугаар 1", consts.ACCOUNTS["DEPOSIT_ACCOUNT"],"")

		elif window_name == "Дансанд хамтран эзэмшигч бүртгэх болон нэмэх":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"],"")
			Tools.button_click(self, "input_placeholder", "Эцэг эхийн нэр", DATA['lastname'],"")
			# Tools.button_click(self, "input_placeholder", "Нэр", "Нэр")
			# Tools.button_click(self, "input_placeholder", "РД", consts.DATA["REGISTER_NO"])

		elif window_name == "Дансны барилт цуцлах":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар 1", consts.ACCOUNTS["DEPOSIT_ACCOUNT"],"")
			Tools.button_click(self, "input_placeholder", "Дансны дугаар 2", consts.ACCOUNTS["DEPOSIT_ACCOUNT_2"],"")

		elif window_name == "Дансны бусад үйлчилгээ":
			Tools.button_click(self, "input_placeholder", "Тайлбар", DATA['description'],"")

		elif window_name == "Дансны төлөв өөрчлөх":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар 1", consts.ACCOUNTS["DEPOSIT_ACCOUNT"],"")
			Tools.button_click(self, "input_placeholder", "Дансны дугаар 2", consts.ACCOUNTS["DEPOSIT_ACCOUNT_2"],"")

		elif window_name == "Дансны төрөл, категори солих":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"],"")
			Tools.button_click(self, "input_placeholder", "Өөрчлөх бүтээгдэхүүн", DATA['changeToProductName'],"")

		elif window_name == "Дансны хамтран эзэмшигч цуцлах":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар ", consts.ACCOUNTS["DEPOSIT_ACCOUNT"],"")
			Tools.button_click(self, "input_placeholder", "Эцэг эхийн нэр", DATA['lastname'],"")
			Tools.button_click(self, "input_placeholder", "Нэр", "Нэр","")
			Tools.button_click(self, "input_placeholder", "Регистерийн дугаар", consts.DATA["REGISTER_NO"],"")

		elif window_name == "Дансны хуулга авах":
			Tools.button_click(self, "input_placeholder", "account-number", consts.ACCOUNTS["DEPOSIT_ACCOUNT"],"")
			Tools.button_click(self, "input_placeholder", "nuuts-hariult", DATA["nuuts-hariult"],"")

		elif window_name == "Дансны үлдэгдэлд барилт хийх":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар 1", consts.ACCOUNTS["DEPOSIT_ACCOUNT"],"")
			Tools.button_click(self, "input_placeholder", "Дансны дугаар 2", consts.ACCOUNTS["DEPOSIT_ACCOUNT_2"],"")

		elif window_name == "Зогсоолт чөлөөлөх":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар 2", consts.ACCOUNTS["DEPOSIT_ACCOUNT_2"],"")
			Tools.button_click(self, "input_placeholder", "Дансны дугаар 1", consts.ACCOUNTS["DEPOSIT_ACCOUNT"],"")

		elif window_name == "Харилцагчийн CIF идэвхжүүлэх":
			Tools.button_click(self, "input_placeholder", "Харилцагчийн CIF дугаар", consts.ACCOUNTS["CIF"],"")
			Tools.button_click(self, "input_placeholder", "Шалтгаан", DATA['reason'],"")

		elif window_name == "Харилцагчийн сегмент, төрөл солих":
			Tools.button_click(self, "input_placeholder", "Өөрчлөх төрөл", DATA["changeToType"],"")
			Tools.button_click(self, "input_placeholder", "Өөрчлөх сегмент", DATA["changeSegment"],"")

		elif window_name == "Хугацаатай хадгаламжийн хугацаа сунгах захиалга /2071/":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"],"")
			Tools.button_click(self, "input_placeholder", "Хугацааны эцэст шилжих бүтээгдэхүүн", DATA["finishidToChangeProduct"],"")

		elif window_name == "Хуримтлал цуцлах":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"],"")

		elif window_name == "Хуримтлалын үйлчилгээ засварлах":
			Tools.button_click(self, "input_placeholder", "Шилжүүлэх данс", consts.ACCOUNTS["DEPOSIT_ACCOUNT"],"")
			Tools.button_click(self, "input_placeholder", " Суутгах данс", consts.ACCOUNTS["DEPOSIT_ACCOUNT_2"],"")
			Tools.button_click(self, "input_placeholder", "Татах өдөр 1", DATA["day1"],"")
			Tools.button_click(self, "input_placeholder", "Мөнгөн дүн 1", DATA["money1"],"")
			Tools.button_click(self, "input_placeholder", "Татах өдөр 2", DATA["day2"],"")
			Tools.button_click(self, "input_placeholder", "Мөнгөн дүн 2", DATA["money2"],"")
			
		Tools.button_click(self, "//button[text()=' Гэрээ, маягт бэлтгэх ']", "click", "",By.XPATH)
	
		# WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'БҮАА Зөвшөөрөл')]")))

	#Geree maygt beltgekh, Tsahimtai holbootoi geree maygt beltgekh function
	def chooseProductCyber(self, window_name):
		driver = self.driver

		DATA = {
			"email": "email@email.com",
			"userId": "testname",
			"customerLimit": "9999999",
			"VaskoSerialNumber": "9295123149",
			"registeredPhoneNumber": "99070149",
			"changeToPhoneBumber": "99884281",
			"phoneNumber": "99070149",
			"description": "Tailbar"
		}
		Tools.button_click(self, "contains", "Цахимтай холбоотой", "",By.XPATH)
		Tools.button_click(self, "contains", "Цахимтай холбоотой", "",By.XPATH)
		
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'И-Биллинг үйлчилгээ цуцлах')]")))
		driver.execute_script("""document.evaluate("//*[text()='{}']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.parentElement.children[1].click()""".format(window_name))
		Tools.button_click(self, "//button[text()='Үргэлжлүүлэх ']", "click", "",By.XPATH)

		if window_name == "И-Биллинг үйлчилгээ цуцлах":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")

		elif window_name == "Интернэт банкны  и-мэйл хаяг солиулах":
			Tools.button_click(self, "input_placeholder", "И мэйл хаяг", DATA['email'], "")

		elif window_name == "Интернэт банкны  лимит нэмэгдүүлэх":
			Tools.button_click(self, "input_placeholder", "Нэвтрэх нэр", DATA['userId'], "")
			Tools.button_click(self, "input_placeholder", "Харилцагчийн хүссэн лимит", DATA['customerLimit'], "")

		elif window_name == "Интернэт банкны Утасны дугаар солиулах":
			Tools.button_click(self, "input_placeholder", "Нэвтрэх нэр ", DATA['userId'], "")
			Tools.button_click(self, "input_placeholder", "Гар утасны дугаар",  DATA['phoneNumber'], "")

		elif window_name == "Интернэт банкны васко төхөөрөмж авах":
			Tools.button_click(self, "input_placeholder", "Нэвтрэх нэр", DATA['userId'], "")
			Tools.button_click(self, "input_placeholder", "Васко сериал дугаар", DATA['VaskoSerialNumber'], "")

		elif window_name == "Интернэт банкны үйлчилгээ сэргээх" or window_name == "Интернэт банкны үйлчилгээ цуцлах":
			Tools.button_click(self, "input_placeholder", "Нэвтрэх нэр", DATA['userId'], "")

		elif window_name == "Мобайл банк үйлчилгээг сэргээх" or window_name == "Мобайл банк үйлчилгээг цуцлах":
			Tools.button_click(self, "input_placeholder", "Бүртгэлтэй утасны дугаар", DATA['registeredPhoneNumber'], "")

		elif window_name == "Мобайл банк-Утасны дугаар солиулах":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Солих  утасны дугаар", DATA['changeToPhoneBumber'], "")

		elif window_name == "Мобайл банкны идэвхижүүлэлтийн код сэргээх, данс нэмэх":
			Tools.button_click(self, "input_placeholder", "Утасны дугаар", DATA['phoneNumber'], "")
			Tools.button_click(self, "input_placeholder", "Дансны дугаар 1", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")

		elif window_name == "Мобайл банкны лимит нэмэгдүүлэх" or window_name == "Мобайл банкны нууц үг солиулах, сэргээлгэх":
			Tools.button_click(self, "input_placeholder", "Бүртгэлтэй утасны дугаар", DATA['registeredPhoneNumber'], "")

		elif window_name == "Мобайл банкны үйлчилгээ сунгах":
			Tools.button_click(self, "input_placeholder", "Бүртгэлтэй гар утас", DATA['registeredPhoneNumber'], "")

		elif window_name == "Телефон банкны лимит нэмэгдүүлэх" or  window_name == "Телефон банкны үйлчилгээ цуцлах":
			Tools.button_click(self, "input_placeholder", "Бүртгэлтэй утасны дугаар", DATA['registeredPhoneNumber'], "")

		elif window_name == "Ухаалаг мэдээ үйлчилгээг цуцлах":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")

		elif window_name == "Ухаалаг мэдээ, Мэдээллийн төрөл солиулах":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")

		elif window_name == "Ухаалаг мэдээ, утасны  дугаар солиулах":
			Tools.button_click(self, "input_placeholder", "Солих утасны дугаар", DATA['changeToPhoneBumber'], "")
			
		elif window_name == "Цахим банкны бусад үйлчилгээ":
			Tools.button_click(self, "input_placeholder", "Тайлбар", DATA['description'], "")
		
		Tools.button_click(self, "//button[text()=' Гэрээ, маягт бэлтгэх ']", "click", "",By.XPATH)
		# time.sleep(10)
		# window_after = driver.window_handles[1]
		# window_after_title = driver.title
		# print(window_after_title)
		# driver.switch_to.window(window_after)
		# driver.save_screenshot("screenshot1.png")
		# WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'БҮАА Зөвшөөрөл')]")))

	#Geree maygt beltgekh, Cardtai holbootoi geree maygt beltgekh function
	def chooseProductCard(self, window_name):
		driver = self.driver
		DATA = {
			"digitSixPhoneNumber": "99060149",
			"phoneNumber": "99070139",
			"CoreCardNumber": "4380567890123456",
			"SubCardNumber": "4667567890123456",
			"ExpCardNumber": "6234567890123456",
			"cardNumber": "9496188198114881",
			"description": "TAilbar aa bicheerei"


		}
		Tools.button_click(self, "contains", "Карттай холбоотой", "",By.XPATH)
		Tools.button_click(self, "contains", "Карттай холбоотой", "",By.XPATH)
		
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Дэд карт авах ')]")))
		driver.execute_script("""document.evaluate("//*[text()='{}']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.parentElement.children[1].click()""".format(window_name))
		Tools.button_click(self, "//button[text()='Үргэлжлүүлэх ']", "click", "",By.XPATH)

		if window_name == "Дэд карт авах ":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "6 оронтой нууц код авах утас", DATA['digitSixPhoneNumber'], "")
			Tools.button_click(self, "input_placeholder", "Үндсэн картын дугаар", DATA['CoreCardNumber'], "")

		elif window_name == "Дэд карт хаалгах":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Дэд картын дугаар ", DATA['SubCardNumber'], "")

		elif window_name == "Идэвхгүй карт нээлгэх ":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар ", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Картын дугаар ", DATA['cardNumber'], "")

		elif window_name == "Карт нөхөн авах ":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар ", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "6 оронтой нэг удаагийн нууц код авах утас", DATA['digitSixPhoneNumber'], "")

		elif window_name == "Карт хаалгах " or window_name == "Картын пин код өөрчлөх ":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Картын дугаар ", DATA['cardNumber'], "")

		elif window_name == "Картын бусад үйлчилгээ":
			Tools.button_click(self, "input_placeholder", "Тайлбар", DATA['description'], "")

		elif window_name == "Картын лимит нэмэгдүүлэх хүсэлт":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Картын дугаар", DATA['cardNumber'], "")

		elif window_name == "Картын нэр өөрчлүүлэх ":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Картын дугаар ", DATA['cardNumber'], "")
			Tools.button_click(self, "input_placeholder", "6 оронтой нууц код авах утас", DATA['digitSixPhoneNumber'], "")

		elif window_name == "Картын хугацаа сунгуулах ":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар ", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Картын дугаар",  DATA['cardNumber'], "")
			Tools.button_click(self, "input_placeholder", "6 оронтой нэг удаагийн нууц код авах утас", DATA['digitSixPhoneNumber'], "")

		elif window_name == "Орлогын карт авах":
			Tools.button_click(self, "input_placeholder", "Карт холбох дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")

		elif window_name == "Сурагчийн карт авах":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Үндсэн картын дугаар", DATA['CoreCardNumber'], "")
			Tools.button_click(self, "input_placeholder", "Утасны дугаар", DATA['phoneNumber'], "")

		elif window_name == "Экспресс карт авах ":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Экспресс картын дугаар", DATA['ExpCardNumber'], "")
			Tools.button_click(self, "input_placeholder", "6 оронтой нэг удаагийн нууц код хүлээн авах утасны дугаар", DATA['digitSixPhoneNumber'], "")

		Tools.button_click(self, "//button[text()=' Гэрээ, маягт бэлтгэх ']", "click", "",By.XPATH)
		# WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'БҮАА Зөвшөөрөл')]")))

	#Geree maygt beltgekh, Dans neegtei holbootoi-Baiguulag-n geree maygt beltgekh function
	def chooseProductCorp(self, window_name):
		driver = self.driver
		DATA = {
			"discountInterest": "10",
			"interestOfYear": "20",
			"getInterestAccount": "5057339304",
			"getInterestDate": "2020",
			"serialNumber": "12345678",
			"moneyAmount": "1000000",
			"incomeAccountNumber": "5999009999",
			"companyName": "Khan Bank",
			"cardConnectAccount": "5999009998",
			"ebillingService": {
				"secretAnswer": "Please enter secret answer",
				"secretQuestion": "Please enter secret question",
				"serviceTypeOne": "serviceTypeOne",
				"serviceTypeTwo": "222222222",
				"paymentNumberOne": "123456789",
				"paymentNumberTwo": "223456789",
				"paymentHoldAccount": "5990009995",
				"corpNameTwo": "Nomin",
				"corpNameThree": "Khurd Group"
			}

		}
		#corp dans oruulaarai

		Tools.button_click(self, "contains", "Данс нээх, шинэ бүтээгдэхүүн", "",By.XPATH)
		Tools.button_click(self, "contains", "Данс нээх, шинэ бүтээгдэхүүн", "",By.XPATH)

		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '.Данс нээх 1')]")))
		driver.execute_script("""document.evaluate("//*[text()='{}']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.parentElement.children[1].click()""".format(window_name))
		Tools.button_click(self, "//button[text()='Үргэлжлүүлэх ']", "click", "",By.XPATH)

		if window_name == ".Данс нээх 1" or window_name == ".Данс нээх 2" or window_name == ".Данс нээх 3" :
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["ORGANIZATION_ACCOUNT"], "")
			Tools.button_click(self, '//*[@title=" Данс сонгоно уу! "]', "click", "",By.XPATH)
			ActionChains(driver).send_keys(" Кредит карт ").perform()
			ActionChains(driver).send_keys(Keys.RETURN).perform()
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[@title=' Тєлбєр, Санхүүжилт ба Тусгай үйлчилгээний харилцах (30000009) ']")))
		
		elif window_name == "Тусгай урьдчилсан хүүт хадгаламж /2223-1/":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["ORGANIZATION_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Бууруулах хүү", DATA['discountInterest'], "")
			Tools.button_click(self, "input_placeholder", "Жилийн хүү ", DATA['interestOfYear'], "")
			Tools.button_click(self, "input_placeholder", "Хүү олгох данс", DATA['getInterestAccount'], "")
		
		elif window_name == "Тусгай харилцах ":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар ", consts.ACCOUNTS["ORGANIZATION_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Хүү олгох огноо", DATA['getInterestDate'], "")
			Tools.button_click(self, "input_placeholder", "Жилийн хүү", DATA['interestOfYear'], "")
		
		elif window_name == "Тусгай урьдчилсан хүүт хадгаламж /2223-1/":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["ORGANIZATION_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Жилийн хүү", DATA['interestOfYear'], "")
		
		elif window_name == "Тусгай хугацаагүй хадгаламж /1001-2 1011-2 1021-2/":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["ORGANIZATION_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Жилийн хүү", DATA['interestOfYear'], "")
		
		elif window_name == "Тусгай хугацаатай хадгаламж /2400-3 2410-3/":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["ORGANIZATION_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Бууруулах хүү", DATA['discountInterest'], "")
			Tools.button_click(self, "input_placeholder", "Жилийн хүү ", DATA['interestOfYear'], "")
		
		elif window_name == "Хадгаламжийн сертификат /2700-1,2/":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["ORGANIZATION_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Серийн дугаар ", DATA['serialNumber'], "")
			Tools.button_click(self, "input_placeholder", "Мөнгөн дүн", DATA['moneyAmount'], "")
		
		elif window_name == "Эскроу харилцах /3000-17 3010-17 3013-17/":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар ", consts.ACCOUNTS["ORGANIZATION_ACCOUNT"], "")
		
		elif window_name == "Үнэт цаасны арилжааны эскроу /3000-26/":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар ", consts.ACCOUNTS["ORGANIZATION_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Орлого хүлээн авах дансны дугаар ", DATA['incomeAccountNumber'], "")
			Tools.button_click(self, "input_placeholder", "ҮЦКомпаний нэр ", DATA['companyName'], "")
		
		elif window_name == "Бизнес карт авах":
			Tools.button_click(self, "input_placeholder", "Карт холбох дансны дугаар", DATA['cardConnectAccount'], "")
		
		elif window_name == "И-Биллинг үйлчилгээ авах":
			Tools.button_click(self, "input_placeholder", "Үйлчилгээнд бүртгүүлэх дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Нууц хариулт", DATA['ebillingService']['secretAnswer'], "")
			Tools.button_click(self, "input_placeholder", "Нууц асуулт", DATA['ebillingService']['secretQuestion'], "")
			Tools.button_click(self, "input_placeholder", "Үйлчилгээний төрөл 1", DATA['ebillingService']['serviceTypeOne'], "")
			Tools.button_click(self, "input_placeholder", "Төлбөрийн код 1", DATA['ebillingService']['paymentNumberOne'], "")
			Tools.button_click(self, "input_placeholder", "Төлбөр суутгах данс 1", DATA['ebillingService']['paymentHoldAccount'], "")
			Tools.button_click(self, "input_placeholder", "Байгууллагын нэр 2", DATA['ebillingService']['corpNameTwo'], "")
			Tools.button_click(self, "input_placeholder", "Үйлчилгээний төрөл 2",  DATA['ebillingService']['serviceTypeTwo'], "")
			Tools.button_click(self, "input_placeholder", "Төлбөрийн код 2", DATA['ebillingService']['serviceTypeTwo'], "")
			Tools.button_click(self, "input_placeholder", "Байгууллагын нэр 3", DATA['ebillingService']['corpNameThree'], "")
		
		elif window_name == "Интернэт банкны гүйлгээний зөвшөөрлийн зэрэг тохируулах ":
			print("test")
		
		elif window_name == "Интернэт банкны үйлчилгээ авах":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар 1", consts.ACCOUNTS["ORGANIZATION_ACCOUNT"], "")
		
		elif window_name == "Свип үйлчилгээ авах ":
			Tools.button_click(self, "input_placeholder", "Орлого суутгах дансны дугаар 1", consts.ACCOUNTS["ORGANIZATION_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Орлого хүлээн авах дансны дугаар", consts.ACCOUNTS["ORGANIZATION_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Хураамж суутгах дансны дугаар", consts.ACCOUNTS["ORGANIZATION_ACCOUNT"], "")

		Tools.button_click(self, "//button[text()=' Гэрээ, маягт бэлтгэх ']", "click", "",By.XPATH)
		# WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'БҮАА Зөвшөөрөл')]")))
		
	#Geree maygt beltgekh, Dans neehtei holbootoi-Irgen-n geree maygt beltgekh function
	def choose_product(self, window_name):
		""""Geree maygt awakh dansnii buteegdekhvvn songoj pdf -r awakh"""
		driver = self.driver
		DATA = {
			"accountNumber": "5599009951",
			"accountNumberTwo": "5599009951",
			"email": "test@test.com",
			"discountInterest": "10",
			"interestOfYear": "20",
			"getInterestAccount": "5057339304",
			"getInterestDate": "2020",
			"serialNumber": "12345678",
			"moneyAmount": "1000000",
			"incomeAccountNumber": "5999009999",
			"companyName": "Khan Bank",
			"cardConnectAccount": "5999009998",
			"mandatoryMinimumAccountBalance": "5000",
			"moneyAmount": "999999",
			"digitSixPhoneNumber": "99060149",
			"phoneNumber": "99070139",
			"standartMaxInterest": "15%",
			"standartMaxInterestChar": "Usgeer oruulna",
			"backPaymentAmountMonth": "200000",
			"ebillingService": {
				"secretAnswer": "Please enter secret answer",
				"secretQuestion": "Please enter secret question",
				"serviceTypeOne": "serviceTypeOne",
				"serviceTypeTwo": "222222222",
				"paymentNumberOne": "123456789",
				"paymentNumberTwo": "223456789",
				"paymentHoldAccount": "5990009995",
				"paymentAccount": "5990009991",
				"paymentCompanyName": "Nomin",
				"corpNameThree": "Khurd Group",
				"paymentDay": "2",
				"paymentMaxAmount" : "11111111"
			},
			"activeCodeAccount": "123456",
			"getSerivcePhoneNumber": "88998811"
		}


		Tools.button_click(self, "contains", "Данс нээх, шинэ бүтээгдэхүүн", "",By.XPATH)
		Tools.button_click(self, "contains", "Данс нээх, шинэ бүтээгдэхүүн", "",By.XPATH)
		
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '.Данс нээх 2 - Иргэн')]")))
		driver.execute_script("""document.evaluate("//*[text()='{}']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.parentElement.children[1].click()""".format(window_name))
		Tools.button_click(self, "//button[text()='Үргэлжлүүлэх ']", "click", "",By.XPATH)
		
		if window_name == "Даатгалын хураамжийн хадгаламж":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Хүү олгох огноо", DATA['getInterestDate'], "")
		
		elif window_name == "Тусгай хугацаагүй хадгаламж /1000-4/":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Жилийн хүү", DATA['interestOfYear'], "")
		
		elif window_name == "Тусгай хугацаатай хадгаламж /2300-3 2310-3/":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар ", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Жилийн хүү", DATA['interestOfYear'], "")
			Tools.button_click(self, "input_placeholder", "Дансанд заавал байлгах доод үлдэгдэл", DATA['mandatoryMinimumAccountBalance'], "")
			Tools.button_click(self, "input_placeholder", "Бууруулах хүү", DATA['discountInterest'], "")
		
		elif window_name == "Хадгаламжийн сертификат /2700-1,2/":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Мөнгөн дүн ", DATA['moneyAmount'], "")
			Tools.button_click(self, "input_placeholder", "Серийн дугаар", DATA['serialNumber'], "")
		
		elif window_name == "Цалингийн зээлийн эрх нээх гэрээ":
			Tools.button_click(self, "input_placeholder", "ХААН Банкны тухайн үед мөрдөгдөж буй стандарт нөхцлийн дээд хүү хувиар", DATA['standartMaxInterest'], "")
			Tools.button_click(self, "input_placeholder", "Зээл олголтын шимтгэлийн хувь", "21", "")
			Tools.button_click(self, "input_placeholder", "ХААН Банкны тухайн үед мөрдөгдөж буй стандарт нөхцлийн дээд хүү үсгээр", DATA['standartMaxInterestChar'], "")
			Tools.button_click(self, "input_placeholder", "БАРЬЦАА ХӨРӨНГИЙН гэрээнд тусгагдах сар бүрийн эргэн төлөлтийн дүн", DATA['backPaymentAmountMonth'], "")
		
		elif window_name == "Үнэт цаасны арилжааны эскроу /3000-25/":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Орлого хүлээн авах данс", DATA['incomeAccountNumber'], "")
			Tools.button_click(self, "input_placeholder", "ҮЦКомпаний нэр", DATA['companyName'], "")

		elif window_name == "Дебит карт авах":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар ", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "6 оронтой нэг удаагийн нууц үг хүлээн авах утас", DATA['digitSixPhoneNumber'], "")
			Tools.button_click(self, "input_placeholder", "Холбогдох утасны дугаар", DATA['phoneNumber'], "")
		
		elif window_name == "И-Биллинг үйлчилгээ авах":
			Tools.button_click(self, "input_placeholder", "Үйлчилгээнд бүртгүүлэх данс", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Нууц асуулт", DATA['ebillingService']['secretAnswer'], "")
			Tools.button_click(self, "input_placeholder", "Нууц хариулт", DATA['ebillingService']['secretQuestion'], "")
			Tools.button_click(self, "input_placeholder", "Төлбөр төлөх байгууллагын нэр 1", DATA['ebillingService']['paymentCompanyName'], "")
			Tools.button_click(self, "input_placeholder", "Төлбөрийн код 1", DATA['ebillingService']['paymentNumberOne'], "")
			Tools.button_click(self, "input_placeholder", "Үйлчилгээний төрөл 1", DATA['ebillingService']['serviceTypeOne'], "")
			Tools.button_click(self, "input_placeholder", "Төлбөр төлөх данс 1",  DATA['ebillingService']['paymentAccount'], "")
			Tools.button_click(self, "input_placeholder", "Төлбөр суутгах өдөр 1", DATA['ebillingService']['paymentDay'], "")
			Tools.button_click(self, "input_placeholder", "Төлбөр төлөх дээд хэмжээ 1", DATA['ebillingService']['paymentMaxAmount'], "")
		
		elif window_name == "Интернэт банкны үйлчилгээ авах":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар 1", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")
		
		elif window_name == "Мобайл банк авах":
			Tools.button_click(self, "input_placeholder", "Утасны дугаар", DATA['phoneNumber'], "")
			Tools.button_click(self, "input_placeholder", "Дансны дугаар ", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")
			Tools.button_click(self, "input_placeholder", "Данс идэвхжүүлэх код", DATA['activeCodeAccount'], "")
		
		elif window_name == "Телефон банкны үйлчилгээ авах":
			Tools.button_click(self, "input_placeholder", "Үйлчилгээ авах утасны дугаар", DATA['getSerivcePhoneNumber'], "")
			Tools.button_click(self, "input_placeholder", "Дансны дугаар 1", DATA['accountNumber'], "")
		
		elif window_name == "Ухаалаг мэдээ үйлчилгээ авах":
			Tools.button_click(self, "input_placeholder", "Бүртгүүлэх утасны  дугаар ", DATA['phoneNumber'], "")
			Tools.button_click(self, "input_placeholder", "Дансны дугаар 1", DATA['accountNumber'], "")
		
		elif window_name == "Хадгаламжийн дуусах хугацааны мэдээллийг имэйлээр хүргүүлэх ":
			Tools.button_click(self, "input_placeholder", "Дансны дугаар 1", DATA['accountNumber'], "")
			Tools.button_click(self, "input_placeholder", "Имэйл хаяг", DATA['email'],"")
		
		elif window_name == "Хуримтлалын үйлчилгээ авах":
			Tools.button_click(self, "input_placeholder", "Хуримтлал шилжүүлэх дансны дугаар", DATA['accountNumber'], "")
		
		else:
			Tools.button_click(self, "input_placeholder", "Дансны дугаар", consts.ACCOUNTS["DEPOSIT_ACCOUNT"], "")

		Tools.button_click(self, "//button[text()=' Гэрээ, маягт бэлтгэх ']", "click", "",By.XPATH)
		# WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'БҮАА Зөвшөөрөл')]")))

	def account_balance_guarantee(self):
		driver = self.driver
		WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.CLASS_NAME, "fancytree-checkbox")))
		driver.find_elements_by_class_name('fancytree-checkbox')[0].click()
		Tools.button_click(self, "//button[text()='Үргэлжлүүлэх ']", "click", "",By.XPATH)
		WebDriverWait(driver,timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//label[text()="Дансны дугаар :"]')))
		driver.find_element_by_class_name('select2-selection').click()
		ActionChains(driver).send_keys(" 5084292318").perform()
		ActionChains(driver).send_keys(Keys.RETURN).perform()
		driver.find_element_by_class_name('icon-calendar22').click()
		driver.find_element(By.CLASS_NAME, "applyBtn" ).click()
		driver.execute_script("""document.querySelector('.input-group-addon').parentElement.children[0].value = "20100430 - 20200930" """)
		Tools.button_click(self, "//button[text()=' Үлдэгдлийн баталгаа бэлтгэх ']", "click", "",By.XPATH)
		time.sleep(2)
		
	def select_etc_document(self, document, operation):
		driver = self.driver
		
		if document == "Данс нээх":
			Tools.button_click(self, 'body > app-root > app-main > div > div > div > div.content > lib-manage-category > div.row > div > div > div.panel-body > lib-fancy-tree > div > ul > li > ul > li:nth-child(7) > ul > li:nth-child(1) > span', "move", "", By.CSS_SELECTOR)
			ActionChains(driver).move_to_element(driver.find_element_by_css_selector('body > app-root > app-main > div > div > div > div.content > lib-manage-category > div.row > div > div > div.panel-body > lib-fancy-tree > div > ul > li > ul > li:nth-child(7) > ul > li:nth-child(1) > span > span.fancytree-title')).context_click().perform()
		elif document == "Дансны үлдэгдлийн баталгаа ":
			Tools.button_click(self, 'body > app-root > app-main > div > div > div > div.content > lib-manage-category > div.row > div > div > div.panel-body > lib-fancy-tree > div > ul > li > ul > li:nth-child(3) > ul > li:nth-child(1) > span > span.fancytree-title', "move", "", By.CSS_SELECTOR)
			ActionChains(driver).move_to_element(driver.find_element_by_css_selector('body > app-root > app-main > div > div > div > div.content > lib-manage-category > div.row > div > div > div.panel-body > lib-fancy-tree > div > ul > li > ul > li:nth-child(3) > ul > li:nth-child(1) > span > span.fancytree-title')).context_click().perform()
		elif document == "Данс нээх ":
			Tools.button_click(self, 'body > app-root > app-main > div > div > div > div.content > lib-manage-category > div.row > div > div > div.panel-body > lib-fancy-tree > div > ul > li > ul > li:nth-child(6) > span > span.fancytree-title', "move", "", By.CSS_SELECTOR)
			target = driver.find_element_by_css_selector('body > app-root > app-main > div > div > div > div.content > lib-manage-category > div.row > div > div > div.panel-body > lib-fancy-tree > div > ul > li > ul > li:nth-child(6) > span > span.fancytree-title')
			target.location_once_scrolled_into_view
			ActionChains(driver).move_to_element(driver.find_element_by_css_selector('body > app-root > app-main > div > div > div > div.content > lib-manage-category > div.row > div > div > div.panel-body > lib-fancy-tree > div > ul > li > ul > li:nth-child(6) > span > span.fancytree-title')).context_click().perform()
		else:
			Tools.button_click(self, '//*[text()="{}"]'.format(document), "move", "", By.XPATH)
			ActionChains(driver).move_to_element(driver.find_element_by_xpath('//span[text()="{}"]'.format(document))).context_click().perform()
		WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="{}"]'.format(operation))))
		driver.find_element_by_xpath('//*[text()="{}"]'.format(operation)).click()
		

		
	def etc_document(self, operation):
		driver = self.driver
		if operation == "add source":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
			driver.find_element_by_xpath('//button[text()=" Сурвалж нэмэх "]').click()
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Нэмэх "]')))
			driver.find_element_by_xpath('//*[@id="add-source-modal"]/div/div/div[2]/div/select').click()
			ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
			ActionChains(driver).send_keys(Keys.RETURN).perform()
			# driver.find_element_by_xpath("//option[text()='Дансны мэдээллүүд ']").click()
			driver.find_element_by_xpath('//button[text()="Нэмэх "]').click()
			
		elif operation == "delete source":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#sources > div > div.row > div > div > table > tbody > tr:nth-child(1) > td.text-right > button > i")))
			len_max = driver.execute_script('''return document.getElementById("sources").querySelector(".table-responsive").getElementsByTagName("tr").length - 1''')
			print(len_max)
			driver.execute_script('''document.getElementById('sources').getElementsByTagName('button')[{}].click()'''.format(len_max))
			
		elif operation == "add field":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
			import random, string
			driver.find_element_by_xpath('//button[text()=" Нэмэлт тайлбар нэмэх "]').click()
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Хадгалах "]')))
			driver.find_element_by_xpath("//input[@placeholder='Нэр']").send_keys(''.join(random.choice(string.ascii_uppercase) for _ in range(5)).lower())
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//option[text()='register ']")))
			driver.find_element_by_xpath("//option[text()='register ']").click()
			driver.find_element_by_xpath('//button[text()=" Хадгалах "]').click()
		
		elif operation == "edit field":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//*[text()=" Засах "]')))
			driver.execute_script('''
			var table_rows = document.getElementById('additional-variables').getElementsByTagName('tr');
			table_rows[table_rows.length - 1].getElementsByTagName('button')[0].click()
			''')
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Хадгалах "]')))
			driver.find_element_by_xpath('//button[text()=" Хадгалах "]').click()
		# < >:
		elif operation == "delete field":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="additional-variables"]/div/div[2]/table/tbody/tr[1]/td[4]/button[2]')))
			driver.execute_script('''
			var table_rows = document.getElementById('additional-variables').getElementsByTagName('tr');
			table_rows[table_rows.length - 1].getElementsByTagName('button')[1].click()
						''')
		
		elif operation == "change order":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Дарааллыг хадгалах "]')))
			driver.find_element_by_xpath('//button[text()=" Дарааллыг хадгалах "]').click()
			
		elif operation == "document inputs":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="document-inputs"]/div/div[1]/table/tbody/tr[1]/td[5]/button[1]')))
			driver.find_element_by_xpath('//*[@id="document-inputs"]/div/div[1]/table/tbody/tr[1]/td[5]/button[1]').click()
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#document-source-variable-modal > div > div > div.modal-footer > button.btn.btn-primary')))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Харагдах нэр"]')))
			driver.find_element_by_xpath('//input[@placeholder="Харагдах нэр"]').clear()
			driver.find_element_by_xpath('//input[@placeholder="Харагдах нэр"]').send_keys('customerregister')
			driver.find_element_by_css_selector('#document-source-variable-modal > div > div > div.modal-footer > button.btn.btn-primary').click()

		elif operation == "document inputs empty":
			for x in range(10):
				content = ""
				try:
					content = driver.execute_script("""return document.querySelector("#document-inputs > div > div.alert.alert-warning.alert-styled-left").textContent""")
				except Exception:
					print("error")
				if content == " Шаардагдах утгууд олдсонгүй. ":
					break
				time.sleep(1)

		elif operation == "edit-html":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//*[text()=" Засах "]')))
			# WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//*[text()=" Бичиг баримтын оролт"]')))
			# driver.find_element_by_class_name('note-editable').find_element_by_tag_name('table').send_keys('test')
			driver.find_elements_by_xpath('//button[text()=" Хадгалах "]')[1].click()
		
		elif operation == "add-related-form":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_all_elements_located((By.TAG_NAME, "tr")))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_all_elements_located((By.TAG_NAME, "option")))
			target = driver.find_element_by_css_selector('#document-relations > div > div.row > div > table > thead > tr > th.text-right > button')
			target.location_once_scrolled_into_view
			Tools.button_click(self, '/html/body/app-root/app-main/div/div/div/div[3]/lib-manage-doc/div[5]/div[1]/lib-manage-document-relation/div[1]/div/div[1]/div/table/thead/tr/th[3]/button', "click", "", By.XPATH)
			Tools.button_click(self, '//*[@id="add-document-modal"]/div/div/div[3]/button[2]', "click", "", By.XPATH)
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="document-relations"]/div/div[2]/button')))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
			Tools.button_click(self, '//*[@id="document-relations"]/div/div[2]/button', "click", "", By.XPATH)
			
		elif operation == "change-configs":
			import random, string
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Түлхүүр үг"]')))
			driver.find_element_by_xpath('//input[@placeholder="Түлхүүр үг"]').clear()
			driver.find_element_by_xpath('//input[@placeholder="Түлхүүр үг"]').send_keys(''.join(random.choice(string.ascii_uppercase) for _ in range(8)).lower())
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="document-settings"]/div/div[4]/select')))
			driver.find_elements_by_xpath('//button[text()=" Хадгалах "]')[3].click()
		
		elif operation == "add group":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Хадгалах "]')))
			driver.find_element_by_xpath('//input[@placeholder="Нэр"]').send_keys('testing')
			driver.find_element_by_xpath('//button[text()=" Хадгалах "]').click()
		
		elif operation == "edit group":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Хадгалах "]')))
			driver.find_element_by_xpath('//button[text()=" Хадгалах "]').click()
		
		elif operation == "add document":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Хадгалах "]')))
			driver.find_element_by_xpath('//input[@placeholder="Нэр"]').send_keys('testing123')
			driver.find_element_by_xpath('//span[text()=" Бүлэг "]').click()
			ActionChains(driver).send_keys('testing').perform()
			ActionChains(driver).send_keys(Keys.RETURN).perform()
			driver.find_element_by_xpath('//option[text()="Байгуулга"]').click()
			driver.find_element_by_xpath('//option[text()="Монгол"]').click()
			driver.find_element_by_xpath('//option[text()="35000"]').click()
			driver.find_element_by_xpath('//button[text()=" Хадгалах "]').click()
		
		elif operation == "edit document":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Хадгалах "]')))
			driver.find_element_by_xpath('//button[text()=" Хадгалах "]').click()
		
		elif operation == "delete document":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Устгах "]')))
			driver.find_element_by_xpath('//button[text()=" Устгах "]').click()
		
		elif operation == "delete document":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Устгах "]')))
			driver.find_element_by_xpath('//button[text()=" Устгах "]').click()
	
	def document_is_deleted(self):
		driver = self.driver
		try:
			driver.find_element_by_xpath('//*[text()="testing123 "]')
			return False
		except:
			return True
	
	def group_is_deleted(self):
		driver = self.driver
		try:
			driver.find_element_by_xpath('//*[text()="testing "]')
			return False
		except:
			return True

def index_finder(self, text, table_id):
	index = 0
	table_data = self.driver.find_element_by_id(table_id).text.split('\n')[2:-1]
	for data in table_data:
		if text in data:
			break
		else:
			index += 1
	return index
