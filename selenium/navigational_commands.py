# Navigating between the pages

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver.exe")

driver.get("https://thearjun.tech")
print(driver.title)

time.sleep(2)
# Opens the URL in same tab like we modify the URL tab and press enter.
driver.get("https:github.com/thearjun")
print(driver.title)

# This will navigate to the previous page opened.
time.sleep(2)
driver.back()
print(driver.title)

# This will navigate to the forward page opened.
time.sleep(2)
driver.forward()
print(driver.title)
time.sleep(2)


driver.close()
