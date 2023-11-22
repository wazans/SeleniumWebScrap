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
# Open the webpage
driver.get("https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html")

# Locate the table element
table = driver.find_element_by_xpath('//tbody/tr[1]/td[1]')

# Find all rows in the table
rows = table.find_elements_by_tag_name("tr")

# Iterate through each row and print cell values
for row in rows:
    cells = row.find_elements_by_tag_name("td")
    for cell in cells:
        cellText = cell.text
        print(cellText)

# Close the browser
driver.quit()
