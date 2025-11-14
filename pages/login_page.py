"""
Login Page - Page Object Model
Demo website: https://www.saucedemo.com/
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators using POM
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password") 
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")
    
    def enter_username(self, username):
        self.enter_text(self.USERNAME_FIELD, username)
    
    def enter_password(self, password):
        self.enter_text(self.PASSWORD_FIELD, password)
    
    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)
    
    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text
    
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()