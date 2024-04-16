from selenium import webdriver
import time
import logging
from selenium.webdriver.common.by import By


def test_open_vwo():
    driver = webdriver.Chrome()  # Create a session - POST request
    driver.get("https://katalon-demo-cura.herokuapp.com/")  # Get request to URL Param
    # we should interact with the HTML elements
    # locators
    # Find the element i.e. anchor tag button and click on it.
    # 1 - you can find by id, classname, name, tagname, linktext, partial linktext (Easy)
    # 2 - CSS Selector and xPath (Sureshot way to find the element in html)
    element = driver.find_element(By.ID,"btn-make-appointment")
    element.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(25)
    driver.quit()