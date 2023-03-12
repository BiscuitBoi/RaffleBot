from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r"/usr/local/bin/chromedriver")

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

#To be done
def readDoc():
    with open('emailList.txt', 'r') as f:
        emails = [row.rstrip('\n') for row in f]
        print(emails)

def login():
    time.sleep(3)
    print("hi")
    driver.get('https://www.tiktok.com/login/')

    email = 'OwningBiscuit235@gmail.com'
    password = 'Q0LsdC90plXb!'

    #Select login
    wait_until_visible(xpath='//*[@id="loginContainer"]/div/div/a[2]/div')
    time.sleep(3)
    driver.find_element(by=By.XPATH, value='//*[@id="loginContainer"]/div/div/a[2]/div').click()

    #Select with email
    wait_until_visible(xpath='//*[@id="loginContainer"]/div[1]/form/div[2]/a')
    time.sleep(3)
    driver.find_element(by=By.XPATH, value='//*[@id="loginContainer"]/div[1]/form/div[2]/a').click()
    print("done")

    #Insert email
    email_input = driver.find_element(by=By.XPATH, value='//*[@id="loginContainer"]/div[1]/form/div[1]/input')
    email_input.clear()
    time.sleep(3)
    email_input.send_keys(email)

    #Insert password
    password_input = driver.find_element(by=By.XPATH, value='//*[@id="loginContainer"]/div[1]/form/div[2]/div/input')
    password_input.clear()
    time.sleep(3)
    password_input.send_keys(password)

    #Click Submit
    driver.find_element(by=By.XPATH, value='//*[@id="loginContainer"]/div[1]/form/button').click()
    time.sleep(30)
    print("done login")



#Wait until element loads in
def wait_until_visible(xpath=None,duration=10000, frequency=0.01):
        WebDriverWait(driver, duration, frequency).until(EC.visibility_of_element_located((By.XPATH, xpath)))


login()














# def login():
#     time.sleep(3)
#     print("hi")
#     driver.get('https://www.nike.com/gb/member/profile/login?continueUrl=https://www.nike.com/gb/')
#
#     email = 'matwro224@gmail.com'
#     password = 'Q0LsdC90plXb'
#
#
#     wait_until_visible(xpath='//*[@id="gen-nav-commerce-header-v2"]/div[1]/div/div[1]/div/div[2]/div[2]/button')
#     time.sleep(3)
#     driver.find_element(by=By.XPATH, value='//*[@id="gen-nav-commerce-header-v2"]/div[1]/div/div[1]/div/div[2]/div[2]/button').click()
#     wait_until_visible(xpath="//input[@name='emailAddress']")
#     time.sleep(3)
#     print("done")
#     email_input = driver.find_element(by=By.XPATH, value="//input[@name='emailAddress']")
#     time.sleep(3)
#     email_input.clear()
#     email_input.send_keys(email)
#
#     password_input = driver.find_element(by=By.XPATH, value="//input[@name='password']")
#     time.sleep(3)
#     password_input.clear()
#     time.sleep(3)
#     password_input.send_keys(password)
#     time.sleep(5)
#     driver.find_element(by=By.XPATH, value="//input[@value='SIGN IN']").click()
