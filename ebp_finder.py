from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


def collect_static_html(url):
# setups up webdriver to model user interactions

## using absolute path for right now, should be dynamic path when publishing
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

# opens and makes request to url
    driver.get(url)

# waits for js to load page
    #wait = WebDriverWait(driver, 5000)

    time.sleep(5)


    # waits for the first name to appear?
    #wait.until(EC.presence_of_element_located((By.CLASS_NAME, "font-bold xs:text-xl sm:text-2xl text-gray-900")))  # Change to a relevant element ID


# closer driver
    driver.quit()

## might need to insert script to get all 113 to load testing with initial 25 first

    return driver.page_source





full_webpage = collect_static_html("https://www.ebpfinder.org/")

with open("ebp.txt", "a+") as file:
    file.write("Full Static Webpage: \n")
    file.write("\n\n")
    file.write(full_webpage)







