from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# the selenium version used is v. 4.0.0.b4

# path for chromedriver
# conversion of backslash to forward slashes

s = Service("C:/SeleniumDrivers/chromedriver.exe")

# we give our driver a path
driver = webdriver.Chrome(service= s)

# opening website
driver.get("https://www.nse.co.ke/dataservices/market-statistics/")

equity_statistics = driver.find_element(by="xpath", value="/html/body/div[1]/div/div[3]/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/ul/li[2]/a/span")
equity_statistics.click()
