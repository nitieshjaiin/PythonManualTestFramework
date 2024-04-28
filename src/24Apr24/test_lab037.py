# Fluent wait

from selenium import webdriver
import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException)


def test_open_vwo():
    driver = webdriver.Chrome()  # Create a session - POST request
    driver.get("https://app.vwo.com/#/login")  # Get request to URL Param
    driver.maximize_window()
    email_element = driver.find_element(By.NAME, "username")
    email_element.send_keys("admin")
    pwd_element = driver.find_element(By.ID, "login-password")
    pwd_element.send_keys("admin")
    button_element = driver.find_element(By.ID, "js-login-btn")
    button_element.click()
    # wait with condition and frequency is called fluent wait
    # fluent wait is a type of explicit wait
    # example - until the error message is seen on the DOM in every 2 secs
    ignore_list = [ElementNotVisibleException,ElementNotSelectableException]
    wait = WebDriverWait(driver=driver,timeout=5,poll_frequency=1,ignored_exceptions= ignore_list)
    wait.until(
        EC.text_to_be_present_in_element((By.ID,"js-notification-box-msg"),
                                         "Your email, password, IP address or location did not match")
    )
    error_msg_element = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"
    driver.quit()
