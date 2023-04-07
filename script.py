import urllib.parse   
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options


base_url="https://mapmybroadband.dps.ny.gov/explore"

 
# address info sometimes get auto changed if exact match not found

street=input("\nPlease enter your street:\n") 
city=input("\nPlease enter your city:\n")
state=input("\nPlease enter your state:\n(Can be in 2 letter format or spelled out)\n")
zip_code=input("\nPlease enter your zip code:\n")



address=[street,city,state,zip_code]
address=", ".join(address)


# target url keeps commas, no conversion to %2C
#https://stackoverflow.com/questions/56722160/how-can-i-escape-certain-characters-while-using-pythons-urllib-urlencode
parsed_address=urllib.parse.quote(address,safe=",")

url=base_url+"?address="+str(parsed_address)


print("\nLoading...\n")

print(f"Scraping from \n{url}\n\n")


options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # https://stackoverflow.com/questions/47392423/python-selenium-devtools-listening-on-ws-127-0-0-1
options.add_argument("--headless")


driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.get(url)


# Click the consent button, which comes up
# prior to the actual map page
consent_btn = driver.find_element_by_id("consentButton")
consent_btn.click()


class_companies = "mat-column-Provider"
class_techs = "mat-column-Tech"


try:
    wait = WebDriverWait(driver, 10)
    
    
    providers = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, "td.mat-column-Provider"))
    techs = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, "td.mat-column-Tech"))
    
    
    #print the text attributes of each element
    res=[]
    print('\n')
    for provider,tech in zip(providers,techs):
        provider_tech_pair=[provider.text,tech.text]
        res.append(provider_tech_pair)
        print(provider_tech_pair)
    

except TimeoutException:
    # if no tech/providers found, TimeoutException is thrown by selenium
    print("\nNo plans were found")

#close the browser
driver.quit()