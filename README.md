# Automated Web Application Interaction using Selenium WebDriver

This project demonstrates how to automate web application interactions using Selenium WebDriver, a powerful tool for browser automation. The script logs into a web application, clicks a specific button, and performs automated actions using the configuration details specified in 'config.json'.

## Files:

1. `login_utils.py`: This module contains the `login()` function, which automates the login process for the web application. It uses Selenium WebDriver to navigate to the login page, enter the login credentials, and log in.

2. `config_utils.py`: This module contains the `load_config()` function, responsible for reading the configuration data from 'config.json'. The JSON file should contain key-value pairs for configuration settings, including XPaths for locating specific web elements.

3. `main.py`: The main script where the automation process is orchestrated. It calls the `login()` function from `login_utils.py` to log in and obtains the WebDriver instance. Then, it uses the `load_config()` function from `config_utils.py` to load additional configuration details. Finally, it waits for the specified button element (using the XPath from the configuration) to become clickable and clicks the button to perform the desired action on the web application.

4. `run.sh`: A bash wrapper script that sets necessary environment variables and runs `main.py`. This is useful for running the automation via a cron job or scheduling.

## Usage:

1. Ensure you have Python and the necessary libraries installed (Selenium).

2. Download the appropriate Chrome WebDriver version matching your Chrome browser version and place it in the project directory.

3. Create a 'config.json' file in the project directory and set the following configuration settings:
   ```json
   {
       "button_to_click_xpath": "your_button_xpath",
       "chrome_driver": "path/to/chromedriver",
       "username_input_xpath": "your_username_input_xpath",
       "password_input_xpath": "your_password_input_xpath",
       "login_button_xpath": "your_login_button_xpath"
   }
   ```
   Replace the placeholders with the corresponding XPaths for the elements on your login page.

4. Set environment variables `APP_USERNAME`, `APP_PASSWORD`, and `LOGIN_URL` with your login credentials and login URL.

5. If using the bash wrapper script:
    - Make the bash wrapper script executable with `chmod +x script.sh`.
    - Update the environment variable assignments inside the script with your actual values.

6. To run the automation process directly, use the command: `python3 main.py`.

7. To run the automation process via the bash wrapper script, use the command: `./script.sh`.

## Important Note:
Ensure that the 'config.json' file contains the necessary XPaths, especially the 'button_to_click_xpath', which is used to locate the button for clicking.

## Acknowledgements:
- **Selenium**: Selenium is an open-source framework for automating browser interactions. To learn more about Selenium and its capabilities, please visit the official Selenium website: [Selenium Documentation](https://www.selenium.dev/documentation/en/)
- **Chrome WebDriver**: The Chrome WebDriver is a tool provided by Selenium for automating interactions with the Chrome browser. For detailed documentation and instructions on using Chrome WebDriver, please refer to the official ChromeDriver documentation: [ChromeDriver Documentation](https://sites.google.com/a/chromium.org/chromedriver/)
