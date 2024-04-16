from selenium import webdriver
import time
import logging


def test_open_vwo():
    driver = webdriver.Chrome()  # Create a session - POST request
    driver.get("https://app.vwo.com")  # Get request to URL Param
    time.sleep(5)
    print(driver.title)
    assert driver.title == "Login - VWO"
    # print(driver.page_source)
    print(driver.session_id)
