from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json
import pickle
import pprint
import time
  
""" Este código, permite usar selenium con la sesión iniciada de Whatsapp, mejorando así 
    el automatismo"""

options = webdriver.ChromeOptions();
options.add_argument('--user-data-dir=C:\\scripts\\Download\\User Data')
driver = webdriver.Chrome(executable_path=r"C:\scripts\Download\chromedriver.exe", chrome_options=options)
driver.get('https://web.whatsapp.com/')