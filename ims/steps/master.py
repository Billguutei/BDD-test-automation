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
from modules.utils import Notification
from modules.statementController import *
from modules.accessController import *
from modules.bulkController import *
from modules.documentController import Document_personal
from modules.mikController import MikSystem
from modules.dispitcherController import *
from modules.reportController import *
from modules.catalogController import *
from modules.taxController import *
from modules.organizationRegistrationController import *
from modules.cardController import *
from modules.forexController import *
from modules.searchController import *
from modules.loanController import *
from modules.nostroController import *
from modules.rateController import *
from modules.loanController import *
from modules.allowanceService import *
from modules.consumerController import *
import cx_Oracle
import time
import base64

consts = Constant()

import time
import os


def download_wait(path_to_downloads):
	seconds = 0
	dl_wait = True
	while dl_wait and seconds < 20:
		time.sleep(1)
		dl_wait = False
		for fname in os.listdir(path_to_downloads):
			if fname.endswith('.crdownload'):
				dl_wait = True
		seconds += 1
	return seconds

@when(u'login to ims')
@given(u'login to ims')
def step(self):
	driver = self.driver
	LoginsClass.login(self)
	WebDriverWait(driver, timeout=30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'nav-item')))

@when(u'login to ims BUAA')
@given(u'login to ims BUAA')
def step(self):
	driver = self.driver
	LoginsClass.login_BUAA(self)
	WebDriverWait(driver, timeout=30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'nav-item')))


# PAGES
@then('check page loaded <{window_name}>')
@when('check page loaded <{window_name}>')
@given('check page loaded <{window_name}>')
def step(self, window_name):
	Tools.check_page_loaded(self, window_name)


@when('<{window_name}> load page')
@given('<{window_name}> load page')
def step(self, window_name):
	Tools.load_page(self, window_name)

@given('search transaction <{transaction_type}>')
def step(self, transaction_type):
	Search.transaction(self, transaction_type)

@then('refresh page')
def step(self, window_name):
	Tools.refresh_page(self)
	
# TRANSACTION
@given("<{transaction_menu}> transaction process <{account_type}>")
@when("<{transaction_menu}> transaction process <{account_type}>")
def step(self, transaction_menu, account_type):
	Transactions.all_transactions(self, transaction_menu, account_type)

@given("<{transaction_menu}> transaction process")
@when("<{transaction_menu}> transaction process")
def step(self, transaction_menu):
	Transactions.exchange_transactions(self, transaction_menu)


@when('<{window_name}> fill field <{account_type}>')
@given('<{window_name}> fill field <{account_type}>')
def step(self, window_name, account_type):
	Tools.fill_account_number(self, window_name, account_type)

@when("create task")
@given("create task")
def step(self):
	driver = self.driver
	Task.all_tasks(self, "create")
	Notification.task(self, "create task")
	Task.get_task_number(self)

@when("create organization task")
@given("create organization task")
def step(self):
	driver = self.driver
	Task.all_tasks(self, "create organization")
	Notification.task(self, "create-organization task")
	Task.get_task_number(self)

@when('approve task')
@then('approve task')
@given('approve task')
def step(self):
	driver = self.driver
	Task.all_tasks(self, "task-approve")
	Notification.task(self, "approve task")
	LoginsClass.login(self)
	WebDriverWait(driver, timeout=30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'nav-item')))

@then('decline task')
def step(self):
	driver = self.driver
	Task.all_tasks(self, "task-decline")
	Notification.task(self, "decline task")
	WebDriverWait(driver, timeout=30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'nav-item')))


# SCREEN SHOT
@then('<{id}> screen shot by id <{screenshot_name}>')
def step(self, id, screenshot_name):
	Tools.take_screenshot_by_tag_name(self, id, screenshot_name, True)


# SCREEN SHOT
@then('<{class_name}> screen shot by class name <{screenshot_name}>')
def step(self, class_name, screenshot_name):
	Tools.take_screenshot_by_class_name(self, class_name, screenshot_name, True)


@then('<{class_name}> screen shot <{window_name}>')
def step(self, class_name, window_name):
	Tools.take_screenshot(self, class_name, window_name, True)


@given("<{window_name}>-<{value}> multi window <{account_type}>")
@when("<{window_name}>-<{value}> multi window <{account_type}>")
def step(self, window_name, value, account_type):
	driver = self.driver
	Tools.multi_window_inquiry(self, window_name, account_type, value)


