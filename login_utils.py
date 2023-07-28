import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login():
    
    # get environment variables
    username = os.environ.get('APP_USERNAME')
    password = os.environ.get('APP_PASSWORD')
    login_url = os.environ.get('LOGIN_URL')

    service = Service(executable_path='C:\chromedriver\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get(login_url)

    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, ''))
    )
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, ''))
    )

    username_input.send_keys(username)
    password_input.send_keys(password)

    login_button = driver.find_element('xpath', '')
    login_button.click()

    return driver

    # username / password xpath
    # //*[@id="x-auto-1-input"]
    # //*[@id="x-auto-2-input"]

