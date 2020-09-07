from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

# user details
username = input("Enter username: ")
password = input("Enter password: ")
hashtag = input("Enter your preferred hashtag: ")  # try two or more hashtags later
number = int(input("Number of likes?: "))

driver = ""


#insta login
def login(name, pasword):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.instagram.com/")

    time.sleep(2)
    driver.find_element_by_name("username").send_keys(name)
    driver.find_element_by_name("password").send_keys(pasword)
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()
    time.sleep(5)


# liking tags
def tag(hashtag, num):
    driver.get("https://www.instagram.com/explore/tags/"+hashtag)
    driver.find_element_by_class_name("v1Nh3").click()
    time.sleep(1)

    i = 0
    while i < num:
        time.sleep(1)
        driver.find_elements_by_class_name("wpO6b")[1].click()
        time.sleep(1.5)
        driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
        i += 1

    time.sleep(5)
    driver.close()


login(username, password)
tag(hashtag, number)


