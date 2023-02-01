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

class Cashdrawer:


    def cash_exchange(self, type):

        driver = self.driver
        if(type == "Change_banknotes"):
            WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn")))
            #driver.find_element(By.XPATH, "//*[contains(text(), 'Дэвсгэрт солих')]").click()
            #Tools.button_click(self, "xpath", "Дэвсгэрт солих", "")
            driver.find_element_by_xpath('//button[text()=" Дэвсгэрт солих "]').click()
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
            Tools.button_click(self, "xpath", " Дэвсгэртийн жагсаалт нээх ", "")
            #time.sleep(5)