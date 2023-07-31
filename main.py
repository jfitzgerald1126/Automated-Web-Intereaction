from login_utils import login
from config_utils import load_config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

if __name__ == '__main__':
    """
    Main script for logging into a web application and clicking a button using Selenium WebDriver.

    This script demonstrates the login process using the `login()` function from 'login_utils',
    which utilizes Selenium WebDriver to perform the login operation. The login credentials and
    login URL are expected to be set as environment variables. Additionally, the 'config_utils'
    module is used to load configuration data from 'config.json', which should contain XPaths
    for locating specific web elements.

    The script does the following steps:
    1. Calls the 'login()' function to log in to the web application and returns the WebDriver instance.
    2. Loads additional configuration settings from 'config.json' using the `load_config()` function.
    3. Waits for the specified button element (using its XPath from the configuration) to be clickable.
    4. Clicks the button to perform the desired action on the web application.

    Important Note:
    Make sure 'config.json' contains the necessary XPaths, including the 'button_to_click_xpath'
    used to locate the button for clicking.
    """
    try:
        driver, display = login()
        config = load_config()

        # Wait for the button element to be clickable
        button_to_click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config['button_to_click_xpath']))
        )

        # schedule click ...
        # or click once and schedule script

        button_to_click.click()

        print("Succesfully refreshsed at " + str(datetime.datetime.now()))

        driver.quit()
        display.stop()
        

    except Exception as e:
        # Handle exceptions
        raise e