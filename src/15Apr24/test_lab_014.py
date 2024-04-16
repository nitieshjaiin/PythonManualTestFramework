from selenium import webdriver
import time
import logging
from selenium.webdriver.common.by import By


def test_open_vwo():
    driver = webdriver.Chrome()  # Create a session - POST request
    driver.get("https://app.vwo.com/#/login")  # Get request to URL Param
    # 1 - you can find by id, name, classname , tagname, linktext, partial linktext (Easy)
    # 2 - CSS Selector and xPath (Sureshot way to find the element in html)
    driver.maximize_window()
    email_element = driver.find_element(By.NAME,"username")
    email_element.send_keys("admin")
    pwd_element = driver.find_element(By.ID, "login-password")
    pwd_element.send_keys("admin")
    button_element = driver.find_element(By.ID,"js-login-btn")
    button_element.click()
    time.sleep(15)
    error_msg_element = driver.find_element(By.ID,"js-notification-box-msg")
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"
    driver.quit()