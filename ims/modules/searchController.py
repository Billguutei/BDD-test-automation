from modules.constants import *
from modules.utils import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class Search:

    def transaction(self, transaction_type):
        driver = self.driver
        WebDriverWait(driver, timeout=consts.DATA["TIMEOUT"]).until(EC.element_to_be_clickable((By.XPATH, "//span[@title=' № ']")))
        driver.find_element_by_xpath("//span[@title=' № ']").click()
        driver.find_element_by_xpath("//input[@role='textbox']").send_keys(' Гүйлгээ код ')
        driver.find_element_by_xpath("//input[@role='textbox']").send_keys(Keys.ENTER)
        Tools.button_click(self, "input_placeholder", "Шүүх утгаа бичнэ үү...", transaction_type)