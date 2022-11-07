import os.path
import json
base = ["Name","Age","Position"]
while True:
     v=input("1.(add)\n2.(find)\n3.(dell)\n")
     if v=="quit":
        break
     if v=="1":
         count=0
         path=os.path.join("hi","spiv")
         file=open(path,"r")
         dict = json.load(file)
         a=input("Enter name: ")
         b=input("Enter age: ")
         c=input("Enter Position: ")
         dict[a] = {"Age":b, "Position":c}
         file.close()
         file = open(path, "w")
         json.dump(dict, file)
         file.close()
     if v=="2":
         path = os.path.join("hi", "spiv")
         file = open(path, "r")
         list = json.load(file)
         file.close()
         a=input("Enter name: ")
         for i in list:
            if i==a:
                 print(i,"This worker is on the list")
     if v=="3":
         path = os.path.join("hi", "spiv")
         file = open(path, "r")
         list = json.load(file)
         file.close()
         a = input("Enter name to delete: ")
         list.pop(a)
         file = open(path, "w")
         json.dump(list, file)