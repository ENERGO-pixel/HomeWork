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
cars2 = Car(color="blue",type="A-4",year="2003")
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
     def __str__(self):
         file = open(self.path, "r")
         list=json.load(file)
         file.close()
         return str(list)