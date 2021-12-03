import time
from _ast import Assert

from data import mail
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(r'C:\Users\Admin\django\chromedriver.exe')
browser.get('https://www.facebook.com/')
clickLogin = browser.find_element_by_xpath("//button[@class='_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy']").click()
clickNewAccount = browser.find_element_by_xpath("//a[@class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']").click()
clickreg = browser.find_element_by_xpath("//button[@name='websubmit']").click()
clickFogot = browser.find_element_by_xpath("//a[@class='_97w4']").click()
clickSearch = browser.find_element_by_xpath("//button[@name='did_submit']").click()

def login(mail):
    time.sleep(1)
    login = browser.find_element_by_xpath('//input[@id="username"]').send_keys(mail['username'])
    time.sleep(1)


def password(mail):
    time.sleep(1)
    password = browser.find_element_by_xpath('//input[@id="password"]').send_keys(mail['password'])
    time.sleep(1)

def firstname(mail):
    time.sleep(1)
    firstname = browser.find_element_by_xpath('//input[@name="firstname"]').send_keys(mail['firstname'])
    time.sleep(1)

def lastname(mail):
    time.sleep(1)
    lastname = browser.find_element_by_xpath('//input[@name="lastname"]').send_keys(mail['lastname'])
    time.sleep(1)

def email(mail):
    time.sleep(1)
    firstname = browser.find_element_by_xpath('//input[@name="email"]').send_keys(mail['email'])
    time.sleep(1)


browser.get('https://www.facebook.com/')
login(mail)
password(mail)
time.sleep(3)
clickLogin

browser.get('https://www.facebook.com/')
login(mail)
time.sleep(2)
clickLogin
time.sleep(3)
password(mail)
time.sleep(2)
clickLogin

browser.get('https://www.facebook.com/')
password(mail)
time.sleep(2)
clickLogin
time.sleep(3)
login(mail)
time.sleep(2)
password(mail)
time.sleep(2)
clickLogin

browser.get('https://www.facebook.com/')
clickNewAccount
firstname(mail)
time.sleep(3)
lastname(mail)
time.sleep(3)
login(mail)
time.sleep(3)
password(mail)
time.sleep(3)
clickreg

browser.get('https://www.facebook.com/')
clickFogot
email(mail)
time.sleep(2)
clickSearch





