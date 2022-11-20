import os.path
base = ["Name","Age","Position"]
while True:
     v=input("1.(add)\n2.(find)\n3.(dell)\n")
     if v=="quit":
        break
     if v=="1":
         count=0
         path=os.path.join("hi","spiv")
         file=open(path,"a")
         while count<len(base):
            file.write(input(base[count]+" : ")+" ")
            count+=1
         file.write("\n")
     if v=="2":
         path = os.path.join("hi", "spiv")
         file = open(path, "r")
         a=input("Enter name to find: ")
         for i in file:
            for j in i.split():
                if a==j:
                    print(i.replace("\n",""))
                    break
     if v=="3":
         path = os.path.join("hi", "spiv")
         file = open(path, "r")
         a = input("Enter name to delete: ")
         line=[i for i in file]
         print(line)
         for i in line:
            for j in i.split():
                if a==j:
                    del line[line.index(i)]
                    break
     file = open(path, "w")
     for i in line:
        file.write(i)