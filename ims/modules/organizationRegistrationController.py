# -*- coding: UTF-8 -*
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from modules.constants import *
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
import os

date_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
date_time_access = datetime.datetime.now().strftime("%m/%d/%Y")
consts = Constant()


class OrgRegService:

	def configuration(self, type):

		driver = self.driver
		if type == "save configuration":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.CLASS_NAME, "content")))
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Хадгалах"]')))
			time.sleep(5)
			driver.find_element_by_xpath("//*[text()='Хадгалах']").click()
			time.sleep(5)
			    

		elif type == "delete configuration":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.CLASS_NAME, "content")))
			time.sleep(3)
			driver.find_element_by_xpath("//*[text()=' Устгах ']").click()
			time.sleep(1.5)
			driver.find_element_by_xpath("//*[text()='Хадгалах']").click()
		elif type == "add configuration":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.CLASS_NAME, "content")))
			time.sleep(3)
            #driver.find_elements_by_tag_name('option')[-1].click()
			driver.find_element_by_xpath("//*[text()=' Тохиргоо нэмэх ']").click()
            ##zeeliin hugatsaa/sar/
			driver.find_element_by_xpath('/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-configuration/div/form/div[1]/lib-condition-component/div/div[1]/div/form/table/tbody/tr[2]/td[1]/div[1]/select/option[1]').click()
			driver.find_element_by_xpath('/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-configuration/div/form/div[1]/lib-condition-component/div/div[1]/div/form/table/tbody/tr[2]/td[1]/div[2]/select/option[12]').click()
            ##jiliin huu
			driver.find_element_by_xpath('/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-configuration/div/form/div[1]/lib-condition-component/div/div[1]/div/form/table/tbody/tr[2]/td[2]/div/input').send_keys(15)
            #tusgai nuhtsulruu
			driver.find_element_by_xpath('/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-configuration/div/form/div[1]/lib-condition-component/div/div[1]/div/form/table/tbody/tr[2]/td[4]/div/input').send_keys(14)
			driver.find_element_by_xpath('/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-configuration/div/form/div[1]/lib-condition-component/div/div[1]/div/form/table/tbody/tr[2]/td[6]/div/ng-select/div/div/div[2]/input').click()
			ActionChains(driver).send_keys('BR_MANAGER').perform()
			ActionChains(driver).send_keys(Keys.ENTER).perform()
			driver.find_element_by_xpath('/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-configuration/div/form/div[1]/lib-condition-component/div/div[1]/div/form/table/tbody/tr[2]/td[7]/div/input').send_keys('09012020')
			driver.find_element_by_xpath("//*[text()='Хадгалах']").click()

	def supervisorlist(self, type):

		driver = self.driver
		if type == "add":
			driver.find_element_by_xpath("//*[text()=' Албан тушаалтан нэмэх ']").click()
			driver.find_element_by_xpath("/html/body/modal[3]/div/div/div[1]/div[2]/form/div[1]/div[2]/div/input").send_keys(consts.USER['FIRST_NAME'])
			driver.find_element_by_xpath("/html/body/modal[3]/div/div/div[1]/div[2]/form/div[1]/div[3]/div/input").send_keys("ddd")
			driver.find_element_by_xpath("/html/body/modal[3]/div/div/div[1]/div[2]/form/div[1]/div[4]/div/input").send_keys(consts.DATA['CHOOSE_PRODUCT'])
			driver.find_element_by_xpath("/html/body/modal[3]/div/div/div[1]/div[2]/form/div[1]/div[5]/div/input").send_keys(consts.DATA['BRANCH'])
			driver.find_element_by_xpath('/html/body/modal[3]/div/div/div[1]/div[2]/form/div[1]/div[6]/div/div/select/option[1]').click()
			driver.find_element_by_xpath("//*[text()=' Хадгалах ']").click()

		elif type == "edit":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.CLASS_NAME, "content")))
			driver.execute_script('document.querySelector("#loading-container > div > div.row > div > div > table > tbody > tr:nth-child(3) > td:nth-child(6) > div > button.btn.btm-sm.btn-info > i").click()')
			time.sleep(3)
			WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), ' Баталгаажуулах албан тушаалтан ')]")))
			driver.find_element_by_xpath("/html/body/modal[3]/div/div/div[1]/div[2]/form/div[1]/div[3]/div/input").clear()
			driver.find_element_by_xpath("/html/body/modal[3]/div/div/div[1]/div[2]/form/div[1]/div[3]/div/input").send_keys("asdqwerty")
			driver.find_element_by_xpath("//*[text()=' Шинэчлэх ']").click()
			time.sleep(5)
		elif type == "delete":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.CLASS_NAME, "content")))
			driver.execute_script('document.querySelector("#loading-container > div > div.row > div > div > table > tbody > tr:nth-child(3) > td:nth-child(6) > div > button.btn.btn-extend.btn-danger.ml-1 > i").click()')
			driver.find_element_by_xpath("//*[text()=' Тийм ']").click()
			time.sleep(3)

	def createContract(self, type):

		driver = self.driver
		if type == "general conditions":
			time.sleep(2)
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[4]/div/input").send_keys("Khaanhuu")
			#baiguullaga ner
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[4]/div/input").send_keys("Khaanhuu")
			#baiguullaga register
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[5]/div/input").send_keys("345435435356")
			time.sleep(2)
			#uil ajilllagani medeelel
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[6]/div/div[2]/div/div/select/option[1]").click()
			time.sleep(2)
			#uil ajilllagani medeelel2
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[6]/div/div[3]/div/div/select/option[1]").click()
			time.sleep(2)
			#uil ajilllagani chiglel tailbar
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[6]/div/div[4]/div/textarea").send_keys("gambushin nz ohin")
			time.sleep(2)
			#baig hayg hot aimg
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[8]/div/div[1]/div/div/select/option[22]").click()
			time.sleep(2)
			#uil ajilllagani chiglel tailbar
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[6]/div/div[4]/div/textarea").send_keys("gambushin nz ohin")
			time.sleep(2)
			#сум/дүүрэг
			driver.find_element_by_xpath("//html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[8]/div/div[2]/div/input").send_keys("Хан-уул")
			time.sleep(2)
			#хороо
			driver.find_element_by_xpath("//html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[8]/div/div[3]/div/input").send_keys(9)
			time.sleep(2)
			#Байгууллагын утас
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[9]/div/input").send_keys(88475417)
			time.sleep(2)
			#Захирлын овог
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[10]/div/input").send_keys("Баатарсүрэнгийн аавын хүү")
			time.sleep(2)
			#Захирлын Нэр
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[11]/div/input").send_keys("Баатарсүрэнгийн аавын хүү")
			time.sleep(2)
			#Няхтлан воодгчын воог
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[12]/div/input").send_keys("Баатарсүрэнгийн аавын хүү")
			time.sleep(2)
			#Няхтлан воодгчын намаэ
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[13]/div/input").send_keys("Баатарсүрэнгийн аавын хүү")
			time.sleep(2)
			#internet bank ashigladag esh
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[14]/div/div/label[2]/input").click()
			time.sleep(2)
			#Нийт ажилчд
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[15]/div/input").send_keys(2)
			time.sleep(2)
			#gereeni hugatsaa/sar
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[2]/org-contract-form/form/div[1]/div[4]/div/input").send_keys(24)
			time.sleep(2)
			#uilchilgeeni nuhtsul
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[2]/org-contract-form/form/div[1]/div[6]/div/div/select/option[2]").click()
			time.sleep(2)
			#automataar sungah eseh
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[2]/org-contract-form/form/div[1]/div[7]/div/div/select/option[2]").click()
			time.sleep(2)
			#gereend oruulah
			#alda zaaj bga heseg
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[2]/org-contract-form/form/div[2]/div[1]/lib-condition-component/div/div/div/form/table/tbody/tr[1]/td[10]/input").click()
			time.sleep(2)
			#gereend oruulah
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[2]/org-contract-form/form/div[3]/div/div/textarea").send_keys("bosa olon ulsiin tsumiin zevseg naimaalagch allah akbar tsai ch goyshu")
			time.sleep(2)
			#tsalingiin sanhuujilt
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[2]/org-contract-form/form/div[4]/div[1]/div/div/label[2]/input").click()
			time.sleep(2)
			#tsalingiin sanhuujilt ulailt uusgej boloh eseh
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[2]/org-contract-form/form/div[4]/div[2]/div/div/label[2]/input").click()
			time.sleep(2)
			#tsalingiin sanhuujilt ulailt uusgeh eseh boloh
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[2]/org-contract-form/form/div[4]/div[3]/div/div/label[2]/input").click()
			time.sleep(2)
			#ajiltnii ovog
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[3]/org-granted-user/div/div[2]/div/form/table/tbody/tr/td[1]/div/input").send_keys("ovogshte")
			time.sleep(2)
			#ajiltnii ner
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[3]/org-granted-user/div/div[2]/div/form/table/tbody/tr/td[2]/div/input").send_keys("ovogshte")
			time.sleep(2)
			#alban tushaal
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[3]/org-granted-user/div/div[2]/div/form/table/tbody/tr/td[3]/div/input").send_keys("ovogshte")
			time.sleep(2)
			#tsahim shuudan
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[3]/org-granted-user/div/div[2]/div/form/table/tbody/tr/td[4]/div/input").send_keys("oasvogshteee@gmail.com")
			driver.find_element_by_xpath("//*[text()=' Гэрээ байгуулах ']").click()
			driver.execute_script("document.getElementsByClassName('btn')[3].click()")
			time.sleep(10)

		elif type == "special conditions":
			time.sleep(2)
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[4]/div/input").send_keys("Khaanhuu")
			#baiguullaga ner
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[4]/div/input").send_keys("Khaanhuu")
			#baiguullaga register
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[5]/div/input").send_keys("345435435355")
			time.sleep(2)
			#uil ajilllagani medeelel
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[6]/div/div[2]/div/div/select/option[1]").click()
			time.sleep(2)
			#uil ajilllagani medeelel2
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[6]/div/div[3]/div/div/select/option[1]").click()
			time.sleep(2)
			#uil ajilllagani chiglel tailbar
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[6]/div/div[4]/div/textarea").send_keys("gambushin nz ohin")
			time.sleep(2)
			#baig hayg hot aimg
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[8]/div/div[1]/div/div/select/option[22]").click()
			time.sleep(2)
			#uil ajilllagani chiglel tailbar
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[6]/div/div[4]/div/textarea").send_keys("gambushin nz ohin")
			time.sleep(2)
			#сум/дүүрэг
			driver.find_element_by_xpath("//html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[8]/div/div[2]/div/input").send_keys("Хан-уул")
			time.sleep(2)
			#хороо
			driver.find_element_by_xpath("//html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[8]/div/div[3]/div/input").send_keys(9)
			time.sleep(2)
			#Байгууллагын утас
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[9]/div/input").send_keys(88475417)
			time.sleep(2)
			#Захирлын овог
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[10]/div/input").send_keys("Баатарсүрэнгийн аавын хүү")
			time.sleep(2)
			#Захирлын Нэр
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[11]/div/input").send_keys("Баатарсүрэнгийн аавын хүү")
			time.sleep(2)
			#Няхтлан воодгчын воог
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[12]/div/input").send_keys("Баатарсүрэнгийн аавын хүү")
			time.sleep(2)
			#Няхтлан воодгчын намаэ
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[13]/div/input").send_keys("Баатарсүрэнгийн аавын хүү")
			time.sleep(2)
			#internet bank ashigladag esh
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[14]/div/div/label[2]/input").click()
			time.sleep(2)
			#Нийт ажилчд
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[15]/div/input").send_keys(2)
			time.sleep(2)
			#gereeni hugatsaa/sar
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[2]/org-contract-form/form/div[1]/div[4]/div/input").send_keys(24)
			time.sleep(2)
			#uilchilgeeni nuhtsul tusgai nuhtsul
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[2]/org-contract-form/form/div[1]/div[6]/div/div/select/option[1]").click()
			time.sleep(2)
			#gereend oruulah
			#alda zaaj bga heseg
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[2]/org-contract-form/form/div[2]/div[1]/lib-condition-component/div/div/div/form/table/tbody/tr[1]/td[10]/input").click()
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[2]/org-contract-form/form/div[2]/div[1]/lib-condition-component/div/div/div/form/table/tbody/tr[2]/td[10]/input").click()
			time.sleep(2)
			#gereend oruulah
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[2]/org-contract-form/form/div[3]/div/div/textarea").send_keys("bosa olon ulsiin tsumiin zevseg naimaalagch allah akbar tsai ch goyshu")
			time.sleep(2)
			#tsalingiin sanhuujilt
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[2]/org-contract-form/form/div[4]/div[1]/div/div/label[2]/input").click()
			time.sleep(2)
			#tsalingiin sanhuujilt ulailt uusgej boloh eseh
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[2]/org-contract-form/form/div[4]/div[2]/div/div/label[2]/input").click()
			time.sleep(2)
			#tsalingiin sanhuujilt ulailt uusgeh eseh boloh
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[2]/org-contract-form/form/div[4]/div[3]/div/div/label[2]/input").click()
			time.sleep(2)
			#ajiltnii ovog
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[3]/org-granted-user/div/div[2]/div/form/table/tbody/tr/td[1]/div/input").send_keys("ovogshte")
			time.sleep(2)
			#ajiltnii ner
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[3]/org-granted-user/div/div[2]/div/form/table/tbody/tr/td[2]/div/input").send_keys("ovogshte")
			time.sleep(2)
			#alban tushaal
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[3]/org-granted-user/div/div[2]/div/form/table/tbody/tr/td[3]/div/input").send_keys("ovogshte")
			time.sleep(2)
			#tsahim shuudan
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[3]/org-granted-user/div/div[2]/div/form/table/tbody/tr/td[4]/div/input").send_keys("oasvogshteeeee@gmail.com")
			driver.find_element_by_xpath("//*[text()=' Гэрээ байгуулах ']").click()
			driver.execute_script("document.getElementsByClassName('btn')[3].click()")
			time.sleep(10)
		elif type == "pay transfer":

			time.sleep(2)
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[4]/div/input").send_keys("Khaanhuu")
			#baiguullaga ner
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[4]/div/input").send_keys("Khaanhuu")
			#baiguullaga register
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[5]/div/input").send_keys("345435435361")
			time.sleep(2)
			#uil ajilllagani medeelel
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[6]/div/div[2]/div/div/select/option[1]").click()
			time.sleep(2)
			#uil ajilllagani medeelel2
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[6]/div/div[3]/div/div/select/option[1]").click()
			time.sleep(2)
			#uil ajilllagani chiglel tailbar
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[6]/div/div[4]/div/textarea").send_keys("gambushin nz ohin")
			time.sleep(2)
			#baig hayg hot aimg
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[8]/div/div[1]/div/div/select/option[22]").click()
			time.sleep(2)
			#uil ajilllagani chiglel tailbar
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[6]/div/div[4]/div/textarea").send_keys("gambushin nz ohin")
			time.sleep(2)
			#сум/дүүрэг
			driver.find_element_by_xpath("//html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[8]/div/div[2]/div/input").send_keys("Хан-уул")
			time.sleep(2)
			#хороо
			driver.find_element_by_xpath("//html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[8]/div/div[3]/div/input").send_keys(9)
			time.sleep(2)
			#Байгууллагын утас
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[9]/div/input").send_keys(88475417)
			time.sleep(2)
			#Захирлын овог
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[10]/div/input").send_keys("Баатарсүрэнгийн аавын хүү")
			time.sleep(2)
			#Захирлын Нэр
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[11]/div/input").send_keys("Баатарсүрэнгийн аавын хүү")
			time.sleep(2)
			#Няхтлан воодгчын воог
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[12]/div/input").send_keys("Баатарсүрэнгийн аавын хүү")
			time.sleep(2)
			#Няхтлан воодгчын намаэ
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[13]/div/input").send_keys("Баатарсүрэнгийн аавын хүү")
			time.sleep(2)
			#internet bank ashigladag esh
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[14]/div/div/label[2]/input").click()
			time.sleep(2)
			#Нийт ажилчд
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[1]/org-information/form/div/div/div/div[15]/div/input").send_keys(2)
			time.sleep(2)
			#gereeni hugatsaa/sar
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[2]/org-contract-form/form/div[1]/div[4]/div/input").send_keys(24)
			time.sleep(2)
			#uilchilgeeni nuhtsul tsalin damjuulah
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[2]/org-contract-form/form/div[1]/div[6]/div/div/select/option[3]").click()
			time.sleep(2)
			#automataar sungah eseh
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[2]/org-contract-form/form/div[1]/div[7]/div/div/select/option[2]").click()
			#gereend oruulah
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[2]/org-contract-form/form/div[3]/div/div/textarea").send_keys("bosa olon ulsiin tsumiin zevseg naimaalagch allah akbar tsai ch goyshu")
			time.sleep(2)
			#ajiltnii ovog
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[3]/org-granted-user/div/div[2]/div/form/table/tbody/tr/td[1]/div/input").send_keys("ovogshte")
			time.sleep(2)
			#ajiltnii ner
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[3]/org-granted-user/div/div[2]/div/form/table/tbody/tr/td[2]/div/input").send_keys("ovogshte")
			time.sleep(2)
			#alban tushaal
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[3]/org-granted-user/div/div[2]/div/form/table/tbody/tr/td[3]/div/input").send_keys("ovogshte")
			time.sleep(2)
			#tsahim shuudan
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-form/div/div[3]/org-granted-user/div/div[2]/div/form/table/tbody/tr/td[4]/div/input").send_keys("oaasdsvogshteeeeee@gmail.com")
			driver.find_element_by_xpath("//*[text()=' Гэрээ байгуулах ']").click()
			driver.execute_script("document.getElementsByClassName('btn')[3].click()")
			time.sleep(10)

	def organizationlist(self, type):

		driver = self.driver
		if type == "inquire contract":
			WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Хайлт хийх"]')))
			driver.execute_script('document.querySelector("#loading-container > div > div.row > div:nth-child(2) > div > table > tbody > tr:nth-child(17) > td:nth-child(11) > div > button.btn.btn-primary.mr-1 > i").click()')
			driver.execute_script('document.querySelector("#modal-form-loading > div:nth-child(1) > div.item-head.d-flex.text-left > div.color-green").click()')
			time.sleep(3)
		elif type == "inquire conditionally":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.CLASS_NAME, "content")))
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-list/div/div/div[2]/div[1]/div/div[2]/div[2]/select/option[2]").click()
			time.sleep(3)

		elif type == "inquire by status":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.CLASS_NAME, "content")))
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-list/div/div/div[2]/div[1]/div/div[2]/div[1]/select/option[5]").click()
			time.sleep(3)

		elif type == "print a contract":
			WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.CLASS_NAME, "content")))
			driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/lib-organization/lib-organization-list/div/div/div[2]/div[2]/div/table/tbody/tr[4]/td[11]/div/button[2]/i").click()
			time.sleep(3)
			driver.switch_to_window(driver.window_handles[-1])
			select = driver.execute_script("return document.querySelector('print-preview-app').shadowRoot.querySelector('print-preview-sidebar').shadowRoot.querySelector('print-preview-destination-settings').root.querySelector('print-preview-destination-select').root.querySelector('select.md-select');") 
			options = select.find_elements_by_tag_name('option')
			save_pdf_by_index = [x.text for x in options].index('    Save as PDF\n  ' )
			options[save_pdf_by_index].click()
			time.sleep(3)
			driver.execute_script('document.querySelector("body > print-preview-app").shadowRoot.querySelector("#sidebar").shadowRoot.querySelector("print-preview-button-strip").shadowRoot.querySelector("cr-button.action-button").click();')
			time.sleep(5)
			pyautogui.press('enter')
			time.sleep(10)
