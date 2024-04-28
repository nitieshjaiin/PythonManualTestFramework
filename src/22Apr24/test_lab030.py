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
    # hover
    hover_item = driver.find_element(By.ID,"hover")
    actions = ActionChains(driver)
    actions.move_to_element(hover_item).perform()
    time.sleep(20)
