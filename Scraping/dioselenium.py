from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import chromedriver_autoinstaller
from bs4 import BeautifulSoup

chromedriver_autoinstaller.install()

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
url = "https://auth.dio.me/realms/master/protocol/openid-connect/auth?client_id=spa-core-client&redirect_uri=https%3A%2F%2Fweb.dio.me%2F&state=3b9a2c8f-e560-46c8-8e72-2df6fc72a98e&response_mode=fragment&response_type=code&scope=openid&nonce=4e530526-bfbd-439e-8030-ed166fd81bec"
driver.get(url)
#driver.set_window_size(808, 727)
driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "username").send_keys("regymatrix@gmail.com")
driver.find_element(By.ID, "password").click()
driver.find_element(By.ID, "password").send_keys("acesso1")
driver.find_element(By.ID, "kc-login").click()
time.sleep(10)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
