from requests.auth import HTTPBasicAuth
import requests
import urllib3
# import openpyxl
urllib3.disable_warnings()

class Constant:
    #PATH 
    URL = {
        'CUSTOMERSERVICE': "https://192.168.26.16:9081",
        'SMSBANKREGISTERSERVICE':"https://192.168.26.16:9221",
		'EXCEL': "excel_path",
        'BODY' : "C:\json\ms\\", #C:\json\cases\\ ./msCRM/json/ms/  C:\json\ms\\
        'CASE' : "C:\json\cases\\",  #C:\json\cases\\  C:\json\cases\\
        'FILEPATH' : "./API-customer-service/log/log_test.log" #./ims/drivers/linux/chromedrive
    }
    #CRM Login
    KEYS = {
		"login": {
			"sendkey": ["UserName","SecureTextBox.Text"],
			"sendkeyvalue":{
				 0: ["crmLogin","user111","crmLogin",""],
			     1: ["123456","123456","819282",""]
			}
		}
	}
    
    FOLDERANDFILESTRUCTURE = {
		'ROOT':'',
		'MAIN':['dir1','dir2'],
		'SUB' :{
			'dir1': ['d1','d2'],
			'dir2': ['d1','d2','d3']
		}
	}


    #devOps руу холболт хийх тогтмол
    DEVOPSTOKEN = "7r3k6mesccjpd2d3bmjnwfneo4nfruntutyensx7nrm2v73hwxta"

    SESSION = requests.Session()
    SESSION.auth = ("90059", DEVOPSTOKEN)

	# Request Header
    HEADERS = dict()
    HEADERS['Content-Type'] = "application/octet-stream" #application/octet-stream #json-patch+json
	# HEADERS['Accept'] = 'text/plain'

	#Excel-н файлын зам
    COLUMN_NUMBER = 3
    LK_COLUMN_NUMBER = 1
	#devOps-н URL оруулах хэсэг
    INSTANCE   = "devops" 
    COLLECTION = "ITDS"
    PROJECT    = "BDD Test Automation"

	#Work Item үүсгэхдээ
    ASSIGNEDTO = ""
    ITERATIONPATH = "BDD Test Automation\Iteration 1"
    AREAPATH = "BDD Test Automation"
    # GET
    HEADERS1 = dict()
    HEADERS1['Content-Type'] = "application/json-patch+json" #application/octet-stream #json-patch+json



















