from selenium import webdriver
import time
import logging


def test_open_vwo():
    driver = webdriver.Chrome()  # Create a session - POST request
    driver.get("https://bing.com/")  # Get request to URL Param
    time.sleep(25) # Python interpreter will wait for 25 seconds and not the webdriver.
    driver.get("https://google.com")
    print(driver.title)
