"""
Test Cases using pytest and POM
Testing login functionality
"""
import pytest
from selenium import webdriver
from pages.login_page import LoginPage

class TestLogin:
    @pytest.fixture
    def setup(self):
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)
        yield
        self.driver.quit()
    
    def test_valid_login(self, setup):
        """Test successful login with valid credentials"""
        self.driver.get("https://www.saucedemo.com/")
        self.login_page.login("standard_user", "secret_sauce")
        assert "inventory" in self.driver.current_url
        print("✅ Valid login test passed")
    
    def test_invalid_login(self, setup):
        """Test login with invalid credentials"""
        self.driver.get("https://www.saucedemo.com/")
        self.login_page.login("invalid_user", "wrong_password")
        error_message = self.login_page.get_error_message()
        assert "Username and password do not match" in error_message
        print("✅ Invalid login test passed")

# Run with: pytest tests/test_login.py -v