# Find Helen Benett's Country name

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_webtable():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    driver.maximize_window()
    # Row - //table[contains(@id,'cust')]/tbody/tr
    # Col - //table[contains(@id,'cust')]/tbody/tr[2]/td

    row_elements = driver.find_elements(By.XPATH,"//table[contains(@id,'cust')]/tbody/tr")
    row = len(row_elements)
    print(row)

    col_elements = driver.find_elements(By.XPATH,"//table[contains(@id,'cust')]/tbody/tr[2]/td")
    col = len(col_elements)
    print(col)

    first_part = "//table[contains(@id,'cust')]/tbody/tr["
    second_part = "]/td["
    third_part = "]"

    for i in range(2,row+1):
        for j in range(1,col+1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            data = driver.find_element(By.XPATH,dynamic_path) .text
            if "Helen Bennett" in data:
                country_path = f"{dynamic_path}/following-sibling::td"
                country_text = driver.find_element(By.XPATH,country_path).text
                print(f"Helen Bennett is in {country_text}")