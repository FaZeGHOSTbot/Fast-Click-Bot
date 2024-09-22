from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import undetected_chromedriver as uc
import random
from selenium.common.exceptions import TimeoutException
import shutil
import tempfile

# Path to your chromedriver
chrome_driver_path = r"C:\Users\lucif\chromedriver.exe"  # Update with your actual chromedriver path

# Path to your original Chrome user data directory
chrome_profile_path = r"C:\Users\lucif\AppData\Local\Google\Chrome\User Data\Profile 3"  # Update this with your profile path

# Set the desired URL (or open the existing webpage)
url = "The website Link you want to open"

# Function to check for the "Book" button and refresh the page until it's found
def auto_refresh_until_book():
    # Create a temporary directory to hold the profile copy
    temp_dir = tempfile.mkdtemp()

    # Copy the entire profile directory to the temporary folder
    shutil.copytree(chrome_profile_path, f"{temp_dir}\\Profile 3")

    # Start the Chrome WebDriver
    options = uc.ChromeOptions()

    # Use the copied Chrome profile in the temp directory
    options.add_argument(f"user-data-dir={temp_dir}")  # Set the temporary user data directory

    # Fix common Chrome startup issues
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    # Initialize undetected ChromeDriver with options
    driver = uc.Chrome(options=options, executable_path=chrome_driver_path)

    # Open the webpage
    try:
        driver.get(url)
        print(f"Opened URL: {url}")
    except Exception as e:
        print(f"Failed to open URL: {e}")
        driver.quit()
        return
    
    while True:
        try:
            # Check if the "word you are looking for" button is available
            wait = WebDriverWait(driver, 5)  # Max 5 seconds wait for each attempt
            book_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'word you are looking for')]")))
            
            # If the "word you are looking for" button is found, click it
            book_button.click()
            print("Book button clicked!")
            break  # Stop the loop as the button has been found and clicked

        except TimeoutException:
            # If the "Book" button is not found, refresh the page
            print("Book button not found yet, refreshing page...")
            driver.refresh()  # Refresh the page
            time.sleep(random.randint(2,4))  # Wait for 2-6 seconds before refreshing again

    # Pause the script after the button is clicked
    input("Press Enter to close the browser...")

    # Close the browser session (optional)
    driver.quit()

# Run the function
if __name__ == "__main__":
    auto_refresh_until_book()
