# Cancel all the LinkedIn sent invitations


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# For waiting page to fully load
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Firefox(executable_path="your_path")

lst = []

driver.get("https://www.linkedin.com")


try:
    sign_in = driver.find_element_by_class_name("nav__button-secondary")
    print('Sign In Link Display : ', sign_in.is_displayed())
    sign_in.click()

    email = driver.find_element_by_name("session_key")
    password = driver.find_element_by_name("session_password")
    login = driver.find_element_by_css_selector(".btn__primary--large")

    # print("In Clean UI Page : ")
    # print("email Display : ", email.is_displayed())
    # print("Password Display : ", password.is_displayed())
    # print("Login Display : ", login.is_displayed())

except:

    email = driver.find_element_by_id("login-email")
    password = driver.find_element_by_id("login-password")
    login = driver.find_element_by_id("login-submit")

    # print("In Old Designed Page : ")
    # print("email Display : ", email.is_displayed())
    # print("Password Display : ", password.is_displayed())
    # print("Login Display : ", login.is_displayed())

email.send_keys("mailarjunadhikari@gmail.com")
password.send_keys("********")
login.click()

# WebDriverWait(driver, 10)

driver.get("https://www.linkedin.com/mynetwork/invitation-manager/sent/")

while True:
    try:
        withdraw = driver.find_element_by_class_name(
            "invitation-card__action-btn")
        withdraw.click()
        time.sleep(2)
    except:
        break
