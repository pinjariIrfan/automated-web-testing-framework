# automated-web-testing-framework
Selenium + PyTest automation using Page Object Model

# Automated Web Testing Framework

## Project Description
Selenium WebDriver automation framework built with Python and pytest, implementing Page Object Model design pattern.

## Technologies Used
- Python
- Selenium WebDriver
- pytest
- Page Object Model (POM)

## Project Structure
``

automated-web-testing-framework/
├──pages/                 # Page Object Classes
├──tests/                 # Test Cases
├──utilities/             # Helper Functions
├──test_data/             # Test Data Files
├──requirements.txt       # Dependencies
└──README.md             # Documentation

```

## Features
- Page Object Model implementation
- pytest test runner
- Cross-browser testing support
- Reusable test utilities

## Setup & Execution
```bash
pip install -r requirements.txt
pytest tests/ -v
```

```

#### **3. Add requirements.txt**
```

selenium==4.15.0
pytest==7.4.0
pytest-html==3.2.0
webdriver-manager==4.0.0

```

#### **4. Create Page Object Model Files**

**File:** `pages/base_page.py`
```python
"""
Base Page Class - Page Object Model Implementation
Common functionality for all page objects
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click_element(self, locator):
        self.find_element(locator).click()
    
    def enter_text(self, locator, text):
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(text)
```
