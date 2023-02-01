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

from webdriver_manager.chrome import ChromeDriverManager
from allure_behave.hooks import allure_report

CHROMEDRIVER_PATH = '/opt/workspace/chromedriver'

# if __name__ == "__main__":
#     ims_user = os.environ.get('IMS_USER')
#     ims_pass = os.environ.get('IMS_PASS')


def before_all(self):
    chrome_options = webdriver.ChromeOptions()

    login = "test"

    # GUI
    chrome_options.add_experimental_option(
        "prefs", {"profile.managed_default_content_settings.images": 2})
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-setuid-sandbox")
    chrome_options.add_argument("--remote-debugging-port=9222")  # this
    chrome_options.add_argument("--disable-dev-shm-using")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("user-data-dir=.\cookies\\" + login)
    chrome_options.add_argument("--headless")

    self.driver = webdriver.Chrome(
        executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    # self.driver = webdriver.Chrome(chrome_options=chrome_options)
    # self.driver.maximize_window()


def after_all(self):

    self.driver.quit()


# allure_report(
#     "/report/")
