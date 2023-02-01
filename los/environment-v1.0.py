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
from webdriver_manager.chrome import ChromeDriverManager
from allure_behave.hooks import allure_report

CHROMEDRIVER_PATH = '/opt/workspace/chromedriver'

IE_PATH = "../Drivers/IE_driver/IEDriverServer.exe"

def before_all(self):
    self.driver = webdriver.Ie(executable_path=IE_PATH)
    self.driver.maximize_window()

def after_all(self):
    self.driver.quit()
