# Actions
import time

from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
def test_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")
    driver.maximize_window()
    time.sleep(10)
    # scrolling
    iframe = driver.find_element(By.TAG_NAME,"iframe")
    scroll_origin = ScrollOrigin.from_element(iframe)
    # Scroll from an element with offset amount,
    actions = ActionChains(driver)
    actions.scroll_from_origin(scroll_origin,0,200).perform()
    time.sleep(15)