@when("<{value}> multi window")
def step(self, value):
	driver = self.driver
	Tools.multi_window_request(self, value)


@then('display to loan repayment request')
def step(self):
	driver = self.driver
	driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
	time.sleep(2)


@when('insert value')
def step(self):
	Allowance.customer_search(self)

@when('download search by user report')
def step(self):
	Allowance.allowance_report(self)

@then('Limited Statement')
def step(self):
	Statement.status_statement(self)


@when('Search transaction with description')
@then('Search transaction with description')
def step(self):
	Transactions.search_transaction_by_description(self)


@then('Do correction for <{window_name}>')
@when('Do correction for <{window_name}>')
def step(self, window_name):
	Task.do_correction(self, window_name)


@given('<{transaction_type}> completed')
@then('<{transaction_type}> completed')
def step(self, transaction_type):
	driver = self.driver
	Notification.task(self, transaction_type)


@when("10400 multi window")
def step(self):
	driver = self.driver
	values = ["1", "2", "3", "C", "4", "P", "R"]
	Tools.multi_window_inquiry(self, "10400", "LOAN_ACCOUNT", values, False)


@then("10400 multi window take screen shot")
def step(self):
	driver = self.driver
	values = ["1", "2", "3", "C", "4", "P", "R"]
	Tools.multi_window_inquiry(self, "10400", "LOAN_ACCOUNT", values, True)


@when('open description of account menu')
def step(self):
	driver = self.driver
	Menu.description_of_account_menu(self)

@given('Do <{click_approved}> to approved task')
@when('Do <{click_approved}> to approved task')
def step(self, click_approved):
	driver = self.driver
	Task.all_tasks(self, click_approved)

@then('<{window_name}> choose product  of account')
def step(self, window_name):
	driver = self.driver
	Document_personal.choose_product(self, window_name)

@then('<{window_name}> choose product  of corp account')
def step(self, window_name):
	driver = self.driver
	Document_personal.chooseProductCorp(self, window_name)

@then('<{window_name}> choose product of card')
def step(self, window_name):
	driver = self.driver
	Document_personal.chooseProductCard(self, window_name)

@then('<{window_name}> choose product of cyber')
def step(self, window_name):
	driver = self.driver
	Document_personal.chooseProductCyber(self, window_name)

@then('<{window_name}> choose product of account service')
def step(self, window_name):
	driver = self.driver
	Document_personal.chooseProductAccount(self, window_name)

@then('<{window_name}> choose type of definition')
def step(self, window_name):
	driver = self.driver
	Document_personal.definition(self, window_name)

@then('<{window_name}> choose type of definitionLoan')
def step(self, window_name):
	driver = self.driver
	Document_personal.definition_loan(self, window_name)

@then('<{window_name}> choose type of embassy')
def step(self, window_name):
	driver = self.driver
	Document_personal.embassy_korea(self, window_name)

@given('click to upgrade button')
def step(self):
	driver = self.driver
	Tools.button_click(self, '//button[text()=" Шинэчлэх "]', "click", "",By.XPATH)

@then('fill fields of branch upgrade')
def step(self):
	driver = self.driver
	Document_personal.upgrade_branch(self)

@then('account balance guarantee')
def step(self):
	driver = self.driver
	Document_personal.account_balance_guarantee(self)

@when('tax transaction list')
@given('tax transaction list')
def step(self):
	driver = self.driver
	Tax.tax_service(self)

@when('tax transaction')
def step(self):
	driver = self.driver
	Tax.tax_transaction(self)

@when('<{invoice_number}> fill date and search')
def step(self, type):
	driver = self.driver
	Tax.tax_report(self, type)

@then('task menus filter <{filter_type}>')
def step(self, filter_type):
	driver = self.driver
	Task.task_menus_filter(self, filter_type)

@then('<{loan_report_type}> loan contract report')
def step(self, loan_report_type):
	driver = self.driver
	Loan.loan_contract_report(self, loan_report_type)
	time.sleep(1)

@then('<{loan_interest_of_partner_organization_type}> loan interest of partner organization')
def step(self, loan_interest_of_partner_organization_type):
	driver = self.driver
	Loan.loan_interest_of_partner_organization(self, loan_interest_of_partner_organization_type)
	time.sleep(1)

