from selenium import webdriver
import time
import os.path
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path=r"C:\Users\sergs\PycharmProjects\Selenium\chromedriver.exe")
try:
     driver.get(url="https://mystat.itstep.org/en/main/schedule/page/index")
     time.sleep(1)
     elements = driver.find_elements(By.CLASS_NAME,'active-day')
     list=[]
     list1=[]
     for i in elements:
         if i.text:
             print(i.text)
     login = driver.find_element(By.CSS_SELECTOR, '#username')
     login.send_keys("Sara_0dbw")
     password = driver.find_element(By.CSS_SELECTOR, '#password')
     password.send_keys("DEath2206")
     button = driver.find_element(By.CLASS_NAME,'login-action')
     button.click()
     time.sleep(5)
     days = driver.find_elements(By.CLASS_NAME,'active-day')
     list = []
     list1=[]
     for i in days:
          i.click()
          time.sleep(1)
          button4 = driver.find_element(By.XPATH, '''/html/body/modal-container/div/div/div/div[1]/button/span''')
          button4.click()
          info = driver.find_elements(By.CLASS_NAME,'on-hover')
          for i in info:
               if i.text:
                    print(i.text+"\n")

except Exception as error:
    print(error)

finally:
    driver.close()
    driver.quit()