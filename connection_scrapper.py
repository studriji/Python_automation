from operator import index
import pandas as pd
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from user import Userdict
# specifies the path to the chromedriver.exe
driver = webdriver.Chrome("chromedriver")
# driver.get method() will navigate to a page given by the URL address
driver.get("https://www.linkedin.com/login")

# locate email form by_id
username = driver.find_element_by_id("username")

#send_keys() to simulate key strokes
username.send_keys(Userdict['email'])

#locate password form id
password = driver.find_element_by_id("password")

# send_keys() to simulate key strokes
password.send_keys(Userdict['pass'])
# locate submit button by_class_name
log_in_button = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')

# .click() to mimic button click
log_in_button.click()
time.sleep(3)
driver.get('https://www.linkedin.com/in/rijit-chakraborty-565a781b6/')
time.sleep(5)

#click connection
driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/ul/li/a').click()
time.sleep(5)

#number of pages
driver.execute_script("window.scrollTo(0, 900)")
time.sleep(2)
pages = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[2]/div/div[1]/main/div/div/div[3]/div/div/ul/li[5]/button/span').text
pages = int(pages)
print(pages)
href_list = []
# pages xpath
#next      /html/body/div[6]/div[3]/div/div[2]/div/div[1]/main/div/div/div[3]/div/div/button[2]/span
#next      /html/body/div[6]/div[3]/div/div[2]/div/div[1]/main/div/div/div/div[2]/div/button[2]/span
#next //div[@class='artdeco-pagination artdeco-pagination--has-controls ember-view pv5 ph2']/button[2]/span
# 2 = /html/body/div[5]/div[3]/div/div[2]/div/div[1]/main/div/div/div[3]/div/div/ul/li[2]/button/span
# 3 = /html/body/div[5]/div[3]/div/div[2]/div/div[1]/main/div/div/div[3]/div/div/ul/li[3]/button/span
#   
k = 0  
for j in range(1,pages+1):
    for i in range(1,11):
        #extract the profile link
        try:
            href=driver.find_element_by_xpath(f'//*[@id="main"]/div/div/div[1]/ul/li[{i}]/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a')
        except:
            break
        href_link = href.get_attribute('href')
        href_list.append(href_link)
        length = len(href_list)
                         
    print(len(href_list))
    time.sleep(2)
    #clicking next pages
    try:
        driver.find_element_by_xpath("//div[@class='artdeco-pagination artdeco-pagination--has-controls ember-view pv5 ph2']/button[2]/span").click()
        time.sleep(3) 
    except:
        break
    driver.execute_script("window.scrollTo(0, 900)")
    time.sleep(2)
    #details
print(href_list)
time.sleep(3)

frame = []
details_list = ['NAME','PROFILE LINK','CURRENT COMPANY','EMAIL']
for link in href_list:
    driver.get(link)
    #time.sleep(2)
                                        
    time.sleep(5)
    #click contact info
    #
    #//*[@id="top-card-text-details-contact-info"]
    #//*[@id="top-card-text-details-contact-info"]
    driver.find_element_by_xpath('//*[@id="top-card-text-details-contact-info"]').click()
    time.sleep(5)
    #name /html/body/div[3]/div/div/div[1]/h1
    #name /html/body/div[3]/div/div/div[1]/h1
    name = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/h1').text
    #//div[@class='pv-profile-section__section-info section-info']/section/div/a
    profile_link = driver.find_element_by_xpath("//div[@class='pv-profile-section__section-info section-info']/section/div/a").text
    try:
        #//*[@id="ember457"]/div/section[1]/div/a
        #/html/body/div[3]/div/div/div[2]/section/div/div/div/section[1]/div/a 
        #/html/body/div[3]/div/div/div[2]/section/div/div/div/section[1]/div/a
        
        
        #//*[@id="ember457"]/div/section[2]/div/a
        # //a             
        # //section[@class='pv-contact-info__contact-type ci-email']/div/a                              
        email = driver.find_element_by_xpath("//section[@class='pv-contact-info__contact-type ci-email']/div/a").text
    except Exception as e:
        email = None
        print(e)
        #break
        #profile_link = 'not available'
        
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[3]/div/div/button').click()
    time.sleep(3)
    #driver.execute_script("window.scrollTo(0, 1080)")
    # /html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[4]/div[3]/ul/li[1]/div/div[2]/div[1]/a/div/span/span[1]
    # /html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[5]/div[3]/ul/li[1]/div/div[2]/div/div[1]/div/span/span[1]
    try:
        company = driver.find_element_by_xpath("//div[@aria-label='Current company']").text
    except:
        company = None                                    
                                            
    details_list = [name,profile_link,company,email]
    frame.append(details_list)
    print(details_list)

df = pd.DataFrame(frame)
df.to_csv(f'D:\AB projects\webScraping\connection_dataset\connection.csv',header=False,index = False)
print('dataset created')


'''
    details_list = []
    name = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/h1').text
                                        
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[2]/span[2]/a').click()
    time.sleep(5)
    try:
        profile_link = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/section/div/div/div/section[1]/div/a').text
                                                    
        email = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/section/div/div/div/section[3]/div/a').text
    except:
        profile_link = 'not available'
        email = 'not available'
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[3]/div/div/button').click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 1080)")
    company = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[5]/div[3]/ul/li[1]/div/div[2]/div/div[1]/div/span/span[1]').text
                                            
    details_list = [name,profile_link,company,email]
    print(details_list)
    driver.back()
    driver.back()
    driver.back()'''