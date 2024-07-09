from selenium import webdriver as wd
import time, parser_site, sql_uploader

server = "https://vk.com/deceasedep"

#st_useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

browser = wd.Chrome("/usr/bin/chromedriver/")

browser.quit() 

#Для начала нам нужно получить стоковую страницу профиля от которого будет идти разыгровка всех страниц в будущем.
#На каждом шаге мы будем проверять, является ли пользователь добавленным в наш список и если он таковым является, 
#и переходим к следующему, чтобы не было повторений.