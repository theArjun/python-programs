from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver.exe")

# Implicitly waiting.
driver.implicitly_wait(10)
driver.maximize_window()

url = "https://opensource-demo.orangehrmlive.com"
driver.get(url)

time.sleep(5)

driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

time.sleep(3)

driver.find_element_by_id("welcome").click()

# No particular ID, so finding by link text.
driver.find_element_by_link_text("Logout").click()

time.sleep(2)
driver.close()
driver.quit()

print("Test one completed.")
