from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import random
import time
import json
import os

class register():
    def __init__(self,driver):
        self.driver=driver
        self.wait= WebDriverWait(driver,10)
        #Locators Register
        self.first_nam=(By.ID,"customer.firstName")
        self.last_nam=(By.ID,"customer.lastName")
        self.address=(By.ID,"customer.address.street")
        self.city=(By.ID,"customer.address.city")
        self.state=(By.ID,"customer.address.state")
        self.zip_code=(By.ID,"customer.address.zipCode")
        self.phone=(By.ID,"customer.phoneNumber")
        self.snn=(By.ID,"customer.ssn")
        self.user_nam=(By.ID,"customer.username")
        self.password=(By.ID,"customer.password")
        self.confirm=(By.ID,"repeatedPassword")
        self.button_register=(By.XPATH,"//input[@value='Register']")

    def wait_send(self,locator,value):
        element=self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)
    
    def append_json(self, nom_fichier, new_data):
        if not os.path.exists(nom_fichier):

            with open(nom_fichier, "w") as f:

                json.dump([new_data], f, indent=4)
        else:

            with open(nom_fichier, "r") as f:

                try:
                    data=json.load(f)
                except json.JSONDecodeError:
                    
                    data = []

        # ✅ S'assurer que data est une liste
            if not isinstance(data, list):
                data = [data]

            data.append(new_data)

            with open(nom_fichier, "w") as f:
                json.dump(data, f, indent=4)


    def full_info(self):

        fake=Faker()
        #generation dataset
        first=fake.first_name()[:20]
        last=fake.last_name()[:20]
        add=f"{random.randint(1,20)} rue M7"
        cit=fake.city()[:6]
        sts=fake.state()[:10]
        zipc=random.randint(10000,99999)
        phon=f"06{random.randint(12345678,989796959)}"
        sn=random.randint(12345678,989796959)
        user=f"alyaTest{random.randint(1000,9999)}"
        keyword="test@123"

        #Upload dataset generated
        self.wait_send(self.first_nam,first)
        self.wait_send(self.last_nam,last)
        self.wait_send(self.address,add)
        self.wait_send(self.city,cit)
        self.wait_send(self.state,sts)
        self.wait_send(self.zip_code,zipc)
        self.wait_send(self.phone,phon)
        self.wait_send(self.snn,sn)
        self.wait_send(self.user_nam,user)
        self.wait_send(self.password,keyword)
        self.wait_send(self.confirm,keyword)

        self.append_json("users.json",{"username": user,"password":keyword,"first":first,"last":last,"address":add,"city":cit})

    def safe_click(self):
        button=self.wait.until(EC.element_to_be_clickable(self.button_register))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.driver.execute_script("arguments[0].click();",button)
    
    def register_check(self):
        msg = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Welcome')]"))
        )
        self.driver.save_screenshot("screenshot.png")
        assert "Welcome" in msg.text,"Register failed"
        print("Rigister passed.")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Transfer Funds")))

