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

class Report:

    def Acc_def_ded_rep(self):
        driver = self.driver

        driver.find_element(By.XPATH, "//span[@class='input-group-addon bg-primary cursor-pointer']").click()
        
        driver.execute_script("document.querySelector('body > div.daterangepicker.dropdown-menu.ltr.show-calendar.opensleft > div.calendars > div.calendar.left > div.calendar-table > table > thead > tr:nth-child(1) > th.prev.available > i').click()")
        
        driver.execute_script("document.querySelector('body > div.daterangepicker.dropdown-menu.ltr.show-calendar.opensleft > div.calendars > div.calendar.left > div.calendar-table > table > thead > tr:nth-child(1) > th.prev.available > i').click()")
        
        driver.execute_script("document.querySelector('body > div.daterangepicker.dropdown-menu.ltr.show-calendar.opensleft > div.calendars > div.calendar.left > div.calendar-table > table > thead > tr:nth-child(1) > th.prev.available > i').click()")
        
        driver.execute_script("document.querySelector('body > div.daterangepicker.dropdown-menu.ltr.show-calendar.opensleft > div.calendars > div.calendar.left > div.calendar-table > table > thead > tr:nth-child(1) > th.prev.available > i').click()")
        
        driver.execute_script("document.querySelector('body > div.daterangepicker.dropdown-menu.ltr.show-calendar.opensleft > div.calendars > div.calendar.left > div.calendar-table > table > thead > tr:nth-child(1) > th.prev.available > i').click()")
        
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[1]/table/tbody/tr[1]/td[7]').click()
        
        driver.execute_script("document.querySelector('body > div.daterangepicker.dropdown-menu.ltr.show-calendar.opensleft > div.calendars > div.calendar.right > div.calendar-table > table > thead > tr:nth-child(1) > th.next.available > i').click()")
        
        driver.execute_script("document.querySelector('body > div.daterangepicker.dropdown-menu.ltr.show-calendar.opensleft > div.calendars > div.calendar.right > div.calendar-table > table > thead > tr:nth-child(1) > th.next.available > i').click()")
        
        driver.execute_script("document.querySelector('body > div.daterangepicker.dropdown-menu.ltr.show-calendar.opensleft > div.calendars > div.calendar.right > div.calendar-table > table > thead > tr:nth-child(1) > th.next.available > i').click()")
        
        driver.execute_script("document.querySelector('body > div.daterangepicker.dropdown-menu.ltr.show-calendar.opensleft > div.calendars > div.calendar.right > div.calendar-table > table > thead > tr:nth-child(1) > th.next.available > i').click()")
        
        driver.execute_script("document.querySelector('body > div.daterangepicker.dropdown-menu.ltr.show-calendar.opensleft > div.calendars > div.calendar.right > div.calendar-table > table > thead > tr:nth-child(1) > th.next.available > i').click()")
        
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[1]/table/tbody/tr[1]/td[7]').click()
        
        driver.execute_script("document.querySelector('body > div.daterangepicker.dropdown-menu.ltr.show-calendar.opensleft > div.ranges > div.range_inputs > button.applyBtn.btn.btn-sm.bg-primary').click()")
        
        Tools.button_click(self, "xpath", " Тайлан татах /EXCEL/ ", "")
        
        time.sleep(10)