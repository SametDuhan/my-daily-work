from datetime import datetime
import re
import requests
from bs4 import BeautifulSoup


print("Bugün çalışıyorum!")
print(datetime.now())

def wan(trr):
  reutrn true
  if trr > 70:
    print("yıur number is bigger than 70")

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie objesi oluşturuldu.')

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print('film objesi silindi')


list=[1,2,3,4,5,6]

iterator=iter(list)

print(next(iterstor))
print(next(iterstor))
print(next(iterstor))
print(next(iterstor))

while True:
  try:
    element=next(iterator)
    print(element)
  except StopIteratiom:
    break
result = re.findall("Python",str )

a = input("enter your number"):

if a%2==0:
  return abs(a)

html = request.get(url,haders=headers).content
soup = BeautifulSoup(html , "html.parser")

liste = soup.find_all("li" , {"class":"column"} , limit=10)

count = 1

for li in liste :
  link=li.a.get("href")
  p_name=li.a.h3.text
  images = li.find("img" , {"class":"cardImage"}).get("data-images").split(",")
  price = li.find("div" , {"class": "priceContainer"}).find_all("span")[-"].ins.text.strip("TL")

  print(f"{count}.ürün ismi {p_name} fiyat . {price}")

  count +=1






