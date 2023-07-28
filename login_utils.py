import os
from selenium import webdriver

def login():
    
     # get environment variables
    username = os.environ.get('APP_USERNAME')
    password = os.environ.get('APP_PASSWORD')
    login_url = os.environ.get('LOGIN_URL')

    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(login_url)

    username_input = driver.find_element_by_xpath('//*[@id="x-auto-1-input"]')
    password_input = driver.find_element_by_xpath('//*[@id="x-auto-2-input"]')

    username_input.send_keys(username)
    password_input.send_keys(password)

    login_button = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/div/div')
    login_button.click()

    return driver

    # username / password xpath
    # //*[@id="x-auto-1-input"]
    # //*[@id="x-auto-2-input"]

