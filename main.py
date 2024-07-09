from selenium import webdriver as wd
import time

server = "https://vk.com/deceasedep"

#st_useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

browser = wd.Chrome("/usr/bin/chromedriver/")

browser.quit() 