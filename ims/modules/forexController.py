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

date_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
consts = Constant()


# main class of CardController
class forex:

    def approved_deals(self):
        driver = self.driver
        Tools.button_click(self, "//*[@id='deal_approved_table']/tbody/tr", "click", "", By.XPATH)