from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import allure


@pytest.mark.smoke
@allure.title("Print the title and price from ebay website")
@allure.description("TC #1 - Simple test to print title and price from ebay website when 16gb is searched and find "
                    "cheapest item from list")
def test_task1():
    drive = webdriver.Chrome()
    drive.get("https://www.ebay.com/")
    drive.maximize_window()
    # drive.switch_to.frame(drive.find_element(By.ID, "result"))
    search_element = drive.find_element(By.ID, "gh-ac")
    search_element.send_keys("16gb")
    button_element = drive.find_element(By.ID,"gh-btn")
    button_element.click()
    time.sleep(10)
    allure.attach(drive.get_screenshot_as_png(), name="Search Results", attachment_type=AttachmentType.PNG)
    list_of_elements = drive.find_elements(By.XPATH,"//span[@role='heading']")
    for product in list_of_elements:
        product_name = product.text
        print("Name of the product: " + product_name)

    product_price_list = drive.find_elements(By.XPATH,"//span[@class='s-item__price']")
    price_list = []
    for price in product_price_list:
        product_price = price.text
        print(product_price)
        x = product_price.replace("$"," ").strip()
        price_list.append(x)

    price_list.sort()
    print("Cheapest price is", price_list[1])
    time.sleep(10)

    # cnf_pwd_element = drive.find_element(By.XPATH, "//input[@id='password2']")
    # cnf_pwd_element.send_keys("123456")
    # submit_button = drive.find_element(By.XPATH,"//button[text()='Submit']")
    # submit_button.click()
    # time.sleep(2)
    # msg_element = drive.find_element(By.XPATH,"//input[@id='username']/following::small")
    # assert msg_element.text == "Username must be at least 3 characters"
