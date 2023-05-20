# coding=UTF8

import sys
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_scores_service(url):
    chrome_driver = webdriver.Chrome(executable_path='chromedriver.exe')
    chrome_driver.get(url)
    score = chrome_driver.find_element(By.ID, "score").text
    if 1 <= int(score) <= 50:
        return True
    else:
        return False


def main_function():
    if test_scores_service('http://localhost:8777/'):
        sys.exit(0)
    else:
        sys.exit(1)


main_function()

