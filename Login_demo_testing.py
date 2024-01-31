import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Login_demo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(3)


    def testLogin1(self): #Wrong username and password

        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("vali")
        username.send_keys(Keys.RETURN)
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("12345")
        login_btt = self.driver.find_element(By.ID, "login-button")
        login_btt.send_keys(Keys.RETURN)
        message = self.driver.find_element(By.CSS_SELECTOR,
                                           "#login_button_container > div > form > div.error-message-container.error")
        print(message.text)
        self.assertIn("Username and password do not match any user in this service", message.text)

    def testLogin2(self): #Correct username, wrong password

        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        username.send_keys(Keys.RETURN)
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("12345")
        login_btt = self.driver.find_element(By.ID, "login-button")
        login_btt.send_keys(Keys.RETURN)
        message = self.driver.find_element(By.CSS_SELECTOR,
                                           "#login_button_container > div > form > div.error-message-container.error")
        print(message.text)
        self.assertIn("Username and password do not match any user in this service", message.text)

    def testLogin3(self): #Wrong username, correct password

        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_use")
        username.send_keys(Keys.RETURN)
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        login_btt = self.driver.find_element(By.ID, "login-button")
        login_btt.send_keys(Keys.RETURN)
        message = self.driver.find_element(By.CSS_SELECTOR,
                                           "#login_button_container > div > form > div.error-message-container.error")
        print(message.text)
        self.assertIn("Username and password do not match any user in this service", message.text)

    def testLogin4(self): #Blank username field

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        login_btt = self.driver.find_element(By.ID, "login-button")
        login_btt.send_keys(Keys.RETURN)
        message = self.driver.find_element(By.CSS_SELECTOR,
                                           "#login_button_container > div > form > div.error-message-container.error")
        print(message.text)
        self.assertIn("Username is required", message.text)

    def testLogin5(self): #Blank password field

        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        username.send_keys(Keys.RETURN)
        login_btt = self.driver.find_element(By.ID, "login-button")
        login_btt.send_keys(Keys.RETURN)
        message = self.driver.find_element(By.CSS_SELECTOR,
                                           "#login_button_container > div > form > div.error-message-container.error")
        print(message.text)
        self.assertIn("Password is required", message.text)

    def testLogin6(self): #Succesful login

        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        username.send_keys(Keys.RETURN)
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        login_btt = self.driver.find_element(By.ID, "login-button")
        login_btt.send_keys(Keys.RETURN)
        swag = self.driver.find_element(By.CSS_SELECTOR, "#header_container > div.primary_header > div.header_label > div")
        print(swag.text)
        self.assertIn("Swag Labs", swag.text)


if __name__ == '__main__':
    unittest.main()