import pytest
import time
import behave
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from allure_behave.hooks import allure_report
from modules.constants import *
import json

consts = Constant()

settings = {
    "browser.download.dir": "D:/Work",
    "recentDestinations": [{
        "id": "Save as PDF",
        "origin": "D:/Work",
        "account": "",
    }],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}
prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--kiosk-printing')
chrome_options.add_argument('--ignore-ssl-errors=yes')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--safebrowsing-disable-download-protection')

chrome_options.add_experimental_option("prefs", {
  "download.default_directory": r"D:\Work",
#   "download.prompt_for_download": False,
#   "download.directory_upgrade": True,
#   "safebrowsing.enabled": True
})
# # #WINDOWS CONFIG
def before_all(self):
    self.driver = webdriver.Chrome(consts.DATA["CHROMEDRIVER_PATH"], chrome_options=chrome_options)
    self.driver.maximize_window()

def after_all(self):
      self.driver.quit()
