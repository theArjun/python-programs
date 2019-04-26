from selenium import webdriver
import selenium.webdriver.common.keys as keys
import time

driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver.exe")

driver.get("https://thearjun.tech")

# sleep function will pause the execution of the program for given seconds.
time.sleep(4)
# Finds the element by XPATH. Replace double quotes by single quotes if found.
# Click function is called to click that HTML element.
driver.find_element_by_xpath("/html/body/div[1]/div/button").click()

time.sleep(5)
driver.find_element_by_xpath("/html/body/div[2]/div/div/button/i").click()
time.sleep(2)

# Closes currently focused browser tab.
# driver.close()

# Closes whole browser.
# If multiple tabs have been opened by testing script, then quit() function
# closes all tabs but close() function closes the tab which was requested to
# open at first using get() method.
driver.quit()
