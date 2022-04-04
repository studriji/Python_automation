import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time
import pandas as pd
#driver = webdriver.Chrome("chromedriver")
#driver.maximize_window()
#table name = 

url = 'https://www.espncricinfo.com/rankings/content/page/211271.html'
r = requests.get(url)
htmlcontent = BeautifulSoup(r.content,'html.parser')

#_________table name________________
title = htmlcontent.find('div', class_ = 'ciPhotoContainer')
title = title.find_all('h3')
#title_list = []
#for i in range(0,len(title)):
#   title_list.append(title[i].text)
#print(title_list)

htmlcontent_table = htmlcontent.find_all('table', class_ = 'StoryengineTable')
#htmlcontent = htmlcontent.find('tbody')

for t in range(0,len(htmlcontent_table)):
    table = htmlcontent_table[t].find_all('tr')
    column_heading = table[0].find_all('th')
    frame = []
    heading = []
    for c in range(0,len(column_heading)):
        heading.append(column_heading[c].text)
    frame.append(heading)
    #print(heading)
    for row in range(1,len(table)):
        column_element = table[row].find_all('td')
        column = []
        for c in range(0,len(column_element)):
            if c == 1:
                column.append(column_element[c].text)
            else:
                column.append(int(column_element[c].text))
        frame.append(column)
        #print(column)
    #print(frame)
    dataframe = pd.DataFrame(frame)
    print(dataframe)
    print(f"{title[t].text}.csv")
    dataframe.to_csv(f'D:\AB projects\webScraping\cricinfo_dataset\{title[t].text}.csv',header=False)
    print('___________###########_________________')

#print(htmlcontent)
#print(len(htmlcontent))
#print(len(table1))
