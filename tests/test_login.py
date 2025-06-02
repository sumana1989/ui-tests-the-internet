from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_login_success():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element("id", "username").send_keys("tomsmith")
    driver.find_element("id", "password").send_keys("SuperSecretPassword!")
    driver.find_element("css selector", "button.radius").click()
    assert "You logged into a secure area!" in driver.page_source
    driver.quit()
