import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

op = Options()
#op.add_argument('--headless')
op.add_argument('--kiosk')
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=op, service=s)

driver.get('http://www.vg.no')
time.sleep(5)

headline = driver.find_element(By.TAG_NAME, 'span')
print(headline.text)


scheight = 10
while scheight < 10000:
    driver.execute_script('window.scrollTo(0, {});'.format(scheight))
    scheight += 1
    time.sleep(0.01)

driver.close()





















