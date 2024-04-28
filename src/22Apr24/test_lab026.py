# Actions
import time

from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()
    first_name = driver.find_element(By.NAME,"firstname")

    # create object of action chains class
    actions = ActionChains(driver)
    # send keys but with the shift
    (actions.key_down(Keys.SHIFT). # Pressing shift key
     send_keys_to_element(first_name,"nitish jain")
     .key_up(Keys.SHIFT).perform()) # Releasing shift key
    url = driver.find_element(By.XPATH,"//a[text()='Click here to Download File']")
    actions.context_click(url).perform()
    time.sleep(20)
