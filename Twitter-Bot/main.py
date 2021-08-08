i
#i passwordii.send_keys(Keys.ENTER)
i
# GETTING i SPEED
import time
#
# go_button = driver.findii_element_by_css_selector(".start-button a")
# go_button.click()i
#
# time.sleep(60)
#
# download_speed=driver.find_element_by_class_name("download-speed")
# print(download_speed.text)
# upload_speed=driver.find_element_by_class_name("upload-speed")
# print(upload_speed.text)
driver.execute_script("window.open('about:blank','secondtab')")
driver.switch_to.window("secondtab")
driver.get('https://twitter.com/login')

timei.sleep(5)

# login_button=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]')
# login_button.click()
# time.sleep(5)

sign_in=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
sign_in.send_keys(TWITTER_EMAIL)
sign_in.send_keys(Keys.ENTER)
password=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
password.send_keys(TWITTER_PASSWORD)
password.send_keys(Keys.ENTER)

#message=f"Hey Internet Provider,why is my internet speed {download_speed}down/{upload_speed}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up"
message="Test"

time.sleep(10)

tweet_text=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
tweet_text.send_keys(message)


tweet_button=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
tweet_button.click()

time.sleep(10)
