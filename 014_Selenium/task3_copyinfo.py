from selenium import webdriver
import time
import os.path
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path=r"C:\Users\sergs\PycharmProjects\Selenium\chromedriver.exe")
try:
     driver.get(url="https://www.marvel.com/characters")
     time.sleep(1)
     count=0
     list = []
     list1 = []
     list2 = []
     list4 = []
     while count!=5:
         elements = driver.find_elements(By.XPATH,'''//*[@id="filter_grid-7"]/div/div[3]/div[2]/div[@class="mvl-card mvl-card--explore"]/a/div[2]/p''')
         for i in elements:
             if i.text:
                 list4.append(i.text)
         elements2 = driver.find_elements(By.XPATH,'''//*[@id="filter_grid-7"]/div/div[3]/div[2]/div[@class="mvl-card mvl-card--explore"]/a''')
         for i in elements2:
             list.append(i.get_attribute("href"))
         button = driver.find_element(By.XPATH,'''//*[@id="filter_grid-7"]/div/div[3]/div[3]/nav/ul/li[@class="pagination__item pagination__item-nav pagination__item-nav-next"]''')
         button.click()
         time.sleep(5)
         count += 1
     for i in range(len(list)):
         driver.get(list[i])
         univers = driver.find_elements(By.XPATH,'''//*[@id="two_column-4"]/div/div[3]/div[1]/div[2]/div[2]/div/ul[@class="railBioInfo"]/li/p''')
         univers2 = driver.find_elements(By.XPATH,'''//*[@id="two_column-4"]/div/div[3]/div[1]/div[2]/div[2]/div/ul[@class="railBioInfo"]/li/ul/li''')
         path = os.path.join("baka", "test.txt")
         file = open(path, "a")
         file.write("\n" + list4[i] + " - " + list[i] + "\n")
         for l, n in zip(univers, univers2):
             file.write(l.text + " - " + n.text + "\n")
         file.close()

except:
    print("error")

finally:
    driver.close()
    driver.quit()