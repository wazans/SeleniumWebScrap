from selenium.webdriver.support import expected_conditions as EC

from openpyxl import Workbook
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

# Replace the path below with the actual path to your ChromeDriver executable
chrome_driver_path = r"Drivers\chromedriver.exe"

# Initialize the ChromeDriver service
chrome_service = Service(chrome_driver_path)

# Initialize the WebDriver (Chrome)
driver = webdriver.Chrome(service=chrome_service)

# Open the W3Schools HTML Tables example page
driver.get("https://www.w3schools.com/html/html_tables.asp")

workbook = Workbook()
sheet = workbook.active

# Write header to Excel
sheet['A1'] = 'Company'
sheet['B1'] = 'Contact'
sheet['C1'] = 'Country'

# Wait for up to 10 seconds for the username field to be present
customer_table_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//table[@id='customers']/tbody/tr"))
)
# Locate the table rows containing the data
table_rows = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr")

# Loop through each row and extract data
for row in table_rows:
    try:
        # Extracting data from each column in the row
        company = row.find_element(By.XPATH, ".//td[1]").text
        contact = row.find_element(By.XPATH, ".//td[2]").text
        country = row.find_element(By.XPATH, ".//td[3]").text

        # Write data to Excel
        sheet.append([company, contact, country])
    except NoSuchElementException as e:
        #   Check if it's the header row
        if "Skipping row" not in row.text:
            # Handle the case where the element is not found in the row
            print(f"Error: {e}")
            print(f"Skipping row: {row.text}")

# Save the Excel file to the 'Drivers' folder
excel_file_path = 'Drivers/extracted_data.xlsx'
workbook.save(excel_file_path)

# Close the browser
driver.quit()