@then('<{choose_tab}> nostro account replenishment')
def step(self, choose_tab):
	driver = self.driver
	Nostro.nostro_account_replenishment(self, choose_tab)

@then('<{search_type}> nostro list report')
def step(self, search_type):
	driver = self.driver
	Nostro.nostro_list_report(self, search_type)

@then('nostro approved decisions')
def step(self):
	driver = self.driver
	Nostro.nostro_approved_decisions(self)

@then('<{type}> nostro transfer')
def step(self, type):
	driver = self.driver
	Nostro.nostro_transfer_type(self, type)
@given('send to loan request')
def step(self):
	Loan.loan_send_request(self)

@given('loan search register')
def step(self):
	Loan.loan_search_register(self)


@then('click cancel button')
def step(self):
	driver = self.driver
	driver.execute_script(
		'document.querySelector("body > print-preview-app").shadowRoot.querySelector("#sidebar").shadowRoot.querySelector("print-preview-button-strip").shadowRoot.querySelector("cr-button.cancel-button").click()')
	time.sleep(5)
	driver.switch_to_window(driver.window_handles[-1])
	
	time.sleep(3)

@then('<{account_type}> search by <{type}>')
def step(self, account_type, type):
	Statement.customer_search(self, account_type, type)

@then('<{type}> Integrated Amount that day')
def step(self, type):
	Integrated_Amount.Integrate(self, type)

@then('<{type}> process')
def step(self, type):
	Cash_drawer.CashExchange(self, type)

@then('fill fields and <{type}>')
def step(self, type):
    Dispitcher.dispitcher_setting(self, type)


@then('get report and take screenshot')
def step(self):
    Dispitcher.dispitcher_report(self)

@when('<{type}> search button')
def step(self, type):
	TransactionList.transaction_type(self, type)

@when('<{type}> on table')#gereeni tuuh harah
def step(self, type):
	OrgRegService.organizationlist(self, type)

@when('<{type}> in table')
def step(self, type):
	OrgRegService.configuration(self, type)

@when('<{type}> supervisor to list')
def step(self, type):
	OrgRegService.supervisorlist(self, type)

@when('<{type}> conditionally')
def step(self, type):
	OrgRegService.createContract(self, type)

@then('matching date and download')
def step(self):
	Report.Acc_def_ded_rep(self)

@then('<{operation_type}> {name}')
@when('<{operation_type}> {name}')
def step(self, operation_type, name):
	if name == "menu":
		Access.menu(self, operation_type)
	elif name == "group":
		Access.group(self, operation_type)
	elif name == "module":
		Access.module(self, operation_type)
	elif name == "product":
		Access.product(self, operation_type)
	elif name == "endpoint":
		Access.endpoint(self, operation_type)
	elif name == "user access":
		Access.user_access(self, operation_type)
	elif name == "in document service":
		Document_personal.etc_document(self, operation=operation_type)
	elif name == "fill fields of order new card":
		card.card_order_new(self, operation_type)
	elif name == "fill fields of order reissue and renewal":
		card.card_order_reissue_renewal(self, operation_type)
	elif name == "bulk list":
		bulk.operation(self, operation_type)
	elif name == "fill fields and go transaction":
		card.change_limit(self, operation_type)
	elif name == "transaction list":
		Transaction.operation(self, operation_type)


#@then('check the table again <{status}>')
#def step(self, status):
#	Catalog.check_operation(self, status)

#@when('<{operation}> branch')
#def step(self, operation):
#	Catalog.menu_operation(self, operation)

#@when("inquire endpoint in table by <{name}>")
#def step(self, name):
#	global inquiry
#	inquiry = Access.inquire_endpoint(self, name)

@when("inquire endpoint completed")
@then("inquire endpoint completed")
def step(self):
	ACCESS = {
		"link": {
			"name": "editedTestName",
			"description": "editedTestDescription",
			"request_method": "POST",
			"url_endpoint": "edited/some/endpoint",
		}
	}
	assert ACCESS['link']['name'] == inquiry[0], "endpoint name mismatch"
	assert ACCESS['link']['description'] == inquiry[1], "descriptions mismatch"
	assert ACCESS['link']['request_method'] == inquiry[2], "request method mismatch"
	assert ACCESS['link']['url_endpoint'] == inquiry[3], "endpoint mismatch"

