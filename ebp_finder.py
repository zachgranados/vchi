#webdriver libraries

from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# helps simulate user behavior, opening banners 
import undetected_chromedriver as uc

# helps mimic random user interactions
import random
import time

# for scraping 
from bs4 import BeautifulSoup


def collect_static_html(url):
# setups up webdriver to model user interactions/preferences

#downlaods chrome diver that is up to date with current veresion of chrome
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")


## using absolute path for right now, should be dynamic path when publishing
    #service = Service(ChromeDriverManager().install())
    driver = uc.Chrome(options=options)

# opens and makes request to url
    driver.get(url)

# waits for randome interval to let js to load page, mimics user random interactions
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

    # reads in full file as html_content
    soup = BeautifulSoup(html_content, 'html.parser')

    # finds the divs that contain provider info
    provider_divs = soup.find_all('div', class_="flex flex-col pt-[2rem] gap-4")

    for div in provider_divs:

        # p tag that holds name
        provider = div.find("p", class_ = "font-bold xs:text-xl sm:text-2xl text-gray-900").text

        # address div
        address_div = div.find("div", class_= "grid grid-cols-1 grid-rows-3 grid-flow-row")
        address = ""

        # set of spans that contain address info
        address_span = address_div.find_all("span")

        # creates address string
        for span in address_span:
            address = address + span.text + " "
        
        # div that contains contact info
        contact_div = div.find("div", class_= "grid grid-cols-1 md:grid-cols-2 lg:grid-cols-1 sm:gap-x-6 gap-y-1")
        
        # contains flexible amount of spans
        contact_spans = contact_div.find_all('span')

        if len(contact_spans) > 2:
           # maybe add website if needed 
            # skips over website if it exists
            email = contact_spans[1].find('a', class_= "text-vcu_navy font-bold hover:underline overflow-hidden text-ellipsis whitespace-nowrap max-w-fit focus:outline-vcu_navy").text

            # goes to third span if it exists
            phone_string = contact_spans[2].text

        # if website span does not exist then it goes to the first link and second span
        else:
        # finding email addresses
            email = contact_div.find('a', class_= "text-vcu_navy font-bold hover:underline overflow-hidden text-ellipsis whitespace-nowrap max-w-fit focus:outline-vcu_navy").text

        # goes to second span
            phone_string = contact_spans[1].text

        

        


        

        # updates dictionary
        ebp_providers[provider] = {
            "Address" : address.strip(),
            "EMAIL" : email,
            "PHONE" : phone_string
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








