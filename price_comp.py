from selenium import webdriver
import time
driver = webdriver.Chrome("chromedriver")
#driver.maximize_window()

item_name = 'oneplus 6'

driver.get("https://www.google.com/")
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(item_name)
time.sleep(3)
search_button = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]').click()
#time.sleep(3)
driver.execute_script("window.scrollTo(0, 700)")
time.sleep(15)
comp_price = driver.find_element_by_xpath('/html/body/div[7]/div/div[10]/div[2]/div/div/div[2]/div/div[3]/div/div/div/div/div[1]/div/div/div/div/div/div[3]/div/div[1]/div[1]/div[1]/div[2]/button').click()

time.sleep(10)
#sort_storage = driver.find_element_by_xpath('/html/body/div[14]/div/div[2]/div/div[1]/div[1]/div/g-dropdown-menu').click()
#storage_value = driver.find_element_by_xpath('/html/body/div[7]/div/div[6]/div/g-menu/g-menu-item[3]/div/div/span').text

# website = /html/body/div[14]/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[1]/span
# price = /html/body/div[14]/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[4]/span
# storage = 
for i in range(1,11):
    website = driver.find_element_by_xpath(f'/html/body/div[14]/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr[{i}]/td[1]/span').text
    price = driver.find_element_by_xpath(f'/html/body/div[14]/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr[{i}]/td[4]/span').text
    storage = driver.find_element_by_xpath(f'/html/body/div[14]/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr[{i}]/td[2]').text
    if str(storage) == '64 GB':
        print(website,price,'  ',storage,'\n')
    