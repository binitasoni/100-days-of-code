from bs4 import BeautifulSoup
import requests
import time
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
    "Accept-Language": "en-US"
}

response = requests.get(
    f"https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.76566542578125%2C%22east%22%3A-121.96229018164063%2C%22south%22%3A37.55951075840637%2C%22north%22%3A37.955802123601366%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D",
    headers=headers)
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")
# print(response.text)
address = soup.find_all(class_="list-card-addr")
address_list = []
for a in address:
    addr = a.getText()
    addr.replace('|', " ")
    address_list.append(addr)
print(address_list)

prices = soup.find_all(class_="list-card-price")
prices_list = []
for p in prices:
    price = p.getText()
    price.strip("/mo")
    price.strip("/mo+ 1 bd")
    prices_list.append(price)
print(prices_list)

links = soup.find_all(class_="list-card-link")
link_list=[]
for l in links:
    link = l['href']
    if link.startswith('/b'):
        link = 'https://zillow.com' + link
        link_list.append(link)
    else:
        link_list.append(link)

print(link_list)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path="/Applications/chromedriver"
driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://forms.gle/UdQ2uX14WbnNPUcN8")
for i in range(len(address_list)):
  time.sleep(2)
  add_input=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
  add_input.send_keys(address_list[i])

  price_input=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
  price_input.send_keys(prices_list[i])

  link_input=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
  link_input.send_keys(link_list[i])


  button=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
  button.click()
  driver.back()
  driver.refresh()

driver.close()