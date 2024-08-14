from selenium import webdriver
from selenium.webdriver.chrome.service import Service

web='https://www.audible.com/search'
path='C:\Users\simant.asawale\Desktop\chrome-win64'

service=Service(executable_path='path')
driver=webdriver.Chrome(service=service)