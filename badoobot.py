from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import sys
import random
import os
# import pyautoguis

import variabelen

from time import sleep
class BadooBot():
    driver = webdriver.Chrome(variabelen.driverpath)
    sleep(1)
    driver.get("https://badoo.com")

    sleep(1)

    gender = driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[3]/div/div[3]/div/div[2]/div/div[1]/div[1]/div[1]')
    gender.click()

    sleep(1)
    name = driver.find_element_by_xpath('//*[@id="first_name1598866574780"]')
    name.send_keys(variabelen.name)

    day = driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[3]/div/div[3]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/div[1]/div/div[1]')
    day.send_keys(variabelen.day)

    month = driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[3]/div/div[3]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/div[2]/div/div[1]')
    month.send_keys(variabelen.month)

    year = driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[3]/div/div[3]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/div[3]/div/div[1]')
    year.send_keys(variabelen.year)

    city = driver.find_element_by_xpath('//*[@id="location_field"]')
    city.send_keys(variabelen.city)

    telefoon = driver.find_element_by_xpath('//*[@id="login"]')
    telefoon.send_keys(variabelen.telefoon)

    password = driver.find_element_by_xpath('//*[@id="password1598866351042"]')
    password.send_keys(variabelen.password)
    # while True:
    #     like = driver.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]')
    #     like.click()
    #     try:
    #         op = driver.find_element_by_xpath('/html/body/aside/section/div[1]/div/div[2]/i')
    #         op.click()