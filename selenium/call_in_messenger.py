from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# For allowing microphone
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver.exe")

driver.get("https://messenger.com")

username = driver.find_element_by_name("email")
password = driver.find_element_by_name("pass")
button = driver.find_element_by_id("u_0_2")

username.send_keys("********")
password.send_keys("********")
button.click()

# For allowing microphone in Browser
chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
webdriver.Chrome(chrome_options=chrome_options)

# Hardcoded XPATH for selecting user
driver.find_element_by_xpath(
    "/html/body/div[1]/div/div/div[1]/div[2]/div[3]/div[1]/div[1]/div/div/div[2]/div/ul/li[3]/div[1]/a/div/div[1]/div/div/div/div/img"
).click()

active_status = driver.find_element_by_css_selector("._2v6o").text
if active_status == "Active now":
    # CSS selector for voice call
    driver.find_element_by_css_selector(
        "._fl2 > li:nth-child(1) > a:nth-child(1) > div:nth-child(1) > svg:nth-child(1)"
    ).click()

time.sleep(5)
driver.close()
