from selenium import webdriver
import time
import logging


def test_open_vwo():
    Logger = logging.getLogger(__name__)
    driver = webdriver.Chrome()  # Create a session - POST request
    driver.get("https://app.vwo.com")  # Get request to URL Param
    time.sleep(5)
    print(driver.title)
    Logger.info(driver.title)
    assert driver.title == "Login - VWO"

