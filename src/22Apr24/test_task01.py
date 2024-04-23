from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import allure


@pytest.mark.smoke
@allure.title("Verify that an error message is displayed on Code Display when username is blank")
@allure.description("TC #1 - Simple test to validate error message when username is blank")
def test_task1():
    drive = webdriver.Chrome()
    drive.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
    drive.maximize_window()
    drive.switch_to.frame(drive.find_element(By.ID, "result"))
    email_element = drive.find_element(By.XPATH, "//input[@id='email']")
    email_element.send_keys("test@gmail.com")
    pwd_element = drive.find_element(By.XPATH,"//input[@id='password']")
    pwd_element.send_keys("123456")
    cnf_pwd_element = drive.find_element(By.XPATH, "//input[@id='password2']")
    cnf_pwd_element.send_keys("123456")
    submit_button = drive.find_element(By.XPATH,"//button[text()='Submit']")
    submit_button.click()
    time.sleep(2)
    msg_element = drive.find_element(By.XPATH,"//input[@id='username']/following::small")
    assert msg_element.text == "Username must be at least 3 characters"
    allure.attach(drive.get_screenshot_as_png(), name="Error Screenshot", attachment_type=AttachmentType.PNG)
