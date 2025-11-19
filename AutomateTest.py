#Author: Melika Malmasi
#Date: Nov 13 2025
# -------------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
# In this test case I wrote an automation that test the functionality of Apply Now form
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # the website is called:
    driver.get("https://marketing.on.sutton.institute/programme-view-buggy/31659545-f6b4-48aa-963b-0d5e432240d2")

    # we focus on the form:
    apply_section = driver.find_element(By.ID, "registerRequest")
    driver.execute_script("arguments[0].scrollIntoView();", apply_section)

    # put some variable on inputs:
    fname = (driver.find_element(By.NAME, "FirstName"))
    fname.send_keys("first name")
    lname = (driver.find_element(By.NAME, "LastName"))
    lname.send_keys("last name")
    email = driver.find_element(By.NAME, "Email")
    email.send_keys("example@gmail.com")

    # accept the Privacy Policy checkBox in here:
    checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    driver.execute_script("arguments[0].click();", checkbox)

    # and at last click the submit button:
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    driver.execute_script("arguments[0].click();", submit_button)

    print("Form submitted successfully!")

# we could see the errors whatever against the case happened:
except Exception as e:
    print(f"Error occurred: {e}")

# coming out of the website & close it:
finally:
    driver.quit()