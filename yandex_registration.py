from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from anticaptchaofficial.imagecaptcha import *
import os
import urllib.request
import time
import sys
import requests
import random

print(sys.argv[1]) # proxy
print(sys.argv[2]) # name
print(sys.argv[3]) # surname
print(sys.argv[4]) # task_id

PROXY = str(sys.argv[1])
name = str(sys.argv[2])
surname = str(sys.argv[3])
task_id = str(sys.argv[4])
MASTER_URL = ""

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome_options.add_argument("--start-maximized")
chrome = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)

# random
random_number = random.randint(100,999)

# name
chrome.get('https://passport.yandex.com.tr/registration/mail?from=mail&require_hint=1&origin=hostroot_homer_reg_tr&retpath=https%3A%2F%2Fmail.yandex.com.tr%2F&backpath=https%3A%2F%2Fmail.yandex.com.tr%3Fnoretpath%3D1')
input = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/main/div/div/div/form/div[1]/div[1]/span/input")
input.clear()
input.send_keys(name)

url = 'http://0.0.0.0:5000/set_status/1' # status update
resp = requests.get(url)

# surname
input = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/main/div/div/div/form/div[1]/div[2]/span[1]/input")
input.clear()
input.send_keys(surname)

# username-password
input = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/main/div/div/div/form/div[1]/div[3]/span/input")
input.clear()
username = name + surname + str(random_number)
input.send_keys(username)
input = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/main/div/div/div/form/div[2]/div[1]/span/input")
password = "dWz3P2WdpzSPrcv"
input.send_keys(password)
input = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/main/div/div/div/form/div[2]/div[2]/span/input")
input.send_keys(password)

next_bttn = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/main/div/div/div/form/div[3]/div/div[2]/div/div[1]/span")
next_bttn.click()

# click "i don't have a phone number"
try:
    element = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[1]/div[2]/span/input")))
finally:
    pass
input = chrome.find_element_by_xpath("/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[1]/div[2]/span/input")
input.clear()
artist="fazilsay"
input.send_keys(artist)

# solve capcha
solver = imagecaptcha()
solver.set_verbose(1)
solver.set_key("70ef28f6ff927932a8db1305496fe783")

element = ""
try:
    element = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[2]/div[2]/div/div[1]/img")))
finally:
    src = element.get_attribute('src')
    urllib.request.urlretrieve(src, "captcha.jpeg")

url = 'http://0.0.0.0:5000/set_status/2' # status update
resp = requests.get(url)

# solve capcha
captcha_text = solver.solve_and_return_solution("captcha.jpeg")
if captcha_text != 0:
    print("captcha text "+captcha_text)
else:
    print("task finished with error "+solver.error_code)


try:
    element = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/button")))
finally:
    chrome.find_element_by_xpath("/html/body/div[2]/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/button").click()


input = chrome.find_element_by_xpath("/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[2]/div[1]/span/input")
input.clear()
input.send_keys(captcha_text)

# try to close cookie selection
try:
    element = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/main/div/div/div/form/div[4]/span/button")))
finally:
    next_bttn = chrome.find_element_by_xpath("/html/body/div/div/div[2]/div/main/div/div/div/form/div[4]/span/button")
    next_bttn.click()

# next button
isNeeded = 0
try:
    element = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/main/div/div/div/form/div[4]/div/div[2]/div/button")))
finally:
    if(chrome.find_element_by_xpath("/html/body/div/div/div[2]/div/main/div/div/div/form/div[4]/div/div[2]/div/button")):
        isNeeded = 1

if (isNeeded == 1):
    element = chrome.find_element_by_xpath("/html/body/div/div/div[2]/div/main/div/div/div/form/div[4]/div/div[2]/div/button")
    chrome.execute_script("arguments[0].click();", element)

# final next button
isNeeded = 0
try:
    element = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div[2]/main/div/div/div/div[3]/span/a")))
finally:
    if(chrome.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/main/div/div/div/div[3]/span/a")):
        isNeeded = 1

if (isNeeded == 1):
    element = chrome.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/main/div/div/div/div[3]/span/a")
    chrome.execute_script("arguments[0].click();", element)
    url = 'http://0.0.0.0:5000/set_status/3' # status update
    resp = requests.get(url)
    url =  MASTER_URL + '/add_email/' + username + "/" + password + "/" + task_id # send credentials to master
    resp = requests.get(url)
else:
    url = 'http://0.0.0.0:5000/set_status/-1' # status update
    resp = requests.get(url)

chrome.quit()
