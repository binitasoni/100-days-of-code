chrome_driver_path="/Applications/chromedriver"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
# price=driver.find_element_by_id("") --> selemium object by id
# print(price.text) ----> text
search_bar=driver.find_element_by_id("cookie")
search_bar.click()
#search_bar=driver.find_element_by_name("q") --> selemium object by name
#print(searchbar.get_attributes("placeholder"))  ----> attribute

# logo=driver.find_element_by_class_name() --> selemium object by class name
driver.close()
driver.quit()