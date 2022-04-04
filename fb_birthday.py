from user import Userdict
from selenium import webdriver
import time
from bs4 import BeautifulSoup
# specifies the path to the chromedriver.exe
driver = webdriver.Chrome("chromedriver")
# driver.get method() will navigate to a page given by the URL address
driver.get("https://www.facebook.com")

# locate email form by_id
username = driver.find_element_by_id("email")#m_login_email

#send_keys() to simulate key strokes
username.send_keys(Userdict['email'])

#locate password form id
password = driver.find_element_by_id("pass")#"m_login_password")

# send_keys() to simulate key strokes
password.send_keys(Userdict['pass'])
# locate submit button by_class_name
log_in_button = driver.find_element_by_name('login')

# .click() to mimic button click
log_in_button.click()
time.sleep(10)

driver.get('https://www.facebook.com/events/birthdays')
driver.implicitly_wait(10)

#_____________birthday list___________________

#//*[@id="mount_0_0_Su"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div[2]/div/form/div/div/div[1]
# //*[@id="mount_0_0_Su"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/div/form/div/div/div[1]
#//*[@id="mount_0_0_xw"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div[2]/div/form/div/div/div[1]
#/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div[2]/div/form/div/div/div[1]
#/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/div/form/div/div/div[1]
#/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div[2]/div/form/div/div/div[1]/div/div/div[2]/div/div/div/div
k=1
while True:
    try:
        birthday = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[{k}]/div/div/div/div[2]/div/div/div[2]/div[2]/div/form/div/div/div[1]/div/div/div[2]/div/div/div/div')
        birthday.send_keys("happy birthday")
        k=k+1
    except Exception as e:
        print(e)
        print(k-1)
        break
    