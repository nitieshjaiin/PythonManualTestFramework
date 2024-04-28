# Dynamic Table

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_webtable():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")
    driver.maximize_window()
    table = driver.find_element(By.XPATH,"//table[@summary='Sample Table']/tbody")
    row_table = table.find_elements(By.TAG_NAME,"tr")

    for row in row_table:
        cols = row.find_elements(By.TAG_NAME,"td")
        for value in cols:
            print(value.text)
            print(end=" ")


