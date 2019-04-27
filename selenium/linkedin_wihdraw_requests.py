# Cancel all the LinkedIn sent invitations

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
# For entering password from console
import getpass
# For quitting app if login fails.
import sys


driver = webdriver.Firefox(executable_path="C:\selenium\geckodriver.exe")
driver.get("https://www.linkedin.com")

try:
    # Linkedin serves two login page : One Clean UI and other old design.
    # This try block is for Clean UI.
    sign_in = driver.find_element_by_class_name("nav__button-secondary")
    print('Sign In Link Display : ', sign_in.is_displayed())
    sign_in.click()

    email = driver.find_element_by_name("session_key")
    password = driver.find_element_by_name("session_password")
    login = driver.find_element_by_css_selector(".btn__primary--large")

    print("In Clean UI Page : ")
    print("email Display : ", email.is_displayed())
    print("Password Display : ", password.is_displayed())
    print("Login Display : ", login.is_displayed())

except NoSuchElementException:

    # This block is for old designed UI.
    email = driver.find_element_by_id("login-email")
    password = driver.find_element_by_id("login-password")
    login = driver.find_element_by_id("login-submit")

    print("In Old Designed Page : ")
    print("email Display : ", email.is_displayed())
    print("Password Display : ", password.is_displayed())
    print("Login Display : ", login.is_displayed())

em = input("Enter Email : ").rstrip()
email.send_keys(em)
pwd = getpass.getpass("Enter password : ")
password.send_keys(pwd)
login.click()

login_status = False

# Checking if user has login successfully or not.
try:
    messaging_check = driver.find_element_by_id("messaging-nav-item")
except NoSuchElementException:
    print("\nLogin failed.")
    sys.exit(0)


print("Successfully Logged in.")

driver.get("https://www.linkedin.com/mynetwork/invitation-manager/sent/")

limit = 0

while not limit > 0:
    limit = int(input("\nLeave empty if you want to withdraw all requests.\n"
                      "Enter numeric value starting from 0 to your choice\n"
                      "Enter how many withdraw you want : "))

withdraw_count = 0

while True:
    try:
        if withdraw_count <= limit:
            withdraw = driver.find_element_by_class_name(
                "invitation-card__action-btn")
            withdraw.click()
            time.sleep(2)
            withdraw_count += 1
        else:
            print("Request withdraw completed.")
            break
    except NoSuchElementException:
        print("No request to withdraw.")
        break
