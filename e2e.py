# coding=UTF8

import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1
chrome_driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
print(os.environ['PATH'])


def main_function():
    chrome_driver.get('https://www.walla.co.il')


main_function()

