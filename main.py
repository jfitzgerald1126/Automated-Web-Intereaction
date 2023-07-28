from login_utils import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    driver = login()

    button_to_click = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, ''))
    )

    # schedule click ...
    # or click once and schedule script

    button_to_click.click()

    driver.quit()