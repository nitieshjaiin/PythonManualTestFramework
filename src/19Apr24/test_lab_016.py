from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_cura_katalon():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    # make_apt_element = driver.find_element(By.LINK_TEXT, "Make Appointment")
    # make_apt_element.click()
    # By. Link Text works with only a "anchor" tag
    # It will perform full/exact match with the text
    # If 2 elements with same name exists, it will return the first
    # If there's no link text, it will not be able to find the element.

    # Partial text - this also works with a "anchor" tag
    # This will match with partial text given
    # Make
    # App
    # oint
    # check for contains keyword
    # it will find the first unique element

    make_apt_element = driver.find_element(By.PARTIAL_LINK_TEXT, "oint")
    make_apt_element.click()

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    print(driver.current_url)
    username_element = driver.find_element(By.ID, "txt-username")
    username_element.send_keys("John Doe")
    pwd_element = driver.find_element(By.ID, "txt-password")
    pwd_element.send_keys("ThisIsNotAPassword")
    login_element = driver.find_element(By.ID, "btn-login")
    login_element.click()
    verify_apt = driver.find_element(By.CLASS_NAME, "col-sm-12")
    assert verify_apt.text == "Make Appointment"
    time.sleep(20)
