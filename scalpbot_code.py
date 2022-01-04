from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import random
    """
    1. load and create all website objects from database_scalpy and text file 
    2. open driver windows for each website data obj, possibly using a class file that can manage all driver windows or assign as a new class variable for a website obj 
    3. run through queue of xpath elements or sen_key or url links, or any other necessary elements
    4. run process on loop for each obj, once done ask user again for reloop, and have mothods for adding or removing website objects
    """
driver = webdriver.Chrome()
driver.implicitly_wait(5)

url = "https://www.walmart.com/ip/Refurbished-Apple-iPad-Pro-12-9-4th-Gen-128GB-Silver-Wi-Fi-MY2J2LL-A-Latest-Model/242925018"
driver.get(url)

driver.maximize_window()
time.sleep(2)

addToCart = driver.find_element_by_xpath('//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]/button/span')
addToCart.click()
time.sleep(1)

checkOut = driver.find_element_by_xpath('//*[@id="cart-root-container-content-skip"]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/button[1]')
checkOut.click()
time.sleep(1)

continueWithoutAcc = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[1]/div/section/section/div/button')
continueWithoutAcc.click()
time.sleep(1)

continueButton = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/div[2]/button')
continueButton.click()
time.sleep(2)

firstName = driver.find_element_by_xpath('//*[@id="firstName"]')
firstName.send_keys("Engkanchanith")
time.sleep(1)

lastName = driver.find_element_by_xpath('//*[@id="lastName"]')
lastName.send_keys("Tan")
time.sleep(1)

phone = driver.find_element_by_xpath('//*[@id="phone"]')
phone.send_keys("7142048324")
time.sleep(1)

address = driver.find_element_by_xpath('//*[@id="addressLineOne"]')
address.send_keys("1013 W Alton Ave")
time.sleep(1)

email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys("t.kanchanith@gmail.com")
time.sleep(1)

city = driver.find_element_by_xpath('//*[@id="city"]')
city.clear()
city.send_keys("Santa Ana")
time.sleep(1)

zipcode = driver.find_element_by_xpath('//*[@id="postalCode"]')
zipcode.clear()
zipcode.send_keys("92707")
time.sleep(1)

state = driver.find_element_by_xpath('//*[@id="state"]')
Select(state).select_by_value("CA")
time.sleep(1)

continueButton2 = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[2]/div[2]/button')
continueButton2.click()