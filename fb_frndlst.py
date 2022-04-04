from user import Userdict
from selenium import webdriver
import time
from bs4 import BeautifulSoup
# specifies the path to the chromedriver.exe
driver = webdriver.Chrome("chromedriver")
# driver.get method() will navigate to a page given by the URL address
driver.get("https://m.facebook.com")

# locate email form by_id
username = driver.find_element_by_id("m_login_email")#m_login_email

#send_keys() to simulate key strokes
username.send_keys(Userdict['email'])

#locate password form id
password = driver.find_element_by_id("m_login_password")#"m_login_password")

# send_keys() to simulate key strokes
password.send_keys(Userdict['pass'])
# locate submit button by_class_name
log_in_button = driver.find_element_by_name('login')

# .click() to mimic button click
log_in_button.click()
time.sleep(10)

driver.get("https://m.facebook.com/profile.php?id=100007107527159&v=friends&lst=100002880697214%3A100007107527159%3A1648670495")
time.sleep(6)
'''
bodytag = driver.find_element_by_tag_name('body')
page = bodytag.get_attribute('innerHTML')
soup = BeautifulSoup(page,"html.parser")
'''
'''
unwanted = ['','Marketplace0','Watch9+','See Friend Lists','News Feed0','Main Menu0','SearchSearch0','Notifications0',
            'Try Again','Profile0', 'Unfriend','\xa0','FRIEND REQUESTS0','Messages1', 'Clear']
friends = set()
#anchors = soup.find_all('a')
#print(anchors)
serial = 0
for i in range(0,3):
    i=i+1
    if i>2:
        break 
    try:
        bodytag = driver.find_element_by_tag_name('body')
        page = bodytag.get_attribute('innerHTML')
        soup = BeautifulSoup(page,"html.parser")
        for i in soup.find_all('a'):
            if serial > 13 and i.text.lower() != 'add friend' and i.text.lower() != 'cancel' and i.text.lower() != 'mark as spam':
                friends.add(i.text)
                print(i.text)
            #if i.text.lower() == 'try again':
                #break
            serial+=1
        driver.execute_script("window.scrollTo(0, 600)")
        time.sleep(3)
      
    except:
        break

print('done')
print(friends)
friend_list = list(friends)
for f in friend_list:
    if f in unwanted:
        friend_list.remove(f)
    

print(friend_list)'''

#prev_height = driver.execute_script('return document.body.scrollHeight')
'''while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(1)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == prev_height:
        break
'''
time.sleep(5)
#        /html/body/div[1]/div/div[4]/div/div[1]/div[2]/div[1]/div[2]/div/div[1]/h3/a
#name = /html/body/div[1]/div/div[4]/div/div[1]/div[2]/div[24]/div[2]/div/div[1]/h3/a
#       /html/body/div[1]/div/div[4]/div/div[1]/div[3]/div[1]/div[2]/div/div[1]/h1/a
#       /html/body/div[1]/div/div[4]/div/div/div[4]/div[1]/div[2]/div/div[1]/h1/a
#       /html/body/div[1]/div/div[4]/div/div/div[5]/div[1]/div[2]/div/div[1]/h1/a
name_list = []
k=1
while True:
    time.sleep(1)
    try:
        name = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[4]/div/div[1]/div[2]/div[{k}]/div[2]/div/div[1]/h3/a').text
        print(name)
        name_list.append(name)
        k= k+1
    except:
        print('done')
        break

l = 2
while True:
    time.sleep(2)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    l=l+1
    
    time.sleep(4)
    try: 
        if l < 4: 
            k=1 
            while True:
                
                time.sleep(1)
                try:
                    name = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[4]/div/div[1]/div[3]/div[{k}]/div[2]/div/div[1]/h1/a').text
                    print(name)                           
                    name_list.append(name)
                    k= k+1
                except:
                    print('done')
                    break
        else :
             k=1
             while True:
                
                time.sleep(1)
                try:
                    name = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[4]/div/div/div[{l}]/div[{k}]/div[2]/div/div[1]/h1/a').text
                    print(name)
                    name_list.append(name)
                    k= k+1
                except:
                    print('done')
                    break

    except :
        print('total done')
        break
#bodytag = []
#bodytag = driver.find_elements_by_class_name('_55wo _55x2')
#print(len(bodytag))
#page = bodytag.get_attribute('innerHTML')
#soup = BeautifulSoup(page,"html.parser")
#soup = soup.find_all('a')
#print(soup)
print(len(name_list))