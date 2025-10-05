from os import wait
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# === 1. โหลดข้อมูลจาก Excel ===
file_path = "/Users/hlab/Desktop/Code/SBH Mock up Data For UAT.xlsx"
df = pd.read_excel(file_path, sheet_name="คนไข้")
print(df.columns.tolist())

# === 2. เปิด Browser ===
Login_url = "https://cortex.srbrhospital.com/reception/welcome"
Username = "user1"
Password = "MyPassw0rd"

try:
    driver = webdriver.Chrome()
    driver.get("https://cortex.srbrhospital.com/reception/welcome")
    wait = WebDriverWait(driver, 10)
    # คลิกปุ่ม Login (กรณีมีปุ่มให้กด)
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div/button")))
    login_button.click()

    # Find the username and password input fields and enter the credentials
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    
    username_input.clear()
    username_input.send_keys(Username)
    password_input.clear()
    password_input.send_keys(Password)

    # Find the login/submit button and click it, or press Enter
    # Try to find a submit button first
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    
    # ปุ่มสร้างผู้ป่วยใหม่
    create_patient_btn = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button-label-overflow")))
    create_patient_btn.click()

    time.sleep(5)

    # เลือกเพศจาก dropdown ตามข้อมูลใน Excel
    for index, row in df.iterrows():
        card_input = wait.until(EC.presence_of_element_located((By.NAME, "identifyVerification.identify")))
        card_input.clear()
        card_input.send_keys(str(row['ID']))
        time.sleep(5)

        # ระบุค่าเพศจากข้อมูลใน Excel และเลือกใน dropdown
        gender_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div[3]/div[2]/div[2]/form/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[2]/button")))
        gender_dropdown.click()
        time.sleep(5)  # รอ dropdown แสดงผล


        gender_value = str(row['Gender']).strip()
        gender_select = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div[3]/div[2]/div[2]/form/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[2]/button')))
        gender_select.click()

        select = Select(driver.find_element(By.XPATH, '//*[@id="radix-theme"]/div[1]/div[3]/div[2]/div[2]/form/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[2]/select'))
        if gender_value == "ชาย":
            select.select_by_value("male - ชาย")
        elif gender_value == "หญิง":
            select.select_by_value("female - หญิง")
        
        time.sleep(5)

    

    #password_input.send_keys(Keys.RETURN)
    


except Exception as e:
    print(f"เกิดข้อผิดพลาดระหว่างการทำงานของ Selenium: {e}")
finally:
    # ปิดเบราว์เซอร์เสมอเมื่อเสร็จสิ้น
    print("ปิดเบราว์เซอร์")
    driver.quit()