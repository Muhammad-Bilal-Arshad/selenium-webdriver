from selenium import webdriver 

BINARY_LOCATION = "/usr/bin/google-chrome" 

# Start selenium with ChromeOptions
options = webdriver.ChromeOptions() 
options.binary_location = BINARY_LOCATION 
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# WebDriver will automatically use the 'chromedriver' in the system's PATH
driver = webdriver.Chrome(options=options) 

# Visit Google's homepage
driver.get("https://www.google.com/") 

# Print the page source
print(driver.page_source.encode('utf-8')) 

# Close browser and quit driver
driver.close() 
driver.quit()
