""" Constants File Integrated"""
# -*- coding: UTF-8 -*

class Constant:
	"""
	Constants
	"""
	URLS = {
		"IMS_URL": "https://15974:@192.168.1.77/certsrv"
	}
	
	AUTH = {
		"USERNAME" : "19379",
		"PASSWORD" : "kb2020*",
		"DABUA_USERNAME" : "03333",
		"DABUA_PASSWORD" : "kb2020*",
		"BUAA_USERNAME" : "04444",
		"BUAA_PASSWORD" : "kb2020*"	
	}
	
	ACCOUNTS = {
		"DEPOSIT_ACCOUNT" : '5030477254',
		"ORGANIZATION_ACCOUNT" : '5030477254',
		"INTERNAL_ACCOUNT" : '5021499463',
		"TIME_DEPOSIT_ACCOUNT" : '5400066186',
		"GEND_ACCOUNT" : '50030011010000005',
		"LOAN_ACCOUNT" : '5400066197',
		"CIF" : '00009500301699882',
		"CLOSE_ACCOUNT" : "5400066164",
		"RECEIVING_ACCOUNT" : "109200062125"
	}

	DATA = {
		"REGISTER_NO" : "УШ97040757",
		"ORGANIZATION_NO" : "RD03237705",
		"AMOUNT" : 10000,
		"HIGH_AMOUNT" : 3000001,
		"RECEIVING_BANK" : "Төрийн банк",
		"RECIPIENT" : "Нямхүү",
		"CHOOSE_PRODUCT" : 2,
		"TIMEOUT" : 20,
		# "CHROMEDRIVER_PATH" : "./ims/drivers/linux/chromedriver", #LINUX
		# "SCREENSHOT_PATH" : "./ims/reports/screenshots", #LINUX
	
		"CHROMEDRIVER_PATH" : "./drivers/windows/chromedriver.exe", #WINDOWS
		"SCREENSHOT_PATH" : "screenshots/", #WINDOWS
		"DESCRIPTION" : "test"
	}

	BILLS = {
		"MNT": [20000, 10000, 5000, 1000, 500, 100, 50, 20, 10, 5, 1, 0.1, 0.01],
		"AUD": [100, 50, 20, 10, 5, 2, 1, 0.1, 0.01],
		"CAD": [100, 50, 20, 10, 5, 2, 1, 0.1, 0.01],
		"CHF": [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1, 0.1, 0.01],
		"CNY": [100, 50, 20, 10, 5, 2, 1, 0.1, 0.01],
		"EUR": [500, 200, 100, 50, 20, 10, 5, 1, 0.1, 0.01],
		"GBP": [200, 100, 50, 20, 10, 5, 2, 1, 0.1, 0.01],
		"HKD": [1000, 500, 100, 50, 20, 10, 5, 2, 1, 0.1, 0.01],
		"JPY": [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1, 0.1, 0.01],
		"KRW": [50000, 10000, 5000, 1000, 500, 100, 50, 20, 10, 5, 1, 0.1, 0.01],
		"NZD": [10000, 1000, 500, 100, 50, 20, 10, 5, 2, 1, 0.1, 0.01],
		"RUB": [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 1, 0.1, 0.01],
		"SGD": [10000, 1000, 500, 100, 50, 20, 10, 5, 2, 1, 0.1, 0.01],
		"USD": [100, 50, 20, 10, 5, 2, 1, 0.1, 0.01]
	}

	CURRENCY = {
		"IN" : "JPY",
		"OUT" : "MNT"
	}

	DATE = {
		"START_DATE" : "20200518",
		"END_DATE" : "20200601",
		"START_DATE_LIMIT" : "20200518",
		"END_DATE_LIMIT" : "20200701"
	}

	USER = {
		"FIRST_NAME" : "ДЭМҮҮЛ",
		"LAST_NAME" : "БАТСҮХ"
	}