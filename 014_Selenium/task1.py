from selenium import webdriver
import time
import os.path
import json
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path=r"C:\Users\sergs\PycharmProjects\Selenium\chromedriver.exe")
try:
     driver.get(url="https://www.marvel.com")
     time.sleep(1)
     #driver.refresh()
     #driver.get_screenshot_as_file("screen1.png")
     #driver.save_screenshot("second.png")
     name = driver.title
     print(name)
     #element=driver.find_element(By.CLASS_NAME,"promo__title")
     #print(element.text)
     elements =driver.find_elements(By.CLASS_NAME,"card-body__headline")
     list=[]
     for i in elements:
         if i.text !='':
            list.append(i.text)
     print(list)
     path = os.path.join("baka", "hello.json")
     file = open(path, "a")
     json.dump(list, file)
     file.close()
     findmarvel = driver.find_elements(By.CLASS_NAME, "card-body__unlinked")
     list1 = []
     for i in findmarvel:
         if i.text != '':
             list1.append(i.text)
     print(list1)
     file = open(path, "a")
     json.dump(list1, file)
     file.close()

except:
    print("error")

finally:
    driver.close()
    driver.quit()