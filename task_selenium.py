from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import random

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome("/home/yamato/Documents/chromdriver/chromedriver", options=chrome_options)


def playTrailer():
    
    ## Synopsis
    text = driver.find_element(By.CLASS_NAME,"title-info-synopsis").text
    print("Description: ",text,"\n")

    ## Casts
    cast = driver.find_elements(By.CLASS_NAME,"item-cast")
    for i in cast:
        print(i.text)
    print("\n")

    #Trailer Play
    trailer = driver.find_element(By.CLASS_NAME,"additional-video-title")
    trailer.click()
    print("The trailer being played is:", trailer.text)
    time.sleep(5)
    seekTime()

def seekTime():
    #Proof that trailer is being played(Seeks the time of the trailer)
    a = ActionChains(driver)
    WebDriverWait(driver, 10).until(lambda x: x.find_element(By.CLASS_NAME,"VideoContainer").is_displayed())
    m = driver.find_element(By.CLASS_NAME,"VideoContainer")
    a.move_to_element(m).click().perform()
    WebDriverWait(driver, 10).until(lambda x: x.find_element(By.CLASS_NAME,'scrubber-head').is_displayed())
    while True:
        scurb = driver.find_element_by_class_name('scrubber-head').get_attribute('aria-valuetext').split(" ")
        print("seek time: ", scurb)
        time.sleep(1)
    
  

def goToTrailerPage():

    ### Hitting up the netflix base url
    driver.get("https://www.netflix.com/in/")
    
    ### Location to the browse menu for netflix
    watchList = "/html/body/div[1]/div/div/div/div/div/div[3]/div[1]/div[2]/ul/li[15]/a/span"
    
    ### Location to the Stranger things main page
    trailerPage = "/html/body/div[1]/div/div[2]/main/section[{l}]/div/ul/li[2]/a/img".format(l = random.randint(2, 10))

    ### Browse page
    driver.find_element(By.XPATH,watchList).click()

    ### Trailer page
    driver.find_element(By.XPATH,trailerPage).click()
    return
    

if __name__ == "__main__":

    goToTrailerPage()
    playTrailer()
    