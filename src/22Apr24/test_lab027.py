# Actions
import time

from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    driver.maximize_window()
    # create object of action chains class
    clickable = driver.find_element(By.ID,"click")
    actions = ActionChains(driver)
    # Click is a nornmal click
    actions.click(clickable).perform()

    # Click and hold will click but will not release
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    driver.maximize_window()
    clickable = driver.find_element(By.ID, "click")
    actions = ActionChains(driver)
    actions.click_and_hold(clickable).perform()
    time.sleep(20)
