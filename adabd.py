from math import ceil , floor, sqrt
from modulea  import add_a
import random as rr
from datetime import datetime
from datetime import timedelta
import requests
import json




while True:
    try:
        enetered = int(input("Enter a number: "))
        print(enetered.add_a())
        break
    except Exception as e:
        print(f"you have a {e} problem check it")
    
ent_number1=input("enter a number : ")

if ent_number % 2 ==0:
    return sqrt(ent_number)

a = rr.random()

if a <= ent_number:
    if a * 100 == range(12,34):
        print("your number is tge greatest number ever ")
    elif a*100 == range (34,67):
        print("not the best number but still good")
    elif a*100== range(67,100):
        print("sorry you are not lucky today")
    else:
        pass
        
def outer(num1):
    print('outer')
    def inner_increment(num1):
        print('inner')
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1, num2)

outer(10)

def factorial(number):
    if not isinstance(number,int):
        raise TypeError("number must be an integer")
    if not number >= 0:
        raise ValueError("number must be zero or positive")

    def inner_factorial(number):
        if number <= 1:
            return 1
        return inner_factorial(number)

try:
    print(factorial("4"))
except Exception as ex:
    print(ex)


simdi = datetime.now()
simdi = datetime.today()

result = datetime.ctime(simdi)
result = datetime.strftime(simdi,'&A')

api_key="<your_api_key>"
api_url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("Bozulan döviz türü: ") 
alinan_doviz = input("Alkınan döviz türü: ") 
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: ")) 

