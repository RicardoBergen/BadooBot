from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  

import sys
import os
import random
from random import randint
import string
import pyautogui
from time import sleep
from PIL import Image

import variables

class DabooBot():

    def randomStr(N):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

    def check_exists_by_xpath(xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def changeRandomPixel():
        originalPic = variables.originalPic
        im = Image.open(originalPic)
        pic = Image.open(originalPic)
        max_x, max_y = pic.size
        pixels = im.load()
        x = random.randrange(max_x)
        y = random.randrange(max_y)
        red = randint(1 , 256)
        green = randint(1 , 256)
        blue = randint(1 , 256) 
        pixels[randint(1, max_x), randint(1, max_y)] = (red, green, blue, 1)
        im.thumbnail(pic.size)
        im.save(variables.newPic)
        return variables.newPic

    driver = webdriver.Chrome(variables.driverpath)
    sleep(1)
    driver.get("https://badoo.com/signup/")
    sleep(2)

    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/section/div/div/div[1]/form/div[1]/div[2]/div/input').send_keys(variables.name)
    driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[3]/section/div/div/div[1]/form/div[2]/div[2]/div/div[1]/div/div[1]').send_keys("1")
    driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[3]/section/div/div/div[1]/form/div[2]/div[2]/div/div[2]/div/div[1]').send_keys("J")
    driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[3]/section/div/div/div[1]/form/div[2]/div[2]/div/div[3]/div/div[1]').send_keys("1")
    
    driver.find_element_by_xpath('//*[@id="location_field"]').click()
    driver.find_element_by_xpath('//*[@id="data-list-location-list"]/li[1]').click()

    driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[3]/section/div/div/div[1]/form/div[4]/div[2]/div/label[1]').click()

    driver.find_element_by_xpath('//*[@id="login"]').send_keys(variables.phoneNumber)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/section/div/div/div[1]/form/div[7]/div[2]/div/input').send_keys(randomStr(10))
    
    sleep(2)
    
    driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[3]/section/div/div/div[1]/form/div[8]/button').click()

    sleep(2)
    
