from login_utils import login

if __name__ == '__main__':
    driver = login()

    button_to_click = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div')

    # /html/body/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div

    # schedule click ...
    # or click once and schedule script

    driver.quit()