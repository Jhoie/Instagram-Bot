from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager  # backward compatability
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.instagram.com/")

# login
time.sleep(2)
driver.find_element_by_name("username").send_keys("xxxxxx")
driver.find_element_by_name("password").send_keys("xxxxx")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()
time.sleep(2)

# opens a hashtag and clicks a post
driver.get("https://www.instagram.com/explore/tags/greece")
driver.find_element_by_class_name("v1Nh3").click()
time.sleep(2)

# loops through several posts of the same hashtag
i = 0
while i < 5:
    time.sleep(1)
    driver.find_elements_by_class_name("wpO6b")[1].click()
    time.sleep(1.5)
    driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
    i+=1

#driver.close()
