import os
from config_utils import load_config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login():
    """
    Automate the login process for a web application using Selenium WebDriver.

    This function performs the following steps:
    1. Retrieves the login credentials and login URL from environment variables.
    2. Loads additional configuration settings from 'config.json' using the `load_config()` function.
    3. Initializes a Chrome WebDriver with the provided 'chrome_driver' path from the configuration.
    4. Navigates to the login page using the login URL.
    5. Finds the username and password input fields using XPaths from the configuration and enters the credentials.
    6. Locates the login button using the specified XPath and clicks it to initiate the login process.

    Returns:
        webdriver.Chrome: The WebDriver instance after successful login.

    Raises:
        FileNotFoundError: If 'config.json' is not found in the current directory.
    """
    
    # Get environment variables
    username = os.environ.get('APP_USERNAME')
    password = os.environ.get('APP_PASSWORD')
    login_url = os.environ.get('LOGIN_URL')

     # Load additional configuration from 'config.json'
    config = load_config()

    # Initialize Chrome WebDriver with the provided 'chrome_driver' path
    service = Service(executable_path=config['chrome_driver'])
    driver = webdriver.Chrome(service=service)
    driver.get(login_url)

    # Wait for fields to be ready
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, config['username_input_xpath']))
    )
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, config['password_input_xpath']))
    )

    # Enter username / password in fields
    username_input.send_keys(username)
    password_input.send_keys(password)

    # Login
    login_button = driver.find_element(By.XPATH, config['login_button_xpath'])
    login_button.click()

    return driver

