from selenium import webdriver


def before_all(self):
    self.driver = webdriver.Chrome("C:\\Users\\15974\\Work Folders\\AzureDevops\\BDD%20Test%20Automation\\ims\\drivers\\windows\\chromedriver.exe")
    self.driver.maximize_window()

def after_all(self):
    self.driver.quit()