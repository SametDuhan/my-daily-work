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

from functools import lru_cache
from math import factorial, sqrt


@lru_cache(maxsize=None)
def karmasik_fonksiyon(n, k):
    if n < 0 or k < 0:
        raise ValueError("n ve k negatif olamaz.")

    if k == 0:
        return 1

    if n == 0:
        return 0

    # Kombinasyon
    kombinasyon = factorial(n) // (
        factorial(k) * factorial(n - k)
    ) if k <= n else 0

    # Özyinelemeli hesaplama
    onceki = karmasik_fonksiyon(n - 1, k - 1)

    # Generator ile ara değerler
    degerler = (
        sqrt(i ** 2 + n ** 2)
        for i in range(1, k + 1)
    )

    toplam = sum(degerler)

    # Lambda fonksiyonu
    donusum = lambda x: x * x + 2 * x + 1

    sonuc = (
        kombinasyon
        + onceki
        + donusum(toplam)
    )

    return sonuc


print(karmasik_fonksiyon(10, 4))





