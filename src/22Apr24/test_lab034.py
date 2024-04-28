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
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()
    time.sleep(10)
    main_window_handle = driver.current_window_handle
    print(main_window_handle)
    link = driver.find_element(By.LINK_TEXT,"Click Here")
    link.click()
    windows_handles = driver.window_handles
    print(windows_handles)
    for handles in windows_handles:
        driver.switch_to.window(handles)
        if "New Window" in driver.page_source:
            print("Found the Text")
            break
    driver.switch_to.window(main_window_handle)
    time.sleep(10)