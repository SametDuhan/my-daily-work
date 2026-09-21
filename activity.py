from datetime import datetime

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
a = input("enter your number"):

if a%2==0:
  return abs(a)
