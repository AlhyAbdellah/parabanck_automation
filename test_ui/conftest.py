from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pytest

@pytest.fixture
def driver():
    options=Options()

    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")  
    options.add_argument("--no-sandbox") 

    driver=webdriver.Chrome(options=options)
    driver.get("https://parabank.parasoft.com/parabank/register.htm")

    yield driver
    time.sleep(5)

    driver.quit()
