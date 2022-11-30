from selenium import webdriver
import time
import os.path
import json
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path=r"C:\Users\sergs\PycharmProjects\Selenium\chromedriver.exe")
try:
     driver.get(url="https://www.marvel.com")
     time.sleep(1)
     name = driver.title
     print(name)
     elements =driver.find_elements(By.CLASS_NAME,"card-body__unlinked")
     findmarvel = driver.find_elements(By.CLASS_NAME,"card-body__headline")
     path = os.path.join("baka", "test.txt")
     file=open(path,"w")
     list=[]
     list1=[]
     for i in elements:
         if i.text:
           list.append(i.text)
     for j in findmarvel:
         if j.text:
            list1.append(j.text)
     for i,j in zip(list,list1):
         file.write(i+" - "+j+"\n")
     file.close()


except:
    print("error")

finally:
    driver.close()
    driver.quit()