from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import os

# Grab secrets from GitHub Actions
MMO_URL = os.environ['MMO_URL']
EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']

# Initialize headless Firefox options
options = Options()
options.add_argument('-headless')

# Initialize the driver with the Service object
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

# Navigate to the login page
driver.get(MMO_URL)

# Fill in the login form
driver.find_element(by=By.ID, value='email').send_keys(EMAIL)
driver.find_element(by=By.ID, value='password').send_keys(PASSWORD)
driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()

# Wait for the login to complete (adjust timeout as needed)
driver.implicitly_wait(10)

# You are now logged in!
print("Page Title:", driver.title)
driver.quit()
