from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

# the selenium version used is v. 4.0.0.b4

# path for chromedriver
# conversion of backslash to forward slashes

s = Service("C:/SeleniumDrivers/chromedriver.exe")

# we give our driver a path
driver = webdriver.Chrome(service= s)

# opening website
driver.get("https://www.nse.co.ke/dataservices/market-statistics/")
time.sleep(10)

# navigation to the equity statistics resources
equity_statistics = driver.find_element(by="xpath", value="/html/body/div[1]/div/div[3]/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/ul/li[2]/a/span")
equity_statistics.click()
time.sleep(5)

es_dropdown = Select(driver.find_element(by="xpath", value="/html/body/div[1]/div/div[3]/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div[1]/form/select"))

# entries within the selected dropdown
options = [option.text for option in es_dropdown.options]

for option in options:
    if option != "Select Sector":
        try:
            es_dropdown.select_by_visible_text(option)
            print(option)
            time.sleep(5)
        except:
            continue


# shares = driver.find_elements(by="xpath", value="/html/body/div[1]/div/div[3]/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/table/tbody/tr")

# for share in shares:
#     print(shares.text)