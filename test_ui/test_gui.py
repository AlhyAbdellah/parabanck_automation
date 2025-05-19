from selenium import webdriver
from test_ui.page_paiement import paiement
from test_ui.page_register import register
import pytest
import time


#setup
driver=webdriver.Chrome()
driver.get("https://parabank.parasoft.com/parabank/register.htm")

#register
reg=register(driver)
reg.full_info()
reg.safe_click()
reg.register_check()


#paiement
pay=paiement(driver)
pay.transfert_funds()
pay.check_transfert()

time.sleep(5)
driver.quit()