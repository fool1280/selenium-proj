import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

load_dotenv()
DEBUG = os.getenv('DEBUG')
URL = os.getenv('URL')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

chrome_options = webdriver.ChromeOptions()
if DEBUG == 'TRUE':
    chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

driver.find_element_by_id("username").send_keys(USERNAME)
driver.find_element_by_id("login-submit").click()
driver.implicitly_wait(10)
driver.find_element_by_id("password").send_keys(PASSWORD)
driver.find_element_by_id("login-submit").click()

WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect email address and / or password."
errors = driver.find_elements_by_id("login-error")

if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")

driver.close()
