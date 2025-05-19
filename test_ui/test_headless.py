from selenium import webdriver
from test_ui.page_register import register
from test_ui.page_paiement import paiement
from test_ui.conftest import driver
import time
from selenium.webdriver.chrome.options import Options
import pytest

# @pytest.fixture
# def driver():

#     options=Options()
#     options.add_argument("--headless")
#     options.add_argument("--disable-gpu")
#     options.add_argument("--window-size=1920,1080")  
#     options.add_argument("--no-sandbox") 

#     driver=webdriver.Chrome(options=options)
#     driver.get("https://parabank.parasoft.com/parabank/register.htm")

#     yield driver
#     time.sleep(5)

#     driver.quit()

def test_register(driver):
    reg=register(driver)
    reg.full_info()
    reg.safe_click()
    reg.register_check()

def test_paiement(driver):
    pay=paiement(driver)
    pay.transfert_funds()
    print("🕒 Waiting for page to be ready before clicking 'Transfer Funds'")
    time.sleep(5)
    pay.check_transfert()






