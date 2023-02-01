from requests.auth import HTTPBasicAuth
import requests
from modules.utils import *
import time 
import pyautogui

class CustomerService:

    # бусад endpoint-н мэдээлэл өөрчиллөх
    def enterVar(self,number,col_name,endpoint,cases):
        self.json_body = initAPI.get_json_body(self,endpoint,"body")  
        self.cases = initAPI.get_json_body(self,cases,"case")        
        
        return initAPI.set_cases_body(self,col_name,"CUSTOMERSERVICE",endpoint,self.json_body,number)
    
    #server руу холболт үүсгэж байна
    def connectToServer(self,endpoint,method):
        url = initAPI.get_end_point_no_parameter(self,"CUSTOMERSERVICE",endpoint)
        self.response = initAPI.get_methods(self,url,method,self.json_body)
    #Үр дүнгээ шалгах хэсэг
    def resultResponse(self,response):
        response1 = initAPI.get_message(self,self.response.json().get('message'))
        print(self.response.json())
        
    # Иргэн мэдээлэл өөрчиллөх
    def enterRetailVar(self,number,col_name,endpoint,retail):
        self.json_body = initAPI.get_json_body(self,retail,"body")  
        self.cases = initAPI.get_json_body(self,"customer-service","case")        
        
        return initAPI.set_cases_body(self,col_name,"CUSTOMERSERVICE",endpoint,self.json_body,number)
    
        