import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

WebDriverWait(driver=driver, timeout=50).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error = WebDriverWait(driver=driver, timeout=50).until(EC.presence_of_element_located(
    (By.XPATH, "//span[contains(text(), 'Incorrect email address')]")))

# error = driver.find_element_by_xpath(
#    "//span[contains(text(), 'Incorrect email address')]")

print(error.text)

driver.quit()
