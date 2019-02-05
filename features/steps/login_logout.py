from behave import *
from locators import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@given(u'go to homepage')
def step_impl(context):
    context.browser.get('https://arena-m3.jog.ojodowo.com/')
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.navbar)
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.landing)
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.slide)

@when(u'click button login')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.login1).click()
    context.browser.implicitly_wait(10)

@then(u'tooltip appear')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.tooltip_login)
    context.browser.implicitly_wait(10)

@when(u'input valid username & password & click login')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.form_username).send_keys('watson')
    context.browser.find_element(By.XPATH,locator.form_password).send_keys('12345678')
    context.browser.find_element(By.XPATH,locator.login2).click()
    context.browser.implicitly_wait(10)

@then(u'success login')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.avatar)
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.slide)
