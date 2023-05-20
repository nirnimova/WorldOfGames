# coding=UTF8

from selenium import webdriver
from selenium.webdriver.common.by import By

# 1
chrome_driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')


def main_function():
    chrome_driver.get('https://www.walla.co.il')


main_function()

