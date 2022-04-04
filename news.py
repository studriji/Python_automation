from selenium import webdriver
import time
driver = webdriver.Chrome("chromedriver")


driver.get("https://news.google.com/search?pz=1&cf=all&hl=en-IN&q=topic:kolkata&gl=IN&ceid=IN:en")
time.sleep(5)
driver.maximize_window()
time.sleep(10)
#top stories
driver.find_element_by_xpath('/html/body/div[4]/header/div[4]/div[2]/div/c-wiz/div/div[1]/a/div[2]/span').click()
time.sleep(5)
#extract top 5 stories
#/html/body/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/div[3]/div/div/article/h3/a
#/html/body/c-wiz[2]/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/div[3]/div/div/article/h3/a
#/html/body/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/div[4]/div/div/article/h3/a
#//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/div[3]/div/div/article/h3/a
#/html/body/c-wiz/div/ ....by parts....div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/div[3]/div/div/article/h3/a
#                       c-wiz changing evertytime so using class name
#//div[@class='T4LgNb']/div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/div[3]/div/div/article/h3/a

for i in range(3,8):
    headline = driver.find_element_by_xpath(f"//div[@class='T4LgNb']/div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/div[{i}]/div/div/article/h3/a").text
    s = i-2
    print(s,' ',headline,'\n')
    print('\n')
    
time.sleep(2)
story_no = int(input('enter story number '))
story_no=story_no+2
print(story_no)
time.sleep(8)
driver.find_element_by_xpath(f"//div[@class='T4LgNb']/div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/div[{story_no}]/div/div/article").click()

'''
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys('google news kolkata')
time.sleep(3)
search_button = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]').click()

'''