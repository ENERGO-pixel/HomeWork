from selenium import webdriver
import time
import os.path
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path=r"C:\Users\sergs\PycharmProjects\Selenium\chromedriver.exe")
try:
     driver.get(url="https://lardi-trans.ua/en/gruz/")
     time.sleep(1)
     button= driver.find_element(By.XPATH,'''//*[@id="react-select-2-input"]''')
     time.sleep(1)
     #country1=input("Enter from country: ")
     button.send_keys("Ukraine")
     button.send_keys(Keys.ENTER)
     time.sleep(2)
     city = driver.find_element(By.XPATH, '''//*[@id="react-select-4-input"]''')
     #city1 = input("Enter from city: ")
     # city.send_keys("Kyiv")
     # time.sleep(2)
     # city.send_keys(Keys.ENTER)
    # time.sleep(2)
     button2 = driver.find_element(By.XPATH, '''//*[@id="react-select-6-input"]''')
     #time.sleep(1)
     #country2 = input("Enter to country: ")
     button2.send_keys("Georgia")
     button2.send_keys(Keys.ENTER)
     time.sleep(2)
     citycity = driver.find_element(By.XPATH, '''//*[@id="react-select-8-input"]''')
     # time.sleep(1)
     #city2 = input("Enter to city: ")
     # citycity.send_keys("Tbilisi")
     # time.sleep(2)
     # citycity.send_keys(Keys.ENTER)
     #time.sleep(2)
     button3 = driver.find_element(By.XPATH, '''//*[@id="proposal-search"]/div/div/div[3]/div[2]/button''')
     button3.click()
     time.sleep(3)
     list=[]
     list1=[]
     count=0
     page= driver.find_elements(By.XPATH,'//*[@id="search-results"]/div/div[3]/div/nav/ul/li[8]/a')
     for i in range(7):
          time.sleep(5)
          veinfo = driver.find_elements(By.XPATH, '''//div[@class="ps_data ps_search-result_data-cargo ps_data-cargo"]/div/span[1]/span''')
          for i in veinfo:
               if i.text:
                    list.append(i.text)
          payment = driver.find_elements(By.XPATH, '''//div[@class="ps_data ps_search-result_data-payment ps_data-payment"]/span[1]''')
          for i in payment:
               if i.text:
                    list1.append(i.text)
          path = os.path.join("baka", "test.txt")
          file = open(path, "w")
          for i,j in zip(list,list1):
               file.write(i+" - "+j+"\n")
          file.close()
          #if i != page:
          baton = driver.find_element(By.XPATH, '''//a[contains(@rel,"next")]''')
          baton.click()
          time.sleep(5)

except Exception as error:
     print(error)


finally:
    driver.close()
    driver.quit()