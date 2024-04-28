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
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")
    driver.maximize_window()
    # time.sleep(10)
    # scrolling
    iframe = driver.find_element(By.TAG_NAME,"iframe")
    actions = ActionChains(driver)
    actions.scroll_to_element(iframe).perform()

    time.sleep(25)