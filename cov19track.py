import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time

driver = webdriver.Chrome("D:\\AB projects\\webScraping\\chromedriver.exe")
#driver.maximize_window()

search = 'TN'

driver.get(f"https://www.covid19india.org/state/{search}")
time.sleep(20)
htmlcontent = driver.find_element_by_class_name('Level')
htmlcontent = htmlcontent.get_attribute('innerHTML')
htmlcontent = BeautifulSoup(htmlcontent,'html.parser')
htmlcontent = htmlcontent.find_all('div')
print("state : ",search)
for i in range(0,4):
    column = []
    category_html = htmlcontent[i]
    category = category_html.find('h5').text
    h4 = category_html.find('h4').text
    h1 = category_html.find('h1').text
    column = [f'category : {category}',f'Increase/Decrease : {h4}',f'Total Count : {h1}']
    print(column)


#print(len(htmlcontent))