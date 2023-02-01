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
# import pandas as pd
import time
import csv
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.policies import DCAwareRoundRobinPolicy
from cassandra.policies import RoundRobinPolicy

consts = Constant()


class RLOS:
    def login(self):
        driver = self.driver
        driver.get(consts.URLS['LOGIN_URL'])

        WebDriverWait(driver, timeout=10).until(
            EC.element_to_be_clickable((By.NAME, "login")))
        driver.find_element_by_id('ssoId').send_keys(consts.AUTH["USERNAME"])
        while driver.current_url != consts.URLS['HOME_PAGE']:
            driver.find_element_by_name('password').send_keys(consts.AUTH["PASSWORD"])
            driver.find_element_by_name('password').click()
            driver.find_element_by_class_name('login').click()

    def check_homepage_loaded(self):
        driver = self.driver
        current_url = driver.current_url
        WebDriverWait(driver, timeout=10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Иргэд")))
        assert current_url == consts.URLS['HOME_PAGE']

    def newLoanIngestion(self):
        self.driver.get(
            'https://192.168.6.142:7001/LOSWebApp/underwriting/newLoanIngestion.htm?fromPage=menu')

    def loanIngestionCategory(self, menuIndicator, loanPurpose):
        driver = self.driver
        WebDriverWait(driver, timeout=10).until(
            EC.element_to_be_clickable((By.ID, "menuIndicator")))

        driver.find_element_by_id('menuIndicator').click()
        for x in range(menuIndicator):
            ActionChains(driver).send_keys(Keys.DOWN).perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()

        driver.find_element_by_id('loanPurpose').click()
        while True:
            try:
                for x in range(loanPurpose):
                    ActionChains(driver).send_keys(Keys.DOWN).perform()
            except:
                pass
            else:
                break

        ActionChains(driver).send_keys(Keys.RETURN).perform()

        for x in range(2):
            driver.find_element_by_id('cifLauncher').click()

        driver.switch_to_frame('popupFrame')
        driver.find_element_by_name('registrationNo').send_keys(
            consts.data['citizen_id'])
        driver.find_element_by_name('bttnSearch').click()

    def data_scrape(self):
        driver = self.driver
        global cif, riskGroup, score

        cif = driver.find_element_by_class_name('coloumnspec').text
        WebDriverWait(driver, timeout=30).until(
            EC.element_to_be_clickable((By.LINK_TEXT, cif)))
        driver.find_element_by_link_text(cif).click()
        WebDriverWait(driver, timeout=30).until(EC.number_of_windows_to_be(2))
        for window in driver.window_handles:
            driver.switch_to_window(window)
            try:
                if driver.find_element_by_name('behavioralRiskGroup').get_attribute('value') != "":
                    riskGroup = driver.find_element_by_name(
                        'behavioralRiskGroup').get_attribute('value')
                    score = driver.find_element_by_id(
                        'behavioralScore').get_attribute('value')
            except:
                continue

    def result(self):
        CIF = cif.split('-')[0]
        auth_provider = PlainTextAuthProvider(
            username='cassandra', password="cassandra")
        cluster = Cluster(["192.168.3.122", "192.168.3.123", "192.168.3.124"], port=9042, auth_provider=auth_provider,
                          protocol_version=4, compression=True, metrics_enabled=False, load_balancing_policy=RoundRobinPolicy())
        session = cluster.connect("b_scoring")

        with open('result.csv', 'a', newline="") as file:
            writer = csv.writer(file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([CIF, riskGroup, score, consts.data['citizen_id']])

        fixed_cif = (16 - len(str(CIF))) * "0" + str(CIF)
        query = session.execute("""
            SELECT cif, riskgroup, score
            FROM bscore WHERE cif = '{}'
        """.format(fixed_cif))

        for data in query:
            print(score, data.score)
            assert int(score) == data.score, (int(score), data.score)
