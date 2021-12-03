import time
from _ast import Assert

from data import mail
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(r'C:\Users\Admin\django\chromedriver.exe')
browser.get('https://www.instagram.com/')
clickLogin = browser.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']").click()


def login(mail):
    time.sleep(2)
    login = browser.find_element_by_xpath('//input[@name="username"]').send_keys(mail['username'])
    time.sleep(2)


def password(mail):
    time.sleep(2)
    password = browser.find_element_by_xpath('//input[@name="password"]').send_keys(mail['password'])
    time.sleep(2)

def firstname(mail):
    time.sleep(2)
    firstname = browser.find_element_by_xpath('//input[@name="firstname"]').send_keys(mail['firstname'])
    time.sleep(2)

def lastname(mail):
    time.sleep(2)
    lastname = browser.find_element_by_xpath('//input[@name="lastname"]').send_keys(mail['lastname'])
    time.sleep(2)

def friend(mail):
    time.sleep(2)
    friend = browser.find_element_by_xpath('//input[@class="oajrlxb2 rq0escxv f1sip0of hidtqoto e70eycc3 lzcic4wl hzawbc8m ijkhr0an aaoq3grb sgqwj88q b3i9ofy5 oo9gr5id b1f16np4 hdh3q7d8 dwo3fsh8 qu0x051f esr5mh6w e9989ue4 r7d6kgcz br7hx15l h2jyy9rg n3ddgdk9 owxd89k7 ihxqhq3m jq4qci2q k4urcfbm iu8raji3 qypqp5cg l60d2q6s hv4rvrfc hwnh5xvq ez2duhqw rmlgq0sb dzqu5etb aj8hi1zk r4fl40cc kd8v7px7 m07ooulj mzan44vs"]').send_keys(mail['friend'])
    time.sleep(2)

currentUrl = browser.getCurrentUrl()
login(mail)
password(mail)
time.sleep(3)
clickLogin
time.sleep(3)


