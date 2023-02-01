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


class bulk:

	def operation(self, type):

		driver = self.driver
		if type == "show":
			
			Tools.button_click(self, 'icon-calendar22.text-size-small', "click", "", By.CLASS_NAME)
			driver.find_element_by_xpath("//td[text()='23']").click()
			driver.find_element_by_xpath("//td[text()='23']").click()
			driver.find_element_by_xpath("//button[text()='Сонгох']").click()