from selenium import webdriver
import time 
import os, time 

""" Lo primero que haremos será ejecutar el driver desde la ruta de preferencia"""

driver = webdriver.Chrome(executable_path=r"C:\scripts\Download\chromedriver.exe")

driver.get("http://www.python.org")
time.sleep(10)

driver.close


