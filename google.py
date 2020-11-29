import time
import urllib
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

b = webdriver.Chrome()
url = "https://www.google.com"
b.get(url)

search = b.find_element_by_xpath(
    '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')

search.send_keys("Malcolm Gladwell")

body = b.find_element_by_xpath('//*[@id="lga"]')

time.sleep(2)
body.click()

btn = b.find_element_by_xpath(
    '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')

time.sleep(2)
btn.click()

img = b.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[2]/a')

img.click()

select = b.find_element_by_xpath(
    '//*[@id="islrg"]/div[1]/div[6]/a[1]/div[1]/img')

select.click()

image = b.find_elements_by_xpath(
    '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img')

time.sleep(5)

src = image[0].get_attribute("src")

urllib.request.urlretrieve(src, "Mal.jpg")
