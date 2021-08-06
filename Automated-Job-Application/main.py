chrome_driver_path="/Applications/chromedriver"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path=chrome_driver_path)
# <-------Page 1------->
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_TPR=r86400&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")
button=driver.find_element_by_link_text("Sign in")
button.click()

# <-------Page 2-sign in credentials------->
email="binitasonitest@gmail.com"
p="2018Bini!"

username=driver.find_element_by_id("username")
username.send_keys(email)
username.send_keys(Keys.ENTER)

password=driver.find_element_by_id("password")
password.send_keys(p)
password.send_keys(Keys.ENTER)

time.sleep(2)
# <-------Page 3-Follow------>


# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

right_pane = driver.find_element_by_class_name("jobs-search__right-rail")
right_pane.click()
from selenium.webdriver.common.keys import Keys

html = driver.find_element_by_tag_name("html")
html.send_keys(Keys.END)
time.sleep(2)
follow = driver.find_element_by_class_name("follow")
follow.click()
driver.close()