from selenium import webdriver
import time
import logging


def test_open_vwo():
    driver = webdriver.Chrome()  # Create a session - POST request
    # Session is created with unique ID - 16 digit ID
    # A fresh copy of browser is created
    # You can open new tabs, URLs, and those will be different from normal browser
    # The moment you close the browser, everything is deleted.

    driver.get("https://app.vwo.com")  # Get request to URL Param
    time.sleep(5)
    print(driver.title)
    assert driver.title == "Login - VWO"
    # print(driver.page_source)
    print(driver.session_id)
    time.sleep(10)
    driver.close()
    time.sleep(20)
    # Close will only close the current window of browser or tab.
    # Session ID will not be null (Invalid)
    # It will not close the other tabs
