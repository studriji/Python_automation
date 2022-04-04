from time import time
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib
import time
#https://www.instagram.com/alienbrains__/
#https://www.instagram.com/indiassuperbrain/
name = str(input('enter the account name : '))
time.sleep(2)
driver = webdriver.Chrome('chromedriver')
driver.get('https://www.instagram.com/')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('{put your username}')
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('put your password')
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(2)
driver.get(f"https://www.instagram.com/{name}/?hl=en")
time.sleep(5)

#time.sleep(3)
bodytag = driver.find_element_by_tag_name('body')
page = bodytag.get_attribute('innerHTML')

soup = BeautifulSoup(page,"html.parser")
#print(soup)
image_tag = soup.select(f'img[alt="{name}\'s profile picture"]') #extra forward slash is to overcome the confusion between inverted comma
# for private profile
if not image_tag:
    image_tag = soup.select('.be6sR')#. for class

print(image_tag)
url = image_tag[0]["src"]
urllib.request.urlretrieve(url,"dp_test.jpg")
