
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import json
import requests

#Хэрэгсэл
class Utilities:
    
    # Шинээр файл болон фолдер үүсгэх
    # файлын бүтэц доорх байдлаар үүсгэх болно
    #    root
    # d1  d2   d3 -> main_dir_names
    # d1  d1   d1 -> main_dir[0,1,2]  
    # d2  d1
    # d3 
    #####################################
    def create_folder_file(self):
        for i in range(0,len(main_dir)):
            for j in range(len(main_dir[i])):
                dirName = str(root_dir) + '/' + str(main_dir_names) + '/' + str(main_dir[i][j])
                try:
                    os.makedirs(dirName)
                except FileExistsError:
                    print("Directory",dirName, "already exist")
                
    # Excel - н мөр болон багана тооллох 
    # @param 1 = файлын нэр  
    # @param 2 = excel - н sheet - н нэр
    # @param 3 = row - мөр тооллох , col - багана тооллох
    def count(file,sheet_name,type):
       
        if type == 'row':
            
            workbook = openpyxl.load_workbook(file)
            sheet = workbook.get_sheet_by_name(sheet_name)
            return sheet.max_row
        
        elif type == 'col':
            
            workbook = openpyxl.load_workbook(file)
            sheet = workbook.get_sheet_by_name(sheet_name)
            return sheet.max_column           
    
    # Excel - руу бичих болон унших
    # @param 1 = файлын нэр 
    # @param 2 = excel - н sheet - н нэр
    # @param 3 = мөрийн тоо
    # @param 4 = баганы тоо
    # @param 5 = Excel руу оруулах өгөгдөл
    # @param 6 = w - Бичих , r - Унших
    def excel_open(file,sheet_name,row_num,col_num,data,type):
        
        if type == 'w':
            
            workbook = openpyxl.load_workbook(r"C:\Users\90059\Desktop\dfpath\da.xlsx")
            sheet = workbook.get_sheet_by_name(sheet_name)
            sheet.cell(row=row_num,column=col_num).value = data
            workbook.save(file)
            
        elif type == 'r':
            
            workbook = openpyxl.load_workbook(file)
            sheet = workbook.get_sheet_by_name(sheet_name)
            return sheet.cell(row=row_num,column=col_num).value         

#devOps
class devOpsInit:
    #devOps руу зураг оруулах
    def get_image(self):
        url_post  = "https://{instance}/{collection}/_apis/wit/attachments?fileName=imageFile.png&api-version=4.1".format(instance=self.const.INSTANCE,collection=self.const.COLLECTION)
        post = self.const.SESSION.post(url_post,data=open('C:\img\screenshot.png', 'rb').read(),headers=self.const.HEADERS,verify=False)

        return post.json().get('url')
    # devOps руу work item үүсгэх 
    def set_dev_ops(self,work_type,img_url):
        
        post_data = {
            "System.Title"                        : "TEST ..11",
            "System.AssignedTo"                   : self.const.ASSIGNEDTO,
            "System.IterationPath"                : self.const.ITERATIONPATH,
            "System.AreaPath"                     : self.const.AREAPATH,
            "description"                         : "<img src='"+img_url+"'>",
            "Microsoft.VSTS.TCM.Steps"            : "asdasd" #step_format(data[1],data[2])
        }

        payload = [dict(op="add", path='/fields/{}'.format(name), value= value) for name, value in post_data.items()]
        url_post  = "https://{instance}/{collection}/{project}/_apis/wit/workitems/${type}?api-version=4.1".format(instance=self.const.INSTANCE,collection=self.const.COLLECTION,project=self.const.PROJECT,type=work_type)
        post = self.const.SESSION.post(url_post,json=payload,headers=self.const.HEADERS1,verify=False)