@then('loan customer search by <{type}>')
def step(self, type):
	Statement.loan_customer_search(self, type)
# consumer loan-д  харилцагчийн cif, register -ээр зээлийн түүх хайхад хэрэглэгдэж байгаа
@Given('search by loanhistory <{type}>')
def step(self, type):
	consumerLoann.inquiryLoanHistory(self, type)
	time.sleep(5)
#########################################################################################
@when("mik-system-xml add information")
def step(self):
	MikSystem.xml_add_information(self)

@when("mik-fee income")
def step(self):
	MikSystem.fee_income(self)

@when('mik-system-xml <{operation}>')
def step(operation):
	MikSystem.xml_menu_operation(self, operation)

@when('insert date time and press inquire button')
def step(self):
	MikSystem.xml_menu_operation(self, 'inquiry')

@then('data will be shown')
def step(self):
	MikSystem.xml_menu_operation(self, 'inquiry')

@when("click on download excel button")
def step(self):
	MikSystem.xml_menu_operation(self, 'download excel')

@then("excel file will be downloaded")
def step(self):
	MikSystem.xml_menu_operation(self, 'check excel')

@when('press on add account')
def step(self):
	MikSystem.loan_account(self, operation="add account")

@then('inquired loan account should be in the table')
def step(self):
	MikSystem.loan_account(self, operation="inquire loan account")

@when("delete loan account from the table")
def step(self):
	MikSystem.loan_account(self, operation="delete loan account")

@then(u'mik-loan-account download excel')
def step(self):
	MikSystem.loan_account(self, 'download excel file')

@when("mik-repayment-plan <{operation}>")
@then("mik-repayment-plan <{operation}>")
def step(self, operation):
	MikSystem.repayment_plan(self, operation)

@then("mik-add-account <{operation}>")
@when("mik-add-account <{operation}>")
def step(self, operation):
	MikSystem.add_account(self, operation)

@given(u'etc document <{operation}> <{document}>')
def step(self, operation, document):
	Document_personal.select_etc_document(self, operation=operation, document=document)
	
@then(u"check if document is deleted")
def step(self):
	assert Document_personal.document_is_deleted(self) == True

@then(u"check if group is deleted")
def step(self):
	assert Document_personal.group_is_deleted(self) == True


@when('Search for a card <{search_type}>')
def step(self, search_type):
	card.card_search(self, search_type)

@when('Search for a customer by <{account_type}> account number')
def step(self,account_type):
	card.customer_search(self,account_type)

@when('Select the closing card')
def step(self):
	card.close_card(self)
	

@given("<{search_type}> find date")
def step(self, search_type):
	Rate.search_history(self, search_type)

@given("file upload")
def step(self):
	Rate.upload_file(self)

@then("open approved deals")
@when("open approved deals")
def step(self):
	forex.approved_deals(self)

