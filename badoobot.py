from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  

import pytesseract
try:
    import Image
except ImportError:
    from PIL import Image
from subprocess import check_output

import urllib
import sys
import os
import random
from random import randint
import string
import pyautogui
from time import sleep

import variables

def randomStr(N):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def resolveCaptcha():
    pytesseract.pytesseract.tesseract_cmd = variables.tesseract
    return pytesseract.image_to_string(Image.open(variables.captcha))

def changeRandomPixel():
    originalPic = variables.originalPic
    im = Image.open(originalPic)
    pic = Image.open(originalPic)
    max_x, max_y = pic.size
    pixels = im.load()
    red = randint(1 , 256)
    green = randint(1 , 256)
    blue = randint(1 , 256)
    pixels[randint(1, max_x), randint(1, max_y)] = (red, green, blue, 1)
    im.thumbnail(pic.size)
    im.save(variables.newPic)
    return variables.newPic

def uploadPicture(driver):
    while True:
        try:
            sleep(1)
            changeRandomPixel()
            driver.find_element_by_xpath('//*[@id="simple-page"]/div[2]/section/div[1]/div[2]/div[1]/div/div').click()
            sleep(1)
            pyautogui.write(variables.path + variables.newPic)
            pyautogui.press('enter')
            sleep(1)
            driver.find_element_by_xpath('//*[@id="simple-page"]/div[2]/section/div[1]/div[4]/div').click()
            return True
        except Exception as e:
            print(e, "failed to upload picture. retry")
            continue

def randomPhoneNumber():
    #get random phone number
    return "0612345678"


print(resolveCaptcha())
sleep(30)


phoneNumber = randomPhoneNumber()

driver = webdriver.Chrome(variables.driverpath)
sleep(1)
driver.get("https://badoo.com/signup/")
sleep(2)

#enter signup info
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/section/div/div/div[1]/form/div[1]/div[2]/div/input').send_keys(variables.name)
driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[3]/section/div/div/div[1]/form/div[2]/div[2]/div/div[1]/div/div[1]').send_keys("1")
driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[3]/section/div/div/div[1]/form/div[2]/div[2]/div/div[2]/div/div[1]').send_keys("J")
driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[3]/section/div/div/div[1]/form/div[2]/div[2]/div/div[3]/div/div[1]').send_keys("1")

#select first location
driver.find_element_by_xpath('//*[@id="location_field"]').click()
driver.find_element_by_xpath('//*[@id="data-list-location-list"]/li[1]').click()

#select gender
driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[3]/section/div/div/div[1]/form/div[4]/div[2]/div/label[1]').click()

#enter phone number
driver.find_element_by_xpath('//*[@id="login"]').send_keys(phoneNumber)

#enter random password
password = randomStr(10)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/section/div/div/div[1]/form/div[7]/div[2]/div/input').send_keys(password)

sleep(2)

#accept cookies
driver.find_element_by_xpath('//*[@id="page-cookie-notification"]/div/div/div[2]/div/div[2]/div').click()

#sign up
driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[3]/section/div/div/div[1]/form/div[8]/button').click()

sleep(7.5)

#verify phone number
number = "1234"
i = 2
while i <= 5:
    driver.find_element_by_xpath('//*[@id="simple-page"]/div[3]/div/div/div/section/div/div[3]/div/form/div[1]/div[1]/div/div[' + i + ']/div/input').send_keys(number[i - 2])
    i += 1
sleep(1)

#upload picture
uploadPicture(driver)
sleep(1)

if not check_exists_by_xpath('/html/body/aside/section/div[1]/div/div/section/div/div[2]/div'):
   sys.exit("require foto verification. exit")

#get started
driver.find_element_by_xpath('/html/body/aside/section/div[1]/div/div/section/div/div[2]/div').click()
sleep(0.5)
driver.find_element_by_xpath('//*[@id="page"]/div[1]/main/div[2]/div/div/section/div/div[2]/div/div/div[1]/div[1]').click()
sleep(0.5)
driver.find_element_by_xpath('//*[@id="page"]/div[1]/main/div[2]/div/div/section/div/div[2]/div/div/div[2]/div[1]').click()
sleep(0.5)
driver.find_element_by_xpath('//*[@id="search_form"]/div/div[2]/div/div[1]/div').click()

# like
i = 0
while i <= 50:
    try:
        driver.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]').click()
        i += 1
    except:
        try:
            driver.find_element_by_xpath('/html/body/aside/section/div[1]/div/div[3]/i').click()
            sleep(0.5)
        
        except Exception as e:
            print(e)
            break


#solve captcha
while True:
    try:
        urllib.urlretrieve(driver.find_element_by_xpath('//*[@id="check_code_img"]').get_attribute('src'), "captcha.png")
        driver.find_element_by_xpath('').send_keys(resolveCaptcha())
        driver.find_element_by_xpath('').click()
        if (check_exists_by_xpath('//*[@id="check_code_img"]')):
            continue
        else:
            break
    except:
        continue
        