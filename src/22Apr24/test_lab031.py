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
    # drag and drop
    draggable = driver.find_element(By.ID,"draggable")
    droppable = driver.find_element(By.ID,"droppable")
    actions = ActionChains(driver)
    actions.drag_and_drop(draggable,droppable).perform()
    time.sleep(25)