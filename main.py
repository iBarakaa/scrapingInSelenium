from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# the selenium version used is v. 4.0.0.b4

# path for chromedriver
# conversion of backslash to forward slashes
s = Service("C:/SeleniumDrivers/chromedriver.exe")

# we give our driver a path
driver = webdriver.Chrome(service= s)

# opening website
driver.get("https://www.nse.co.ke/dataservices/market-statistics/")

# # use of the Xpaths
# # you can procure the Xpath throuh
# driver.find_element_by_xpath()