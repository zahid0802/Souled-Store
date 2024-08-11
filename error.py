from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Use the correct path to the chromedriver executable
driver_path = r"C:\Users\zah\OneDrive\Desktop\st_project-main-main\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)

# Initialize WebDriver
web = webdriver.Chrome(service=service)

# Navigate to the website
web.get("https://www.thesouledstore.com/login?redirect=%2Fmen")

# Wait until the login input field is present
login = WebDriverWait(web, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[2]/div/div[1]/div/nav/div[1]/div/a[1]/span/span/img"))
)
login.send_keys("1234567890")

# Wait until the submit button is clickable
submit = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/form/button"))
)
submit.click()

# Wait for user input to close the browser
input("Press Enter to close the browser...")

web.quit()