from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
import time
import string
from selenium.webdriver.chrome.options import Options
import random
import threading

# VALUES
threads1 = 5 # Amount of threads
password = "password" # Password for all accounts
email = "@fro.email" # Ending domain (setup wildcard)

def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def run_stuff():

    chromedriver_autoinstaller.install()

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('log-level=3')

    inputs = 0

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://newegg.com/product-shuffle")
    time.sleep(1)
    driver.find_element_by_xpath("//strong[text()='Sign Up']").click()
    inputElement = driver.find_elements_by_xpath("//input")
    for inputEl in inputElement:
        inputs = inputs + 1
        if (inputs == 1):
            inputEl.send_keys(random_generator(5))
        elif (inputs == 2):
            inputEl.send_keys(random_generator(5))
        elif (inputs == 3):
            inputEl.send_keys('newegg' + random_generator(10) + email)
        elif (inputs == 7):
            inputEl.send_keys(password)

    driver.find_element_by_xpath("//button[@class='btn btn-orange']").click()
    
    time.sleep(2)
    cards = driver.find_elements_by_xpath("//div[@class='multiple-choice-card ']")
    for card in cards:
        try:
            card.click()
        except Exception as e:
            print(e)
            continue
    
    try:
        continue1 = driver.find_element_by_xpath("//button[contains(@class,'btn btn-primary')]")
        continue1.click()
    except:
        print("Exception")

    time.sleep(0.5)

    try:
        continue2 = driver.find_element_by_xpath("//button[@class='btn btn-primary']")
        continue2.click()
    except:
        print("Exception")

    time.sleep(1)

    print("Entered Shuffle")

    driver.close()


def start_thread():
    while True:
        run_stuff()

for i in range(threads1):
    threading.Thread(target=start_thread, args=()).start()
