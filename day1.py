from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
username = "mngr298718"
password = "zUqAjut"

driver.get("http://www.demo.guru99.com/V4/")

uname = driver.find_element(By.NAME, "uid")
pwd = driver.find_element(By.NAME, "password")
login =  driver.find_element(By.NAME, "btnLogin")


uname.send_keys(username)
pwd.send_keys(password)
login.click()
WebDriverWait(driver, 700).until(EC.url_to_be("http://www.demo.guru99.com/V4/manager/Managerhomepage.php"))

if(driver.current_url == "http://www.demo.guru99.com/V4/manager/Managerhomepage.php"):
    print("login successful")
    
else:
    print("login failed")

driver.close()


