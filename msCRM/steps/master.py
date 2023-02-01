from modules.customerServiceController import *
import requests
import urllib3
# import openpyxl
import behave 
import time 
import base64

urllib3.disable_warnings()

@Given('Enter {var_} and {col_name} and {endpoint} and {cases}')
def enterCif(self,var_,col_name,endpoint,cases):
    self.json_body = CustomerService.enterVar(self,var_,col_name,endpoint,cases)

@When('Connect to server {endpoint} and {method}')
def connectToServer(self,endpoint,method):
    CustomerService.connectToServer(self,endpoint,method)

@Then('Result {response}')
def resultResponse(self,response):
    CustomerService.resultResponse(self,response)

@Given('Enter1 {var_} and {col_name} and {endpoint} and {retail}')
def enterRetailCif(self,var_,col_name,endpoint,retail):
    self.json_body = CustomerService.enterRetailVar(self,var_,col_name,endpoint,retail)
