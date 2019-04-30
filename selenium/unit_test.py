from selenium import webdriver
import time
import unittest


class LoginTest (unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(
            executable_path="C:\selenium\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):

        url = "https://opensource-demo.orangehrmlive.com"
        self.driver.get(url)
        time.sleep(2)
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        time.sleep(2)
        self.driver.find_element_by_id("welcome").click()
        # No particular ID, so finding by link text.
        self.driver.find_element_by_link_text("Logout").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):

        cls.driver.close()
        cls.driver.quit()
        print("Test one completed.")


if __name__ == "__main__":
    # To make it run without python -m unittest unit_test.py
    unittest.main()
