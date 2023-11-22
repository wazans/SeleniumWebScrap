from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service  # Add this import
import time

# Replace the path below with the actual path to your ChromeDriver executable
# Assuming 'chromedriver.exe' is inside the 'Drivers' folder within your project
chrome_driver_path = r"Drivers\chromedriver.exe"


# Initialize the ChromeDriver service
chrome_service = Service(chrome_driver_path)

# Initialize the WebDriver (Chrome)
driver = webdriver.Chrome(service=chrome_service)

# Open OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/")

# Wait for up to 10 seconds for the username field to be present
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)

# Fill in login credentials
password_field = driver.find_element("name", "password")
username_field.send_keys("Admin")
password_field.send_keys("admin123")

# Wait for up to 10 seconds for the login button to be present
login_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
)

# Clicking the login button
login_button.click()

# Pause for login process
time.sleep(2)

# Verify the presence of the text 'Employee Distribution by Sub Unit'
employee_distribution_text = "Employee Distribution by Sub Unit"
employee_distribution_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, f"//p[normalize-space()='{employee_distribution_text}']"))
)

# Verify if the text is present
if employee_distribution_element.is_displayed():
    print(f"Text '{employee_distribution_text}' is Present on the Home Page.")
else:
    print(f"Text '{employee_distribution_text}' is NOT Present on the Home Page.")

# Close the browser window
driver.quit()
