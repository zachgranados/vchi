from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# trying to fly under radar
import undetected_chromedriver as uc

import random
import time


def collect_static_html(url):
# setups up webdriver to model user interactions
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")


## using absolute path for right now, should be dynamic path when publishing
    #service = Service(ChromeDriverManager().install())
    driver = uc.Chrome(options=options)

# opens and makes request to url
    driver.get(url)

# waits for js to load page

    time.sleep(random.uniform(5, 10))


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







