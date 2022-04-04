#https://finance.yahoo.com/quote/CL%3DF?p=CL%3DF
#https://finance.yahoo.com/quote/GC%3DF?p=GC%3DF
#https://finance.yahoo.com/quote/SI%3DF?p=SI%3DF

import requests
from bs4 import BeautifulSoup
import pandas as pd


#GC = 'GC'
#url = ('https://finance.yahoo.com/quote/') + str(GC) + ('%3DF?p=') + str(GC) +('%3DF')
#print(url)

codes =['GC','CL','SI']
def stockPrice(code):
    url = ('https://finance.yahoo.com/quote/') + str(code) + ('%3DF?p=') + str(code) +('%3DF')
    r = requests.get(url)
    htmlcontent = BeautifulSoup(r.text,'html.parser')
    htmlcontent = htmlcontent.find('div',class_ = 'D(ib) Mend(20px)')
    htmlcontent = htmlcontent.find_all('fin-streamer')
    price = htmlcontent[0].text
    rmc = htmlcontent[1].find('span').text
    rmc_percent = htmlcontent[2].find('span').text
    return price,rmc,rmc_percent


for i in range(1,3):
    for code in codes:
        row = []
        column = []
        row = [f'CODE : {code}']
        p,r,rp = stockPrice(code)
        column = [f'PRICE : {p}',f'REGULAR MARKET CHANGE : {r}',f'PERCENT CHANGE : {rp}']
        row.extend(column)
        dataFrame = pd.DataFrame(row)
        print(row)
    
'''
#url = ('https://finance.yahoo.com/quote/') + str() + ('%3DF?p=') + str(code) +('%3DF')
url = 'https://finance.yahoo.com/quote/GC%3DF?p=GC%3DF'
r = requests.get(url)
htmlcontent = BeautifulSoup(r.text,'html.parser')
htmlcontent = htmlcontent.find('div',class_ = 'D(ib) Mend(20px)')
htmlcontent = htmlcontent.find_all('fin-streamer')
price = htmlcontent[0].text
rmc = htmlcontent[1].find('span').text
rmc_percent = htmlcontent[2].find('span').text


#print(price)
print(price)
print(rmc)
print(rmc_percent)
'''