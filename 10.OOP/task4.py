import os.path
import json
class Car:
     def __init__(self,color,type,year):
         self.color = color
         self.type = type
         self.year = year
     def __str__(self):
         return f"{self.type}, {self.color}, {self.year}"
cars1 = Car(color="red",type="B-2",year="2001")
cars2 = Car(color="red",type="A-4",year="2003")
class Carsalon:
     def __init__(self):
         self.path=os.path.join("hi","bob.json")
     def add_car(self,car):
         file = open(self.path, "r")
         dict = json.load(file)
         dict[car.type] = {"Color":car.color,"Year":car.year}
         file.close()
         file = open(self.path, "w")
         json.dump(dict, file)
         file.close()
         return "Adding car"
     def buy_car(self,lin):
         file = open(self.path, "r")
         list = json.load(file)
         file.close()
         list.pop(lin)
         file = open(self.path, "w")
         json.dump(list, file)
         file.close()
         return "kva"
     def diff(self):
         if cars1.type==cars2.type:
            print(cars1.type)
         else:
            print(cars1.type,cars2.type)
         if cars1.color == cars2.color:
            print(cars1.color)
         else:
            print(cars1.color, cars2.color)
         if cars1.year == cars2.year:
            print(cars1.year)
         else:
            print(cars1.year, cars2.year)
         return "kva"
     def __str__(self):
         file = open(self.path, "r")
         list=json.load(file)
         file.close()
         return str(list)
AndreyCar=Carsalon()
print(AndreyCar.add_car(cars1))
print(AndreyCar.add_car(cars2))
print(AndreyCar)
print(AndreyCar.diff())
a=input("Enter what you buy: ")
print(AndreyCar.buy_car(a))
print(AndreyCar)
print("ae86","ae85");print("gray");print("1983","1981")