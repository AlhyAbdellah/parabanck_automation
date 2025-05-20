from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import json

class paiement():
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
        self.transfer_fund=(By.LINK_TEXT,"Transfer Funds")
        self.amout=(By.ID,"amount")
        self.from_acout=(By.ID,"fromAccountId")
        self.to_accout=(By.ID,"toAccountId")
        self.trensfer=(By.XPATH,"//input[@value='Transfer']")
    
    def transfert_funds(self):

        print("✅ Current page:", self.driver.current_url)
        print("✅ Trying to click 'Transfer Funds'...")
        link = self.wait.until(EC.presence_of_element_located(self.transfer_fund))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", link)
        self.driver.execute_script("arguments[0].click();", link)
        

        fake_amout=str(random.randint(1,2000))
        self.wait.until(EC.visibility_of_element_located(self.amout)).send_keys(fake_amout)
        print(f"Input Ammout : {fake_amout}")

        transfert_button=self.wait.until(EC.element_to_be_clickable(self.trensfer))
        self.driver.execute_script("arguments[0].scrollIntoView(true);",transfert_button)
        self.driver.execute_script("arguments[0].click();",transfert_button)
    
    def check_transfert(self):
        try:
            confirmation = self.wait.until(EC.presence_of_element_located((By.XPATH,"//h1[@class='title'and contains(text(),'Transfer Complete!')]")))
            self.driver.save_screenshot("screenshot.png")
            assert "Transfer Complete!" in confirmation.text 
            print("Transfert succed")
        except Exception:
            print("Transfert failed")