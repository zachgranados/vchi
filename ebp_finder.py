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

from bs4 import BeautifulSoup


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


def collect_provider_info(data_file):

    ebp_providers = {}
    # gets html from file
    with open(data_file, "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    provider_divs = soup.find_all('div', class_="flex flex-col pt-[2rem] gap-4")

    for div in provider_divs:
        provider = div.find("p", class_ = "font-bold xs:text-xl sm:text-2xl text-gray-900").text

        address_div = div.find("div", class_= "grid grid-cols-1 grid-rows-3 grid-flow-row")
        address = ""

        address_span = address_div.find_all("span")

        for span in address_span:
            address = address + span.text + " "
        
        
        
        ebp_providers[provider] = {
            "Address" : address.strip(),
            "EMAIL" : "NULL",
            "PHONE" : "NULL"
        }
    
    
    

    print(ebp_providers)




    # Abigail Brown

    # p, class = font-bold xs:text-xl sm:text-2xl text-gray-900


    # About Change 

    #p, class = font-bold xs:text-xl sm:text-2xl text-gray-900
    return


def main():
    full_webpage = collect_static_html("https://www.ebpfinder.org/")

    with open("ebp.txt", "a+") as file:
        file.write("Full Static Webpage: \n")
        file.write("\n\n")
        file.write(full_webpage)








