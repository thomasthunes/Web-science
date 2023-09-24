import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

op = Options()
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=op, service=s)
driver.get('https://www.tetralark.com/ClickerJs/')

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button')))
button = driver.find_element(By.XPATH, '//button')

while True:
    for i in range(10):
        button.click()

    current_clicks = driver.find_element(By.XPATH, '//span[2]').text
    upgrade = driver.find_element(By.XPATH, '//ul/li[last()]/span/span[2]').text
    if int(current_clicks) >= int(upgrade):
        driver.find_element(By.XPATH, '//ul/li[last()]/span/button').click()
    #time.sleep(1000)

#time.sleep(10000)
