from selenium import webdriver
import time
import os, time
import csv

options = webdriver.ChromeOptions();
options.add_argument('--user-data-dir=C:\\scripts\\Download\\User Data')
driver = webdriver.Chrome(executable_path=r"C:\scripts\Download\chromedriver.exe", chrome_options=options)
driver.get('https://web.whatsapp.com/')

time.sleep(10)

with open('datos.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        celular = (f'{row[0]}')
        mensaje = (f'{row[1]}')

driver.get("https://wa.me/"+celular+"?text="+mensaje)
time.sleep(2)

boton = driver.find_elements_by_xpath("//*[@id='action-button']")[0]
boton.click()
time.sleep(5)

try:
    boton = driver.find_elements_by_xpath("//*[@id='fallback_block']/div/div/a")[0]
    boton.click()
    time.sleep(10)
except: "Ya se encuentra registrado el whatsapp en el automatizador"

boton = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[3]")[0]
boton.click()

time.sleep(5)
	
print("-- Fin de Bot--")

time.sleep(10)

driver.close()

