### Auto-refresh and Book Script for Event Tickets using Selenium and Undetected ChromeDriver

This Python script automates the process of booking tickets for events on the BookMyShow website. It continuously refreshes the page until the "Book" button becomes available and automatically clicks it once found. The script uses Selenium WebDriver with undetected ChromeDriver to avoid detection by automated browsing restrictions.

It is mainly focused for the use of getting quick access to something which has a first come first serve basis on the internet and does the job for you.

#### Features:
- **Auto-Refresh Mechanism**: The script refreshes the page at random intervals to mimic human behavior until the "Book" button appears.
- **Chrome User Profile Support**: It clones an existing Chrome user profile for a more seamless browsing experience.
- **Undetected Browsing**: Uses `undetected-chromedriver` to bypass automated browser detection, avoiding CAPTCHA or blocking mechanisms.
- **Customizable Paths**: Easily specify paths to ChromeDriver and Chrome profiles.

#### Prerequisites:
- Python 3.x
- Selenium
- Undetected ChromeDriver
- Google Chrome
- Chromedriver matching your Chrome version

#### How to Use:
1. Install the necessary packages via `selenium`, `undetected_chromedriver`.
2. Update the script with your own ChromeDriver path and Chrome profile path.
  -Search `chrome://version/` on your chrome browser to check the version.
  -Download necessary chromedriver from `https://developer.chrome.com/docs/chromedriver/downloads` and paste it in the root folder and use the root folder to define the path in the `index.py`.
3. Run the script, and it will refresh the page until the "Text you are searching for" button appears and clicks it.

#### Important Notes:
- Ensure your ChromeDriver version matches your installed Chrome version.
- This script is intended for educational purposes and should be used responsibly.
