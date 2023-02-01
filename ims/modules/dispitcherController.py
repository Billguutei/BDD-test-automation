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

class Dispitcher:


    def dispitcher_setting(self, type):

        driver = self.driver
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//span[@title=" Данс сонгоно уу! "]')))
        ActionChains(driver).move_to_element(driver.find_element_by_xpath('//span[@title=" Данс сонгоно уу! "]')).click().perform()
        ActionChains(driver).send_keys('5010023735').perform()
        ActionChains(driver).send_keys(Keys.ENTER).perform()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'table')))
        if type == "add account":
            ActionChains(driver).move_to_element(driver.find_element_by_xpath('//span[@title=" Банк доторх "]')).click().perform()
            ActionChains(driver).send_keys('Банк доторх').perform()
            ActionChains(driver).send_keys(Keys.ENTER).perform()
            driver.find_element_by_xpath('//input[@placeholder="Хүлээн авах данс"]').send_keys(consts.ACCOUNTS['TO_ACCOUNT'])
            driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэг хийх хувь"]').send_keys(consts.DATA['TRANSFER_PERCENT'])
            ActionChains(driver).move_to_element(driver.find_element_by_xpath('//span[@title=" Сар бүрийн эцэст "]')).click().perform()
            ActionChains(driver).send_keys(' Сар бүрийн эцэст ').perform()
            ActionChains(driver).send_keys(Keys.ENTER).perform()
            ActionChains(driver).move_to_element(driver.find_element_by_xpath('//span[@title=" 2019 "]')).click().perform()
            ActionChains(driver).send_keys(' 2020').perform()
            ActionChains(driver).send_keys(Keys.ENTER).perform()
            ActionChains(driver).move_to_element(driver.find_element_by_xpath('//span[@title=" 10-р сар "]')).click().perform()
            ActionChains(driver).send_keys(' 11-р сар ').perform()
            ActionChains(driver).send_keys(Keys.ENTER).perform()
            time.sleep(5)
            #Tools.button_click(self, "xpath", "", "")
            Tools.button_click(self, '//button[text()=" Данс нэмэх "]', "click", "",By.XPATH)
            time.sleep(3)

        elif type == "add account transaction type external":
            ActionChains(driver).move_to_element(driver.find_element_by_xpath('//span[@title=" Банк доторх "]')).click().perform()
            ActionChains(driver).send_keys(' Банк хооронд ').perform()
            ActionChains(driver).send_keys(Keys.ENTER).perform()
            driver.find_element_by_xpath('/html/body/app-root/app-main/div/div/div/div[3]/lib-settings-dispatcher/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div[2]/lib-payment-bank/div/div/lib-select/div/span/span[1]/span').click()
            driver.find_element_by_css_selector('body > span > span > span.select2-search.select2-search--dropdown > input').send_keys("300000")
            ActionChains(driver).send_keys(Keys.ENTER).perform()
            driver.find_element_by_xpath('//input[@placeholder="Хүлээн авах данс"]').send_keys(consts.ACCOUNTS['TO_ACCOUNT'])
            driver.find_element_by_xpath("//input[@placeholder='Дансны нэр']").send_keys(consts.USER["FIRST_NAME"])
            driver.find_element_by_xpath('//input[@placeholder="Шилжүүлэг хийх хувь"]').send_keys(consts.DATA['TRANSFER_PERCENT'])
            ActionChains(driver).move_to_element(driver.find_element_by_xpath('//span[@title=" Сар бүрийн эцэст "]')).click().perform()
            ActionChains(driver).send_keys(' Сар бүрийн эцэст ').perform()
            ActionChains(driver).send_keys(Keys.ENTER).perform()
            ActionChains(driver).move_to_element(driver.find_element_by_xpath('//span[@title=" 2019 "]')).click().perform()
            ActionChains(driver).send_keys(' 2020').perform()
            ActionChains(driver).send_keys(Keys.ENTER).perform()
            ActionChains(driver).move_to_element(driver.find_element_by_xpath('//span[@title=" 10-р сар "]')).click().perform()
            ActionChains(driver).send_keys(' 11-р сар ').perform()
            ActionChains(driver).send_keys(Keys.ENTER).perform()
            #Tools.button_click(self, "xpath", "", "")
            Tools.button_click(self, '//button[text()=" Данс нэмэх "]', "click", "",By.XPATH)
            time.sleep(5)
        elif type == "update":
            #Tools.button_click(self, "xpath", "", "")
            time.sleep(3)
            Tools.button_click(self, '//button[text()=" Засах "]', "click", "",By.XPATH)
            ActionChains(driver).move_to_element(driver.find_element_by_xpath('//span[@title=" 9-р сар "]')).click().perform()
            ActionChains(driver).send_keys(' 12-р сар ').perform()
            ActionChains(driver).send_keys(Keys.ENTER).perform()
            #Tools.button_click(self, "xpath", "", "")
            Tools.button_click(self, '//button[text()=" Хадгалах "]', "click", "",By.XPATH)
            time.sleep(5)
        elif type == "delete":
            driver.execute_script("document.getElementsByTagName('tr')[1].getElementsByTagName('button')[0].click()") 
            driver.execute_script("document.querySelector('.modal').getElementsByTagName('button')[2].click()")
            time.sleep(5)

    def dispitcher_report(self):

        driver = self.driver
        ActionChains(driver).move_to_element(driver.find_element_by_xpath('//span[@class="input-group-addon bg-primary cursor-pointer"]')).click().perform()
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[1]/table/thead/tr[1]/th[1]/i').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[1]/table/tbody/tr[1]/td[2]').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[4]').click()
        #Tools.button_click(self, "xpath", "", "")
        Tools.button_click(self, '//button[text()="Сонгох"]', "click", "",By.XPATH)
        driver.find_element_by_xpath('//input[@placeholder="Дансны дугаар"]').send_keys(consts.ACCOUNTS['REPORT_ACCOUNT'])
        #Tools.button_click(self, "xpath", "", "")
        Tools.button_click(self, '//button[text()=" Хайх "]', "click", "",By.XPATH)
        #WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Мэдээлэл алга')]")))
        #WebDriverWait(driver, timeout=30).until(EC.visibility_of_element_located((By.XPATH, "//table[@id='transactionList']")))
        time.sleep(3)
        a = driver.find_element_by_xpath("//table[@id='transactionList']").screenshot_as_png
        with open('./ims/reports/screenshots/screenshot.png', 'wb') as file:
           file.write(a)
           time.sleep(3)

            