#API
class initAPI:
    
    # Parameter - тэй холбоос үүсгэх
    def get_end_point_parameter(self,url_name,endpoint,parameter,number):
        end_point = ""
        url = self.cases['INIT'][url_name]
        _param = parameter.split(":")
        _number = number.split(":")
        index = 0
        end_point = self.cases[url_name]["PARAMETER"][endpoint]["ENDPOINT"]
        for e in _param:
            end_point = end_point.replace("#"+e+"#",self.cases[url_name]["PARAMETER"][endpoint]["PARAM"][e][int(_number[index])])
            index += 1;      
                
        return url+""+end_point # Бүтэн URL буцаана ( https://example.com/custom/000 )

    # Parameter байхгүй холбоос үүсгэх
    def get_end_point_no_parameter(self,url_name,endpoint):
        end_point = self.cases[url_name]["NOPARAMETER"][endpoint]["ENDPOINT"]
        url = self.cases['INIT'][url_name]

        return url+end_point # Бүтэн URL буцаана ( https://example.com/custom/ )

    # URL - н GET, POST, PUT method-г сонгох
    def get_methods(self,url,type_method,response):
        
        if type_method == "get" or type_method == "GET":
            headers = {"Authorization":"Bearer " + self.cases['INIT']["TOKEN"]}
            json_response = requests.get(url, headers = headers,verify= False)
            return json_response #үр дүнг буцаах

        elif type_method == "post" or type_method == "POST":
            session = requests.Session()
            session.verify = False
            headers = {"content-type":"application/json","Authorization":"Bearer " + self.cases['INIT']["TOKEN"]}
            
            json_response = session.post(url,headers = headers,json = response)
            return json_response #үр дүнг буцаах

        elif type_method == "put" or type_method == "PUT":
            session = requests.Session()
            session.verify = False
            headers = {"content-type":"application/json","Authorization":"Bearer " + self.cases['INIT']["TOKEN"]}
            
            json_response = session.put(url,json = response,headers = headers)

            return json_response #үр дүнг буцаах

        # elif type_method == "delete" or type_method == "DELETE": break

        return json_response # үр дүнг буцаах

    # endpoint - н body -г json файлаас авах 
    def get_json_body(self,endpoint,type):
        path = ""
        if type == "case":
            path = self.const.URL.get("CASE")
        elif type == "body":
            path = self.const.URL.get("BODY")
            
        file = open(path+endpoint+'.json','r',encoding="utf8") #'./json/' #r rb ашиглаж байгаа бол ,encoding="utf8" хэрэглэхгүй
        json_input = file.read()
        request_json = json.loads(json_input)
        return request_json

    # Json body - д өөрчилөлт оруулах
    # PARAMETERVALUE дээр өгөгдөл нэмсэн байх
    def set_body(self,body_data,url_name,endpoint,json):

        self.get_body_data = body_data

        for n in body_data.keys():   
            json[n] =  self.cases[url_name]["NOPARAMETER"][endpoint]["BODY"][body_data.get(n)][0]
     
        return json
    # json файлд байгаа  key - с PARAMETERVALUE  дээр байгаа key ижил байгаа бол setOneBody() ашиглана.
    # PARAMETERVALUE дээр өгөгдөл нэмсэн байх
    def set_cases_body(self,param1,url_name,endpoint,json,number):
        params  = param1.split(":")
        if len(params) > 1:
            params  = param1.split(":")
            numbers = number.split(":")
            
            for p in range(0,len(params)):
                json[params[p]] = self.cases[url_name]["NOPARAMETER"][endpoint]["BODY"][params[p]][int(numbers[p])]
        else:
            json[param1] = self.cases[url_name]["NOPARAMETER"][endpoint]["BODY"][param1][int(number)]
    
        return json
    
    def set_one_body(self,param1,url_name,endpoint,json,number):
        json[param1] = self.cases[url_name]["NOPARAMETER"][endpoint]["BODY"][param1][number]
            
        return json
    # json файлд байгаа  key - с PARAMETERVALUE  дээр байгаа key өөр байгаа бол setOneParam2Body() ашиглана.
    # setOneParam2Body() ашиглах-н өмнө SAMEPARAMETER дээр ялгаатай key-үүдыг оруулсан байх хэрэгтэй.
    # PARAMETERVALUE дээр өгөгдөл нэмсэн байх
    def set_one_param2_body(self,param1,url_name,endpoint,json,number):

        param2 = self.cases[url_name]["NOPARAMETER"][endpoint]["SAMEPARAM"][param1]
        json[param2] = self.cases[url_name]["NOPARAMETER"][endpoint]["BODY"][param1][number]
        
        return json
    
    def get_ln(self,type,json):
        
        if type == 1:
            json["terminal"]  = ""
            json["teller"]    = ""
            json["branch"]    = ""
            return json
        elif type == 2:
            json["terminal"]  = "999"
            json["teller"]    = "999"
            json["branch"]    = "5004"
            return json
        elif type == 3:
            json["terminal"]  = ""
            json["teller"]    = "999"
            json["branch"]    = "5004"
            return json
        elif type == 4:
            json["terminal"]  = "999"
            json["teller"]    = ""
            json["branch"]    = "5004"
            return json
        elif type == 5:
            json["terminal"]  = "999"
            json["teller"]    = "999"
            json["branch"]    = "5004"
            return json
        else:
            print("error -1")
            
    #Body дээр олон parameter оруулахад ашиглана
    def set_multi_body(self,param1,url_name,endpoint,json,number):
        params  = param1.split(":")
        numbers = number.split(":")
        
        for p in range(0,len(params)):
            json[params[p]] = self.cases[url_name]["NOPARAMETER"][endpoint]["BODY"][params[p]][int(numbers[p])]
            
        return json
    
    def get_message(self,message):
        
        if message == "Success":
            return 1000
        elif message == "'cif' Invalid cif number.":
            return 1001
        elif message == "0108 00 NO SUCH ACCOUNT ДАНСНЫ ДУГААР ОЛДОХГҮЙ БАЙНА":
            return 1002
        elif message == "1353 00 CANNOT AMEND AN INACTIVE RECORD":
            return 1003
    
    def get_check(self,url_name,endpoint,response,col_name,number,endpoint1):
            m = 0
            url = self.cases["INIT"][url_name] + self.cases[url_name]["NOPARAMETER"][endpoint]["ENDPOINT"]
            
            session = requests.Session()
            session.verify = False
            headers = {"content-type":"application/json","Authorization":"Bearer " + self.cases['INIT']["TOKEN"]}
            
            json_response = session.post(url,headers = headers,json = response)
            check_param = json_response.json()[col_name]
            check_value = self.cases[url_name]["NOPARAMETER"][endpoint1]["BODY"][col_name][number]
            print(check_param)
            if check_param == check_value:
                print(json_response.json()[col_name]) 
                m = 1
                
            # assert m == 1, "Error ..."
                