from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Path of the executable driver.
# for Mozilla
driver = webdriver.Firefox(executable_path="C:\selenium\geckodriver.exe")
# for Chrome
driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver.exe")

# Desired url
driver.get("https://thearjun.tech")

# Returns the title of the webpage.
print(driver.title)

# Returns the current of the webpage
print(driver.current_url)

# Returns the HTML code for the page.
print(driver.page_source)

# Closes the browser.
driver.close()
