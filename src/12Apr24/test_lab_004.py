from selenium import webdriver
import time


def test_open_vwo():
    driver = webdriver.Chrome()  # Create a session - POST request
    driver.get("https://app.vwo.com")  # Get request to URL Param
    time.sleep(5)
