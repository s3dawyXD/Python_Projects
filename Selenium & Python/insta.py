from conf import INSTA_PASS , INSTA_EMAIL
from selenium import webdriver
import time

browser = webdriver.Chrome()
url = 'https://www.instagram.com'
browser.get(url)
time.sleep(2)
username_el = browser.find_element_by_name('username')
password_el = browser.find_element_by_name('password')
submit_btn_el = browser.find_elements_by_css_selector("button[type='submit']")
