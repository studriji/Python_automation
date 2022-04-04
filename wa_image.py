from selenium import webdriver
import time 
import schedule

#D://AB projects//Automation//demo.jpeg

#schedule library in python
def greeting():

    name = input('Enter the name of user or group : ')
    filepath = input('Enter your filepath (images/video): ')

    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')
    time.sleep(5)
    input('Enter anything after scanning QR code')
    time.sleep(7)
    account_name = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    account_name.click()
    time.sleep(3)
    attachment = driver.find_element_by_xpath('//div[@title = "Attach"]')
    attachment.click()

    image = driver.find_element_by_xpath(
        '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image.send_keys(filepath)

    time.sleep(20)

    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[2]/div[2]/div/div/span').click()
    #//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[2]/div[2]/div/div/span
    time.sleep(20)
    

schedule.every().day.at('16:32').do(greeting)

while True:
    schedule.run_pending()


