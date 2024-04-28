# Actions
import time

from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
def test_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    driver.maximize_window()
    # create object of action chains class
    clickable = driver.find_element(By.ID,"clickable")
    actions = ActionChains(driver)
    actions.double_click(clickable).perform()
    time.sleep(20)
