chrome_driver_path="/Applications/chromedriver"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")
count=driver.find_element_by_name("fName")
count.send_keys("Bini")
count.send_keys(Keys.ENTER)

count=driver.find_element_by_name("lName")
count.send_keys("Soni")
count.send_keys(Keys.ENTER)

count=driver.find_element_by_name("email")
count.send_keys("bini@sofg.com")
count.send_keys(Keys.ENTER)

count=driver.find_element_by_class(".btn")
count.click()
driver.close()