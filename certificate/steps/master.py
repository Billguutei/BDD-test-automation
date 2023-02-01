# -*- coding: UTF-8 -*
import datetime

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
from modules.utils import *

import time

consts = Constant()


@when(u'login to ims')
@given(u'login to ims')
def step(self):
	driver = self.driver
	LoginsClass.login(self)
	WebDriverWait(driver, timeout=30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'nav-item')))


# PAGES
@when('check page loaded <{window_name}>')
@given('check page loaded <{window_name}>')
def step(self, window_name):
	Tools.check_page_loaded(self, window_name)


@when('<{window_name}> load page')
@given('<{window_name}> load page')
def step(self, window_name):

	Tools.load_page(self, window_name)


@then('refresh page')
def step(self, window_name):
	Tools.refresh_page(self)


# TRANSACTION
@given("<{transaction_menu}> transaction process")
@when("<{transaction_menu}> transaction process")
def step(self, transaction_menu):
	Transactions.all_transactions(self, transaction_menu)


@when('<{window_name}> fill field <{account_type}>')
@given('<{window_name}> fill field <{account_type}>')
def step(self, window_name, account_type):
	Tools.fill_account_number(self, window_name, account_type)


# TASK
@then("close_approved_task_process")
def step(self):
	driver = self.driver
	Task.close_approved_task_process(self)


@when("create task")
@given("create task")
def step(self):
	driver = self.driver
	Task.all_tasks(self, "create")
	Notification.task(self, "task create")
	Task.get_task_number(self)


@when("create organization task")
@given("create organization task")
def step(self):
	driver = self.driver
	Task.all_tasks(self, "create organization")
	Notification.task(self, "task create-organization-task")
	Task.get_task_number(self)


@when('approve task')
@given('approve task')
def step(self):
	driver = self.driver
	Task.all_tasks(self, "task-approve")
	Notification.task(self, "task approve")
	LoginsClass.login(self)
	WebDriverWait(driver, timeout=30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'nav-item')))


@then('decline task')
def step(self):
	Task.all_tasks(self, "task-decline")
	Notification.task(self, "decline task")


# SCREEN SHOT
@then('<{id_name}> screen shot by id <{name}>')
def step(self, id_name, name):
	Tools.take_screenshot_by_tag_name(self, id_name, name, True)


# SCREEN SHOT
@then('<{class_name}> screen shot by class name <{name}>')
def step(self, class_name, name):
	Tools.take_screenshot_by_class_name(self, class_name, name, True)


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

@then('Limited Statement')
def step(self):
	Statement.status_statement(self)


@when('Search transaction with description')
@then('Search transaction with description')
def step(self):
	Transaction.search_transaction_by_description(self)


@then('Do correction for <{window_name}>')
@when('Do correction for <{window_name}>')
def step(self, window_name):
	Task.do_correction(self, window_name)


@then('task menus filter <{filter_type}>')
def step(self, filter_type):
	driver = self.driver
	Task.task_menus_filter(self, filter_type)


@given('<{transaction_type}> completed')
@then('<{transaction_type}> completed')
def step(self, transaction_type):
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


@given('search by account number')
def step(self):
	driver = self.driver
	driver.find_element_by_xpath("//input[@type='text']").clear()
	driver.find_element_by_xpath("//input[@type='text']").send_keys(consts.ACCOUNTS["DEPOSIT_ACCOUNT"])
	time.sleep(3)
	driver.find_element_by_xpath("//button[@type='button']").click()
	time.sleep(3)


@given('search by register number')
def step(self):
	driver = self.driver
	driver.find_element_by_xpath("//input[@type='text']").clear()
	driver.find_element_by_xpath("//input[@type='text']").send_keys(consts.DATA["REGISTER_NO"])
	time.sleep(3)
	driver.find_element_by_xpath("//button[@type='button']").click()


# service of documnet
# Usukhbayar

@when('document load page')
def step(self):
	Tools.load_page(self, 'Бичиг баримт', 'Үйлчилгээ')


@when('Do document to approved task')
def step(self):
	driver = self.driver
	Task.all_tasks(self, "approved-document")


@then('<{window_name}> choose product  of account')
def step(self, window_name):
	driver = self.driver
	Document_personal.choose_product(self, window_name)


@when('Do account_balance_guarantee to approved task')
def step(self):
	driver = self.driver
	Task.all_tasks(self, "approved-account_balance_guarantee")


@then('account balance guarantee')
def step(self):
	driver = self.driver
	Document_personal.account_balance_guarantee(self)


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


# ACCESS MENU KHURELCHULUUN
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

	# elif name == "endpoint" and operation_type == "add":
	# 	Access.add_endpoint(self)
	# elif name == "endpoint" and operation_type == "edit":
	# 	Access.edit_endpoint(self)
	# elif name == "status" and operation_type == "change":
	# 	Access.change_status(self)
	# elif name == "endpoint" and operation_type == "delete":
	# 	Access.delete_endpoint(self)
	# elif name == "branch" and (operation_type == "add" or operation_type == "edit" or operation_type == "delete"):
	# 	CatalogAdmin.menu_operation(self, operation_type)

@then('check the table again <{status}>')
def step(self, status):
	CatalogAdmin.check_operation(self, status)

@when("inquire endpoint in table by <{name}>")
def step(self, name):
	global inquiry
	inquiry = Access.inquire_endpoint(self, name)

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

@when("mik-system-xml add information")
def step(self):
	MikSystem.xml_add_information(self)

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
