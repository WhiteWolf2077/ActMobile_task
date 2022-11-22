from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/home/yamato/Documents/chromdriver/chromedriver')


### Hitting up the netflix base url
driver.get("https://www.netflix.com/in/")

### Location to the browse menu for netflix
watchList = "/html/body/div[1]/div/div/div/div/div/div[3]/div[1]/div[2]/ul/li[15]/a/span"

### Location to the Stranger things main page
stranger_things = "/html/body/div[1]/div/div[2]/main/section[2]/div/ul/li[2]/a/img"

### Location to the play trailer button
#play_trailer = "/html/body/div[1]/div/div[2]/section[3]/div[2]/ul/li[1]/div/button/span[2]"

### Browse page
driver.find_element_by_xpath(watchList).click()

### Stranger things page
driver.find_element_by_xpath(stranger_things).click()


### Gets the Synopsis
text = driver.find_element_by_class_name("title-info-synopsis").text


print("Description: ",text,"\n")

### Get the list of casts
print("StarCast:\n")
cast = driver.find_elements_by_class_name("item-cast")
for i in cast:
    print(i.text)

print("\n")


### Playing the trailer
try:
    trailer = driver.find_element_by_class_name("additional-video-title")
    trailer.click()
    print("The trailer being played is:", trailer.text)
except:
    print ("An error occured")


#driver.close()
