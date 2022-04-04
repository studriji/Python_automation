from selenium import webdriver
import time
print("Login now...\n")

name = input("Enter name:")

message = input("Message: ")
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

input('press y if scanning done')

time.sleep(5)
account_name = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)).click()
time.sleep(5)
textBox = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')

textBox.send_keys(message)
sendButton = driver.find_element_by_xpath('//span[@data-icon="send"]')
sendButton.click()


print("Message Sent")
