chrome_driver_path=r"C:\Users\Shruti Soni\Downloads\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
show_name=input("Enter Show Name:")
#show_name="Red Sleeve"
driver=webdriver.Chrome(executable_path=chrome_driver_path)
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
#https://asianwiki.com/Main_Page
#go to link

try:
 driver.get("https://asianwiki.com/Main_Page")
 time.sleep(5)
 text_area = driver.find_element_by_xpath('/html/body/header/form/input[2]')
 text_area.send_keys(show_name)
 text_area.send_keys(Keys.ENTER)
 time.sleep(4)
 result=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/ul[1]/li/div[1]/a')
 result.click()
 time.sleep(4)
 synopsis= driver.find_element_by_xpath('//*[@id="mw-content-text"]/p[5]')
 print(synopsis.text)

 driver.close()
except:
 print("Bye")
#type the show name
#click on first link
#copy synopsis
#print