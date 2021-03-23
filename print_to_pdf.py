from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
import math

CHROMEDRIVER_PATH = 'chromedriver.exe'


def print_to_pdf(link):
    appState = {
        "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2
    }
    prefs = {
        'printing.print_preview_sticky_settings.appState': json.dumps(appState)
    }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--kiosk-printing')
    driver = webdriver.Chrome(
        executable_path=CHROMEDRIVER_PATH, options=chrome_options)
    driver.get(link)
    total_height = int(driver.execute_script(
        "return document.body.scrollHeight"))
    for i in range(1, total_height, math.floor(total_height*.05)):
        driver.execute_script("window.scrollTo(0, {});".format(i))
        time.sleep(2)  # delayed scrolling to fetch all images
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(driver, 20)
    driver.execute_script('window.print();')
    driver.quit()
