from bs4 import BeautifulSoup
# f = open("website.html", "r")
# contents=f.read()
# soup=BeautifulSoup(contents,'html.parser')
# print(soup.title.string)
import requests
response=requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
yc_webpage=response.text
soup=BeautifulSoup(yc_webpage,"html.parser")
texts=soup.find_all(name="h3",class_ ="jsx-4245974604")
print(texts)
