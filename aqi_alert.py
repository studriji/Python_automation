from selenium import webdriver
import time
import smtplib
driver = webdriver.Chrome("chromedriver")
#driver.maximize_window()

item_name = 'aqi kolkata'

# aqi = //*[@id="_k2Q4YuyUDuaSseMPrbWosAo56"]/div/div[2]/div[2]/span[5]/span[1]
# aqi = //*[@id="_k2Q4YuyUDuaSseMPrbWosAo58"]/div/div[2]/div[2]/span[5]/span[1]
#       //*[@id="_k2Q4YuyUDuaSseMPrbWosAo72"]/div/div[2]/div[2]/span[5]/span[1]
#       //*[@id="_k2Q4YuyUDuaSseMPrbWosAo66"]/div/div[2]/div[2]/span[5]/span[1]
#//*[@id="_k2Q4YuyUDuaSseMPrbWosAo62"]/div/div[2]/div[2]/span[5]/span[1]

#/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/block-component/div/div[1]/div/div/div/div[1]/div/div/div/div/div[6]/g-accordion/div/div/g-accordion-expander[1]/div[1]/div/div[2]/div[2]/span[5]/span[1]
#/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/block-component/div/div[1]/div/div/div/div[1]/div/div/div/div/div[6]/g-accordion/div/div/g-accordion-expander[2]/div[1]/div/div[2]/div[2]/span[5]/span[1]
#/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/block-component/div/div[1]/div/div/div/div[1]/div/div/div/div/div[6]/g-accordion/div/div/g-accordion-expander[3]/div[1]/div/div[2]/div[2]/span[5]/span[1]

driver.get("https://www.google.com/")
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(item_name)
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]').click()
time.sleep(3)
#scroll
driver.execute_script("window.scrollTo(0, 300)")
time.sleep(3)
'''
for i in range(1,4):
    aqi_list = driver.find_element_by_xpath(f'/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/block-component/div/div[1]/div/div/div/div[1]/div/div/div/div/div[6]/g-accordion/div/div/g-accordion-expander[{i}]/div[1]/div/div[2]/div[2]/span[5]/span[1]')
    aqi = aqi_list.text
    print(aqi,'\n')
    '''
#more options
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/block-component/div/div[1]/div/div/div/div[1]/div/div/div/div/div[6]/g-accordion/div/g-expandable-container/div/g-inline-expansion-bar/div[1]/span').click()
time.sleep(3)

driver.execute_script("window.scrollTo(0, 600)")
time.sleep(3)

#/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/block-component/div/div[1]/div/div/div/div[1]/div/div/div/div/div[6]/g-accordion/div/g-expandable-container/div/g-expandable-content/span/div/g-accordion-expander[1]/div[1]/div/div[2]/div[2]/span[5]/span[1]
#/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/block-component/div/div[1]/div/div/div/div[1]/div/div/div/div/div[6]/g-accordion/div/g-expandable-container/div/g-expandable-content/span/div/g-accordion-expander[2]/div[1]/div/div[2]/div[2]/span[5]/span[1]
#/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/block-component/div/div[1]/div/div/div/div[1]/div/div/div/div/div[6]/g-accordion/div/g-expandable-container/div/g-expandable-content/span/div/g-accordion-expander[5]/div[1]/div/div[2]/div[2]/span[5]/span[1]

def sendEmail(places):
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("demoautoab@gmail.com","automation*123")
    msg = ''
    for p in places:
        msg = msg + str(p) + ' ; '
    message = f"alert at {msg} !! high AQI value"
    server.sendmail("demoautoab@gmail.com","studrijit@gmail.com",message)

places = []
def alert(aqi,place):
    if int(aqi) > 95:
        places.append(place)
        time.sleep(2)
        return '  alert !!'
    else:
        return " "
    

flag = True
for i in range(1,4):
    aqi_list = driver.find_element_by_xpath(f'/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/block-component/div/div[1]/div/div/div/div[1]/div/div/div/div/div[6]/g-accordion/div/div/g-accordion-expander[{i}]/div[1]/div/div[2]/div[2]/span[5]/span[1]')
    place_list = driver.find_element_by_xpath(f'/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/block-component/div/div[1]/div/div/div/div[1]/div/div/div/div/div[6]/g-accordion/div/div/g-accordion-expander[{i}]/div[1]/div/div[2]/div[1]')
    aqi = aqi_list.text
    place = place_list.text
    if str(aqi) != 'Currently unavailable':
        print(place,': ',aqi,alert(aqi=aqi,place=place))
    else:
        print(place,': ',aqi)
    print('\n')
    time.sleep(2)
k=1
while flag:
    try:
        aqi_list = driver.find_element_by_xpath(f'/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/block-component/div/div[1]/div/div/div/div[1]/div/div/div/div/div[6]/g-accordion/div/g-expandable-container/div/g-expandable-content/span/div/g-accordion-expander[{k}]/div[1]/div/div[2]/div[2]/span[5]/span[1]')
        place_list = driver.find_element_by_xpath(f'/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/block-component/div/div[1]/div/div/div/div[1]/div/div/div/div/div[6]/g-accordion/div/g-expandable-container/div/g-expandable-content/span/div/g-accordion-expander[{k}]/div[1]/div/div[2]/div[1]')
        #                                           /html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/block-component/div/div[1]/div/div/div/div[1]/div/div/div/div/div[6]/g-accordion/div/g-expandable-container/div/g-expandable-content/span/div/g-accordion-expander[1]/div[1]/div/div[2]/div[1]
        aqi = aqi_list.text
        place = place_list.text
        k = k+1
        if str(aqi) != 'Currently unavailable':
            print(place,': ',aqi,alert(aqi=aqi,place=place))
        else:
            print(place,': ',aqi)
        print('\n')
        time.sleep(2)
    except Exception as e:
        print(e) 
        print("done")
        break


sendEmail(places)
#aqilist = /html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/block-component/div/div[1]/div/div/div/div[1]/div/div/div/div/div[6]/g-accordion/div/g-expandable-container/div/g-expandable-content/span/div/g-accordion-expander[5]/div[1]/div/div[2]/div[2]/span[5]/span[1]
#          /html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/block-component/div/div[1]/div/div/div/div[1]/div/div/div/div/div[6]/g-accordion/div/g-expandable-container/div/g-expandable-content/span/div/g-accordion-expander[1]/div[1]/div/div[2]/div[2]/span[5]/span[1]
# place = /html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/block-component/div/div[1]/div/div/div/div[1]/div/div/div/div/div[6]/g-accordion/div/div/g-accordion-expander[1]/div[1]/div/div[2]/div[1]   
#         