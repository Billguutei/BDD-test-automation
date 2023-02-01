import datetime
import time
from modules.constants import *
from modules.utils import Tools
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


#IMS-n Consumer loan - Зээлийн түүх лавлах цэсэнд энэ classaar ашиглаж харилцагч хайж байгаа
consts = Constant()
class consumerLoann:
	
    def inquiryLoanHistory(self, type):
        driver = self.driver
        if type == "cif":
            driver.find_element_by_xpath('//input[@placeholder="Харилцагчийн регистрийн дугаар, cif дугаар"]').send_keys(consts.DATA['CONSUMER_CIF_NO_HIST'])
            Tools.button_click(self, '//button[text()=" Хайх "]', "click", "",By.XPATH)
            
        elif type == "register_no":
            Tools.button_click(self, '//input[@placeholder="Харилцагчийн регистрийн дугаар, cif дугаар"]', "send_keys", consts.DATA['CONSUMER_REG_NO_HIST'],By.XPATH)
            Tools.button_click(self, '//button[text()=" Хайх "]', "click", "",By.XPATH)
            
        elif type == "null":
            Tools.button_click(self, '//input[@placeholder="Харилцагчийн регистрийн дугаар, cif дугаар"]', "send_keys", consts.DATA['CONSUMER_NULL_BOTH'],By.XPATH)
            Tools.button_click(self, '//button[text()=" Хайх "]', "click", "",By.XPATH) 
        
        elif type == "wrongvalue1":
            Tools.button_click(self, '//input[@placeholder="Харилцагчийн регистрийн дугаар, cif дугаар"]', "send_keys", consts.DATA['CONSUMER_WRONGSTRING_BOTH'],By.XPATH)
            Tools.button_click(self, '//button[text()=" Хайх "]', "click", "",By.XPATH)    
        
        elif type == "wrongvalue2":
            Tools.button_click(self, '//input[@placeholder="Харилцагчийн регистрийн дугаар, cif дугаар"]', "send_keys", consts.DATA['CONSUMER_WRONGNUMBER_BOTH'],By.XPATH)
            Tools.button_click(self, '//button[text()=" Хайх "]', "click", "",By.XPATH) 
        
        elif type == "emptyregister":
            Tools.button_click(self, '//input[@placeholder="Харилцагчийн регистрийн дугаар, cif дугаар"]', "send_keys", consts.DATA['CONSUMER_NOTFOUND_REG_CORE_BOTH'],By.XPATH)
            Tools.button_click(self, '//button[text()=" Хайх "]', "click", "",By.XPATH)        

        elif type == "nocheckdigit":
            Tools.button_click(self, '//input[@placeholder="Харилцагчийн регистрийн дугаар, cif дугаар"]', "send_keys", consts.DATA['CONSUMER_NO_CHECKDIGIT_BOTH'],By.XPATH)
            Tools.button_click(self, '//button[text()=" Хайх "]', "click", "",By.XPATH) 
        
        elif type == "nocustomercif":
            Tools.button_click(self, '//input[@placeholder="Харилцагчийн регистрийн дугаар, cif дугаар"]', "send_keys", consts.DATA['CONSUMER_NOTFOUND_CIF_HIST'],By.XPATH)
            Tools.button_click(self, '//button[text()=" Хайх "]', "click", "",By.XPATH) 

        elif type == "customercif":
            Tools.button_click(self, '//input[@placeholder="Харилцагчийн регистрийн дугаар, cif дугаар"]', "send_keys", consts.DATA['CONSUMER_CIF_NO_CUSTOMER'],By.XPATH)
            Tools.button_click(self, '//button[text()=" Хайх "]', "click", "",By.XPATH)  
        
        elif type == "notfound cif":
            Tools.button_click(self, '//input[@placeholder="Харилцагчийн регистрийн дугаар, cif дугаар"]', "send_keys", consts.DATA['CONSUMER_NOTFOUND_CIF_CUSTOMER'],By.XPATH)
            Tools.button_click(self, '//button[text()=" Хайх "]', "click", "",By.XPATH)      

        elif type == "notfound reg":
            Tools.button_click(self, '//input[@placeholder="Харилцагчийн регистрийн дугаар, cif дугаар"]', "send_keys", consts.DATA['CONSUMER_NOTFOUND_REG_CUSTOMER'],By.XPATH)
            Tools.button_click(self, '//button[text()=" Хайх "]', "click", "",By.XPATH)     