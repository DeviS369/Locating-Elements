from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time ,os
from dotenv import load_dotenv
# Automatically install and configure ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
time.sleep(5)
try:
    url = os.environ.get('url')
    user = os.environ.get('phone_user')
    pwd = os.environ.get('pwd')
    driver.get(url)
    
    # Allow time for page to load
    time.sleep(5)  # Adjust based on internet speed
    sign_in = driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[2]/p/a/span')
    sign_in.click()
    time.sleep(5)
    phone_user = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div/div[1]/div/label/input')
    phone_user.send_keys(user)
    time.sleep(1)
    pwd1 = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div/div[2]/div/label/input')
    pwd1.send_keys(pwd)
    sub = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div/div[3]/button/div')
    sub.click()
    time.sleep(5)
    not_save = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div')
    not_save.click()
    time.sleep(5)
    driver.get(url)
    time.sleep(4)
    
    # Step 2: Use XPATH to locate followers and following
    followers_xpath = "//a[contains(@href,'/followers')]/span"
    following_xpath = "//a[contains(@href,'/following')]/span"

    # Extract the values
    followers = driver.find_element(By.XPATH, followers_xpath).get_attribute("title")  # For formatted numbers
    following = driver.find_element(By.XPATH, following_xpath).text

    # Step 3: Print the results
    print(f"Followers: {followers}")
    print(f"Following: {following}")

finally:
    # Close the browser
    driver.quit()
