from math import ceil , floor, sqrt
from modulea  import add_a
import random as rr

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

