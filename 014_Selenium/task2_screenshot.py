from selenium import webdriver
import time
import os.path
import json
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path=r"C:\Users\sergs\PycharmProjects\Selenium\chromedriver.exe")
try:
     driver.get(url="https://www.marvel.com/characters")
     time.sleep(1)
     list1=[]
     elements2=driver.find_elements(By.XPATH,'''//*[@id="filter_grid-7"]/div/div[3]/div[2]/div[@class="mvl-card mvl-card--explore"]/a''')
     for i in elements2:
            list1.append(i.get_attribute("href"))
     for i in range(len(list1)):
         driver.get(list1[i])
         driver.get_screenshot_as_file(f"{i}.png")

except:
    print("error")

finally:
    driver.close()
    driver.quit()