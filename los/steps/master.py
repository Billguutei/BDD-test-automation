# -*- coding: UTF-8 -*
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then, step
from allure_behave.hooks import allure_report
from modules.constants import *
from modules.utils import *
import time

constants = Constant()

@when("login to RLOS")
def step(self):
    RLOS.login(self)

@then("check home page loaded")
def step(self):
    RLOS.check_homepage_loaded(self)

@then("open menu shine urgudul uusgeh")
def step(self):
    RLOS.newLoanIngestion(self)

@then("inquiry process")
def step(self):
    RLOS.loanIngestionCategory(self, menuIndicator=1, loanPurpose=5)

@then("scrape our data")
def step(self):
    RLOS.data_scrape(self)

@then("result will be displayed")
def step(self):
    RLOS.result(self)

@given("login url to RLOS")
def step(self):
    self.driver.get("https://192.168.6.142:7001/LOSWebApp/security/login.htm?logOut=yes&from=logedIn")

@when("we provide correct authentication")
def step(self):
    driver = self.driver
    WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.NAME, "login")))
    driver.find_element_by_id('ssoId').send_keys(90057)
    while driver.current_url != constants.urls['home_page']:
        driver.find_element_by_name('password').send_keys('Khaanbank*')
        driver.find_element_by_name('password').click()
        driver.find_element_by_class_name('login').click()


@when("we provide wrong authentication")
def step(self):
    driver = self.driver
    WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.NAME, "login")))
    driver.find_element_by_id('ssoId').send_keys(90057)
    driver.find_element_by_name('password').send_keys('kb2018*')
    driver.find_element_by_name('password').click()
    driver.find_element_by_class_name('login').click()


@then("error will show")
def step(self):
    driver = self.driver 
    try: 
        driver.find_element_by_xpath('//*[text()="User Id or Password is Invalid, Login Un-Successful!"]')
    except: 
            assert driver.current_url == "https://192.168.6.142:7001/LOSWebApp/security/mort_main.htm"

@then("home page will load")
def step(self):
    assert self.driver.current_url == "https://192.168.6.142:7001/LOSWebApp/security/mort_main.htm", "Home Page not loaded"


