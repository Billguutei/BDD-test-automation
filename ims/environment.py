import pytest
import time
import json
import os
import behave
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from modules.constants import *
from allure_behave.hooks import allure_report


consts = Constant()

settings = {
    "recentDestinations": [{
        "id": "Save as PDF",
        "origin": "local",
        "account": "",
    }],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}
prefs = {
    'printing.print_preview_sticky_settings.appState': json.dumps(settings),
    'savefile.default_directory': "/udata/jenkins/workspace/ims/inquiry/BDD-pipeline-90057/ims/reports/pdf"
}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--kiosk-printing')


# WINDOWS CONFIG
# def before_all(self):
#     self.driver = webdriver.Chrome(chrome_options=chrome_options)
#     self.driver.maximize_window() # Ene ni delgetsiig tomruulna.

# # LINUX CONFIG
def before_all(self):
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    self.driver = webdriver.Chrome(
        consts.DATA["CHROMEDRIVER_PATH"], options=chrome_options)
    self.driver.maximize_window()


def after_all(self):
    self.driver.quit()