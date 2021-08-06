chrome_driver_path="/Applications/chromedriver"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path=chrome_driver_path)
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
# <-------Page 1------->
try:
 driver.get("https://tinder.com/app/recs")
 time.sleep(10)
 button=driver.find_element_by_xpath('//*[@id="t-1147506855"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
 button.click()
 time.sleep(5)

 button = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/div[1]/div/div[3]/span/div/div/button')
 button.click()
 time.sleep(5)

 windows=driver.window_handles
 base_window=windows[0]

 google_login_window = driver.window_handles[1]
 driver.switch_to.window(google_login_window)
 print(driver.title)

 button = driver.find_element_by_xpath('//*[@id="identifierId"]')
 button.send_keys("areumlee010@gmail.com")
 button.send_keys(Keys.ENTER)

 time.sleep(2)

 button = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
 button.send_keys("2018Bini!")
 button.send_keys(Keys.ENTER)
 time.sleep(5)

 driver.switch_to.window(base_window)
 print(driver.title)
 time.sleep(2)

 location_allow = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/div/div/div[3]/button[1]')
 location_allow.click()
 time.sleep(3)

 notification_enable = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/div/div/div[3]/button[2]')
 notification_enable.click()
 time.sleep(3)

 i_accept = driver.find_element_by_xpath('//*[@id="t-1147506855"]/div/div[2]/div/div/div[1]/button')
 i_accept.click()
 time.sleep(3)

 no_thanks = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/div[1]/button')
 no_thanks.click()
 time.sleep(3)
 for i in range(10):
  try:
   button_like = driver.find_element_by_xpath(xpath='/html/body')
  except NoSuchElementException:
   time.sleep(.5)
   print('error')
   match_popup = driver.find_element_by_xpath('//*[@id="t--1495887802"]/div/div/div[1]/div/div[4]/button/svg/path')
   match_popup.click()
   print("It's a match")
  else:
   for like in range(5):
    button_like.send_keys(Keys.ARROW_RIGHT)
    time.sleep(2)


 # for i in range(100):
 #  try:
 #   like = driver.find_element_by_xpath('//*[@id="t-1147506855"]/div/div[1]/div/div/main/div/div[1]/div[1]/div[2]/div[4]/button')
 #   like.click()
 #   time.sleep(2)
 #   print("Clicking like")
 #  except ElementClickInterceptedException:
 #   try:
 #    match_popup = driver.find_element_by_css_selector(".itsAMatch a")
 #    match_popup.click()
 #    print("It's a match")
 #  # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
 #   except NoSuchElementException:
 #    print("Not found")
 #    time.sleep(2)
except:
    print("Bye")
