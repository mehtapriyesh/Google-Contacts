# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 21:34:28 2019

@author: user
"""

"""
This can be used to add an entire database of contacts to google contacts which can later be used for other purposes such as using saved
contacts to apply whatsapp marketing.
"""



from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
    
id=input('Enter your email id.')
psw=input('Enter your password.')
driver=webdriver.Chrome()

driver.get('https://contacts.google.com/')
email=driver.find_element_by_id("identifierId")
email.send_keys(id)
submit=driver.find_element_by_id("identifierNext")
submit.click()
sleep(2)
password=driver.find_element_by_name("password")
password.send_keys(psw)
submit=driver.find_element_by_id("passwordNext")
submit.click()
sleep(2)

fnames=['abc','def']
lnames=['ghi','jkl']
numbers=[12345,56789]

ignored_exceptions=(StaleElementReferenceException,NoSuchElementException)
def wdw(path):
    return WebDriverWait(driver,10,ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located((By.XPATH,path)))

for n in range(len(fnames)):
    create_contact=wdw("//button/span[2]").click()
    fnameins=wdw("//input[@aria-label='First name']").send_keys(fnames[n])
    lnameins=wdw("//input[@aria-label='Last name']").send_keys(lnames[n])
    numins=wdw("//input[@aria-label='Phone']").send_keys(numbers[n])
    submit=wdw("//button[2]/span").click()
    end=wdw("//div[3]/div[4]").click()
    sleep(2)

