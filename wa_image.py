from selenium import webdriver
from time import sleep

name = input('Enter the name of user or group : ')
filepath = input('Enter your filepath (images/video): ')
#D://AB projects//Automation//demo.jpeg

#schedule library in python
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
sleep(5)
input('Enter anything after scanning QR code')
sleep(5)
account_name = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
account_name.click()
sleep(3)
attachment = driver.find_element_by_xpath('//div[@title = "Attach"]')
attachment.click()

image = driver.find_element_by_xpath(
    '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image.send_keys(filepath)

sleep(3)

driver.find_element_by_xpath('//span[@data-icon="send"]').click()

