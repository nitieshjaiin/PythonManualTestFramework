# Fluent wait
import allure
from allure_commons.types import AttachmentType
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
    email_element.send_keys("0347pdwksq@ezztt.com")
    pwd_element = driver.find_element(By.ID, "login-password")
    pwd_element.send_keys("0347pdwksq@Ezztt.com")
    button_element = driver.find_element(By.ID, "js-login-btn")
    button_element.click()
    # wait with condition and frequency is called fluent wait
    # fluent wait is a type of explicit wait
    # example - until the error message is seen on the DOM in every 2 secs
    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1, ignored_exceptions=ignore_list)
    wait.until(
        # EC.text_to_be_present_in_element((By.CSS_SELECTOR,".page-heading"),"Dashboard")
        EC.presence_of_element_located((By.CSS_SELECTOR, ".page-heading"))
    )
    heading_element = driver.find_element(By.XPATH, "//span[@data-qa='lufexuloga']")
    assert heading_element.text == "asd asd"
    allure.attach(driver.get_screenshot_as_png(), name="Dashboard", attachment_type=AttachmentType.PNG)
    driver.quit()
