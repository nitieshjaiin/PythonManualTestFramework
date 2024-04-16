from selenium import webdriver


def test_open_vwo():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
