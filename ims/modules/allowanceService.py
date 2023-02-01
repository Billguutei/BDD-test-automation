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

class Allowance:

    def customer_search(self):
            driver = self.driver
            WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="search"]')))
            driver.find_element_by_xpath('//input[@placeholder="Регистрийн дугаараар хайх"]').send_keys(consts.DATA['ALLOWANCE_REGISTER_NO'])
            driver.find_element_by_xpath("//*[text()='Хайх ']").click()
            WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Олголтын форм')]")))
            time.sleep(3)
            # a = driver.find_element_by_xpath("/html/body/app-root/app-main/div/div/div/div[3]/allowance-manage/div/div/div[1]/div[2]").screenshot_as_png
            # with open('./ims/reports/screenshots/screenshotallowance.png', 'wb') as file:
            #     file.write(a)

    def allowance_report(self):
        driver = self.driver
        driver.execute_script('document.querySelector("body > app-root > app-main > div > div > div > div.content > lib-allowance-list > div > div.panel-body > form > div:nth-child(1) > div > div > div > lib-date-range-picker > div > span > i").click()')
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[1]/table/tbody/tr[1]/td[4]").click()
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[7]").click()
        driver.execute_script('document.querySelector("body > div.daterangepicker.dropdown-menu.ltr.show-calendar.opensleft > div.ranges > div.range_inputs > button.applyBtn.btn.btn-sm.bg-primary").click()')
        driver.find_element_by_xpath("//*[text()=' Тайлан гаргах ']").click()
        time.sleep(10)