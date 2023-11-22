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

# Open the "Quotes to Scrape" website
driver.get("http://quotes.toscrape.com/js/")

# Initialize an empty list to store quotes
all_quotes = []

# Function to extract and print quotes from the current page
def extract_quotes():
    quotes = driver.find_elements(By.CLASS_NAME, "text")
    for quote in quotes:
        all_quotes.append(quote.text)
        print(quote.text)

# Extract quotes from the initial page
extract_quotes()

# Loop to navigate through multiple pages using the "Next" button
while True:
    try:
        # Click the "Next" button to load more quotes (AJAX request)
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@class='next']/a"))
        )
        next_button.click()

        # Wait for the quotes to load on the next page
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "text"))
        )

        # Extract quotes from the current page
        extract_quotes()

    except Exception as e:
        # Break the loop if there is no "Next" button (reached the last page)
        print(f"No more pages: {e}")
        break

# Print all quotes collected
print("All Quotes:")
print(all_quotes)

# Close the browser
driver.quit()