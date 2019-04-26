from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver.exe")

driver.get("http://tplinkwifi.net")

# Sad, this username and password field doesn't have name attribute.
# Filling the forms, finding element by name is the best option.
username = driver.find_element_by_id("userName")
password = driver.find_element_by_id("pcPassword")
button = driver.find_element_by_id("loginBtn")

# Sometimes the input field is set disabled. is_enabled() method returns the
# boolean value of its status.
# Sometimes the input field is set not to be displayed on browser like
# setting display: none.
# is_displayed() method returns the boolean value of its status.
print(username.is_displayed(), username.is_enabled())
print(password.is_displayed(), password.is_enabled())

time.sleep(2)
username.send_keys("******")
time.sleep(2)
password.send_keys("******")

time.sleep(2)
button.click()

time.sleep(4)

# The page we selected hadn't check boxes.
# Let's jump to facebook.com for testing.

driver.get("https://facebook.com")

time.sleep(5)

# No double quote inside parameter.
# Preferably, select by CSS selector, in case try other methods.
female = driver.find_element_by_xpath("//*[@id='u_0_6']")
male = driver.find_element_by_xpath("//*[@id='u_0_7']")

print("Female Selected : ", female.is_selected())
print("Male Selected : ", male.is_selected())

driver.quit()
