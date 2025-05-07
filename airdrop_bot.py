from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def login_galxe_and_complete_task():
    chrome_options = Options()

    # Your Chrome profile path
    chrome_options.add_argument("user-data-dir=C:/Users/HP PROBOOK X360 G4/AppData/Local/Google/Chrome/User Data")
    chrome_options.add_argument("profile-directory=Profile 2")

    driver = webdriver.Chrome(service=Service(), options=chrome_options)

    driver.get("https://galxe.com/quest/Liqfinity/GCAKotmYfH")  # Replace with a real campaign
    time.sleep(10)

    try:
        complete_button = driver.find_element(By.XPATH, "//button[contains(text(),'Complete')]")
        complete_button.click()
        print("✅ Task clicked!")
    except:
        print("⚠️ Task button not found.")

    time.sleep(10)
    driver.quit()

# Run the bot
login_galxe_and_complete_task()
