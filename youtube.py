from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver")

#url = 'https://www.youtube.com/c/CleverProgrammer'
driver.get('https://www.youtube.com/c/CleverProgrammer/videos')
#response = requests.get(url)
#print(response.text)

#htmlcontent = response.content
#soup = BeautifulSoup(htmlcontent,'html.parser')
#print(soup.prettify())
#paralist = []
#paralist = soup.find_all('div')
#print(paralist)
'''time.sleep(10)
bodytag = driver.find_element_by_tag_name('body')
page = bodytag.get_attribute('innerHTML')
soup2 = BeautifulSoup(page,"html.parser")
try:
    for i in soup2.find_all('p'):
            print(i.text)
except:
    print('error')
    '''

subs = driver.find_element_by_id('subscriber-count').text
print(subs)

#__________views on latest vids_______________
#//*[@id="metadata-line"]/span[1]
#//*[@id="metadata-line"]/span[1]
#/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[1]/div[1]/div[1]/div[1]/div/div[1]/div[2]/span[1]
#/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[1]/div[1]/div[1]/div[1]/div/div[1]/div[2]/span[1]
#/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/........ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/span[1]
#vidname =/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/..........ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[1]/div[1]/div[1]/div[1]/h3/a

try:
    print('views on latest videos')
    for i in range(1,6):
        views = driver.find_element_by_xpath(f"//ytd-browse[@role='main']/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[{i}]/div[1]/div[1]/div[1]/div/div[1]/div[2]/span[1]").text
        vidname = driver.find_element_by_xpath(f"//ytd-browse[@role='main']/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[{i}]/div[1]/div[1]/div[1]/h3/a").text
        print(vidname,' : ',views)
except :
    print("error")

#__________About section_______
time.sleep(5)
driver.find_element_by_xpath('//*[@id="tabsContent"]/tp-yt-paper-tab[6]/div').click()
time.sleep(3)
total_views = driver.find_element_by_xpath('//*[@id="right-column"]/yt-formatted-string[3]').text
print('total views on channel : ',total_views)
time.sleep(2)
duration = driver.find_element_by_xpath('//*[@id="right-column"]/yt-formatted-string[2]/span[2]').text
dur = int(duration[-4:])
dur_span = (2022-dur)
if dur_span>1:
    print('Duration : ',dur_span,' years')
else:
    print("less than 1 year")

try:
    about_the_channel = driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-about-metadata-renderer/div[1]/div[1]/yt-formatted-string[2]').text
    print('Description : ',about_the_channel)
except Exception as e:
    print(e)

location = driver.find_element_by_xpath('//*[@id="details-container"]/table/tbody/tr[2]/td[2]/yt-formatted-string').text
print("Location : ",location)

#   social
#//*[@id="link-list-container"]/a[1]/yt-formatted-string
#//*[@id="link-list-container"]/a[2]/yt-formatted-string

names = driver.find_elements_by_xpath('//*[@id="link-list-container"]/a/yt-formatted-string')
links = driver.find_elements_by_xpath('//*[@id="link-list-container"]/a')
l = len(names)

for i in range(0,l):
    print(names[i].text)
    print(links[i].get_attribute('href'))
    print('\n')
    
#print(links)
driver.quit()