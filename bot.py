from selenium import webdriver
import time
import os, time

driver = webdriver.Chrome(executable_path=r"C:\scripts\Download\chromedriver.exe")

driver.get("https://web.whatsapp.com/")
time.sleep(10)

celular = "telefono"
mensaje = "mensaje"

driver.get("https://wa.me/"+celular+"?text="+mensaje)
time.sleep(5)

boton = driver.find_elements_by_xpath("//*[@id='action-button']")[0]
boton.click()
time.sleep(5)
boton = driver.find_elements_by_xpath("//*[@id='fallback_block']/div/div/a")[0]
boton.click()
time.sleep(30)

#boton enviar                        //*[@id='main']/footer/div[1]/div[3]
boton = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[3]")[0]
boton.click()
time.sleep(5)
	
print("-- Fin de Bot--")

time.sleep(40)

driver.close()