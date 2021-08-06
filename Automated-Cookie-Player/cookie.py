# chrome_driver_path="/Applications/chromedriver"
# from selenium import webdriver
# driver=webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get("http://orteil.dashnet.org/experiments/cookie/")
# search_bar=driver.find_element_by_id("cookie")
#
# print(search_bar)
#
#
# money=driver.find_element_by_id("money")
# test = driver.find_elements_by_css_selector("#store div b")
# prices = []
# names = []
#
#
# import time
# timeout = time.time() + 60   # 5 minutes from now
# five_seconds= time.time() + 5   # 5 secs from now
# while True:
#
#     if time.time() > timeout:
#         break
#     if time.time()==five_seconds:
#         for t in test:
#             if len(prices) < 5:
#                 print(t.text)
#                 names.append(t.text.split()[0])
#                 p = t.text.split()[2]
#
#                 if "," in p:
#                     b = p.split(",")
#                     print(b)
#                     a = b[0] + b[1]
#                     prices.append(a)
#                 else:
#                     prices.append(p)
#                 i = 0
#                 print(prices)
#                 print(money.text)
#                 for price in prices:
#
#                     if int(price) < int(money.text):
#                         i = i + 1
#                 id = f"buy{names[i]}"
#                 shop = driver.find_element_by_id(id)
#                 shop.click()
#         names.append("Alchemy Lab")
#         prices.append("50000")
#         names.append("Portal")
#         prices.append("1000000")
#         names.append("Time Machine")
#         prices.append("123456789")
#         print(names)
#

# driver.close()