@when("database config")
def step(self):
    conn = cx_Oracle.connect(base64.b64decode("YW5zaWJsZQ==").decode("utf-8"), base64.b64decode("YW5zaWJsZTEyMw==").decode("utf-8"), consts.URLS["DATABASE"])
    cursor = conn.cursor()
    cursor.execute("delete msidentity.users where id = 10000")
    cursor.execute("delete msidentity.users where id = 12321")
    cursor.execute("delete msidentity.user_roles where user_id = 10000")
    cursor.execute("delete msidentity.user_roles where user_id = 12321")
    cursor.execute("Insert into MSIDENTITY.USERS (ID, NAME, DEPARTMENT, TITLE, BRANCH, RETRY, STATUS, REGISTER) Values ('12321', 'test', 'test', 'test', '5000', 0, 1, '')")
    cursor.execute("Insert into MSIDENTITY.USERS (ID, NAME, DEPARTMENT, TITLE, BRANCH, RETRY, STATUS, REGISTER) Values ('10000', 'test', 'test', 'test', '5000', 0, 1, '')")
    cursor.execute("Insert into MSIDENTITY.USER_ROLES(USER_ID, ROLE_ID) Values('10000', 132)")
    cursor.execute("Insert into MSIDENTITY.USER_ROLES(USER_ID, ROLE_ID) Values('10000', 46)")
    cursor.execute("Insert into MSIDENTITY.USER_ROLES(USER_ID, ROLE_ID) Values('10000', 15)")
    cursor.execute("Insert into MSIDENTITY.USER_ROLES(USER_ID, ROLE_ID) Values('10000', 154)")
    cursor.execute("Insert into MSIDENTITY.USER_ROLES(USER_ID, ROLE_ID) Values('12321', 25)")
    
    # cursor.execute("update msidentity.users set FINGERPRINT = '' where id = "+ consts.AUTH["USER_NAME"] +"")
    conn.commit()
    cursor1 = conn.cursor()
    cursor1.execute("select value from msconfig.configs where application = 'bancs-inquiry-service-1' and label = 'master' and name = 'database.url'")
    for each in cursor1:
        for i in range (len(each)):
            bancs_database = each[i]
    bancs_database_url = (bancs_database.split(":")[3] + ":" + bancs_database.split(":")[4]).split("@")[1]
    conn.close()
    conn_bancs = cx_Oracle.connect(base64.b64decode("YW5zaWJsZQ==").decode("utf-8"), base64.b64decode("YW5zaWJsZTEyMw==").decode("utf-8"), bancs_database_url)
    cursor = conn_bancs.cursor()
    cursor.execute("update fnsonlp.telm SET signon_flag='N',teller_pword='99?@2dD 63',brch_no = '05000',prim_branch = '05000', teller_pword_retry=00, teller_no='0000000000010000',prim_cap=10,capable=10,prim_grp=21,stat='01',grp_no = 21,teller_name='Tester' where teller_no like '0000000000010000'")
    cursor.execute("update fnsonlp.telm SET signon_flag='N',teller_pword='99?@2dD 63',brch_no = '05000',prim_branch = '05000', teller_pword_retry=00,teller_no='0000000000012321',prim_cap=11,capable=11,prim_grp=20,stat='00',grp_no = 20,teller_name='Tester' where teller_no like '0000000000012321'")
    cursor.execute("update fnsonlp.invm set CURR_STATUS = '00', ACCT_TYPE='4100', INT_CAT='0001', CUSTOMER_NO = '0000009555101149',  DAY_CASH_WDL_VALUE = '72000',DAY_CASH_DATE='44073',SOP_BAL='256898.52', CURR_BAL='5648402.29',NPB_VAL='5648402.29' where KEY_1 like '0030000000575351166'")
    cursor.execute("update fnsonlp.invm set CURR_STATUS = '00', ACCT_TYPE='4100', INT_CAT='0001', CUSTOMER_NO = '0000009555101149',  DAY_CASH_WDL_VALUE = '72000',DAY_CASH_DATE='44073',SOP_BAL='256898.52', CURR_BAL='5648402.29',NPB_VAL='5648402.29' where KEY_1 like '0030000000555209656'")
    cursor.execute("update fnsonlp.cusc set customer_no = '0000009555101149' where acct_no like '0000000555209656'")
    cursor.execute("update fnsonlp.cusm set prim_acct = '9555101149' where cust_acct_no like '0000000555209656'")
    cursor.execute("update fnsonlp.cusvdd set ID1 = 'ÓÈ00000000              ' where KEY_1 like '0030000009555101149%'")
    cursor.execute("update fnsonlp.cuid set ID_NUMBER = 'ÓÈ00000000              ' where CUST_NO like '0000009555101149'")
    cursor.execute("update fnsonlp.borm set BR_NO = '05000', STAT = '08', ACT_TYPE = '2300', DISCH_FEE_CODE='N', INT_REPAY_FREQ = '01', PURPOSE_CODE_A = '3', LOAN_OFFICER = '92', APPLIC_AMOUNT = '100000', INT_REPAY_DAY ='00', REPAY_COUNT='0', EOY_BASIC_BAL = '100000', APP_AMT = '100000', LOAN_BAL='59000', ADV_VAL='100000', NPB_VAL='59000', THEO_LOAN_BAL='100000', SOP_BAL='0', EOM_BASIC_BAL='100000', CUSTOMER_NO = '0000009555101149'  where key_1 = '0030000000500002403'")
    cursor.execute("update fnsonlp.cusc set customer_no = '0000009555101149' where acct_no like '0000000500002403' and status = '01'")
    cursor.execute("update fnsonlp.cusm set prim_acct = '9555101149' where cust_acct_no like '0000000500002403'")
    conn_bancs.commit()
    conn_bancs.close()