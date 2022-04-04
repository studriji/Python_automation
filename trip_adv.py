from selenium import webdriver
import time

source = str(input('Enter source city'))
destination = str(input('Enter destination city'))
driver = webdriver.Chrome("chromedriver")

driver.get('https://www.google.com/')
flight = f'{source} to {destination} flight'
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(flight)
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]').click()
time.sleep(5)

#flight details
# company = /html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[5]/div/div/a[1]/span[1]
#           /html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[5]/div/div/a[2]/span[1]         
# fare = /html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[5]/div/div/a[1]/span[4]/span
for i in range(1,5):
    company = driver.find_element_by_xpath(f'/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[5]/div/div/a[{i}]/span[1]').text
    fare = driver.find_element_by_xpath(f'/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[5]/div/div/a[{i}]/span[4]/span').text
    print('\n')
    print(company,' : ',fare) 
    time.sleep(1)
time.sleep(5)

#______top 10 tourist place in destination____________
driver.get('https://www.google.com/')
time.sleep(5)
tour_search = f'{destination} tourist places'
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(tour_search)
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]').click()
time.sleep(5)
# more to do
driver.execute_script("window.scrollTo(0, 300)")
driver.find_element_by_xpath("//div[@class='ULSxyf']//div/div/div/div/div[4]/a/g-more-link/div").click()
#                              /html/body/div[7]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[4]/a/g-more-link/div
#                             /html/body/div[7]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[1] ,,,by parts....   /div/div/div/div/div[4]/a/g-more-link/div
#                                                                         /div[@class='ULSxyf']//div/div/div/div/div[4]/a/g-more-link/div
time.sleep(5)
# spots1 = /html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[2]/c-wiz/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div
# spots2 = /html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[2]/c-wiz/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div
#   see all top sights      
driver.find_element_by_xpath('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[2]/c-wiz/div/div[2]/div[3]/div/div/button/span').click()
time.sleep(5)
driver.execute_script("window.scrollTo(0, 300)")
time.sleep(5)
for i in range(1,11):
    tour_spot = driver.find_element_by_xpath(f'/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[2]/c-wiz/div/div/div/div[2]/div[{i}]/div/div/div[1]/div[2]/div[1]/div')
    spots = tour_spot.text
    print(spots)
    time.sleep(2)


time.sleep(10)

#__________________hotels________
time.sleep(5)
driver.get(f'https://www.google.com/travel/hotels?q={destination}')
time.sleep(10)
#price = //*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[1]/c-wiz/div/div/div/div[1]/div/div[2]/div[1]/div/a/div/div/div/span[1]/span/span[1]
#price2 = //*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]...  ...../c-wiz[2]/c-wiz/div/div/div/div[1]/div/div[2]/div[1]/div/a/div/div/div/span[1]/span/span[1]
# pricelast=//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[17]/c-wiz/div/div/div/div[1]/div/div[2]/div[1]/div/a/div/div/div/span[1]/span/span[1]
# pricenxt = //*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[1]/c-wiz/div/div/div/div[1]/div/div[2]/div[1]/div/a/div/div/div/span[1]/span/span[1]
#pricenxtlas //*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[14]/c-wiz/div/div/div/div[1]/div/div[2]/div[1]/div/a/div/div/div/span[1]/span/span[1]
#//div[@class='l5cSPd']/c-wiz[i]/c-wiz/div/div/div/div[1]/div/div[2]/div[1]/div/a/div/div/div/span[1]/span/span[1]
#//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]/c-wiz[7]/c-wiz/div/div/div/div[1]/div/div[2]/div[1]/div/a/div/div/div/div[1]/span[2]/span/span[1]/span
#hotel name = //*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div[1]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[6]......./c-wiz[1]/c-wiz/div/div/div/div[1]/div/div[1]/div[1]/div[1]/h2
# //div[@class='l5cSPd']/c-wiz[i]/c-wiz/div/div/div/div[1]/div/div[1]/div[1]/div[1]/h2
for i in range(1,15):
    try:
        price_list = driver.find_element_by_xpath(f"//div[@class='l5cSPd']/c-wiz[{i}]/c-wiz/div/div/div/div[1]/div/div[2]/div[1]/div/a/div/div/div/span[1]/span/span[1]")
        hotel_list = driver.find_element_by_xpath(f"//div[@class='l5cSPd']/c-wiz[{i}]/c-wiz/div/div/div/div[1]/div/div[1]/div[1]/div[1]/h2")
        hotel = hotel_list.text
        price = price_list.text
        price = price[1:]
        price = price.replace(',','')
        price = int(price)
        #print(price)
        time.sleep(3)
        if price < 4000:
           print(hotel,' : ',price)
    except:
        continue
driver.quit()