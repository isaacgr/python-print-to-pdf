import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://excesssoilnotices.rpra.ca/s/?language=en_US'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('user-data-dir=C:\\Users\\Isaac\\Documents')
chrome_options.binary_location = '/mnt/c/Program Files (x86)/Google/Chrome/Application/chrome.exe'
chrome_options.add_argument('--disable-dev-shm-usage') # Add this option

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

links = driver.find_elements(By.CLASS_NAME, "darkish-green.cRegistryPublicPortalFilingAction")

for link in links:
    print(link)
    break
    if link.text == "View":
        print(link)
        #link.click()
        # code to interact with the resulting page after clicking on the link goes here

driver.quit()

