import requests 
from bs4 import BeautifulSoup
search=""
url=f"https://www.google.com/search?&q={search}"
r=request.get(url)
s=BeautifulSoup(r.text,"html.parser")
update=s.find("div",class_="BNeawe").text
print(updates)
