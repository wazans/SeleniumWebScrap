from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Replace the path with the actual path to your chromedriver.exe
# Assuming 'chromedriver.exe' is inside the 'Drivers' folder within your project
chrome_driver_path = r"Drivers\chromedriver.exe"

# Initialize the ChromeDriver service
chrome_service = Service(chrome_driver_path)

# Initialize the WebDriver (Chrome)
driver = webdriver.Chrome(service=chrome_service)

# Open the SauceDemo login page
driver.get("https://www.saucedemo.com/")

# Locate the username field using XPath and enter the username
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))
)
username_field.send_keys("standard_user")

# Locate the password field using XPath and enter the password
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))
)
password_field.send_keys("secret_sauce")

# Locate the login button using XPath and click it
login_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='login-button']"))
)
login_button.click()

# Verify the presence of the specified paragraph
paragraph_text = "A red light isn't the desired state in testing"
paragraph_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, f'//*[contains(text(), "{paragraph_text}")]'))
)

# Verify if the paragraph is present
if paragraph_element.is_displayed():
    print(f"Paragraph is Present on the Page:\n{paragraph_text}\n")
else:
    print(f"Paragraph is NOT Present on the Page:\n{paragraph_text}\n")

# Close the browser window
driver.quit()
