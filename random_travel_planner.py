import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

op = Options()
op.add_argument('--kiosk')
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=op, service=s)
driver.get('https://www.google.com')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//textarea[@class="gLFyf"]')))
driver.find_element(By.XPATH, '//button[@id = "W0wltc"]').click()
search = driver.find_element(By.XPATH, '//textarea[@class="gLFyf"]')
search.send_keys("random country generator")
search.submit()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h3[@class="LC20lb MBeuO DKV0Md"]')))
sites = driver.find_elements(By.XPATH, '//h3[@class="LC20lb MBeuO DKV0Md"]')
for site in sites:
    if site.text == "Generate Random Countries - Random Lists":
        site.click()
        break

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[@class="rand_medium"]')))
country = driver.find_element(By.XPATH, '//span[@class="rand_medium"]').text
driver.back()

driver.find_element(By.XPATH, '//div[@class="M2vV3 vOY7J"]').click()
search = driver.find_element(By.XPATH, '//textarea[@class="gLFyf"]')
search.send_keys("google flights")
search.submit()

driver.find_element(By.XPATH, '//h3[@class="LC20lb MBeuO DKV0Md"]').click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="II2One j0Ppje zmMKJ LbIaRd"]')))
destination = driver.find_elements(By.XPATH, '//input[@class="II2One j0Ppje zmMKJ LbIaRd"]')[2]

#print(destination.get_attribute('class'))
#destination.click()
#time.sleep(1)
#destination.send_keys('')
destination.send_keys(country)
time.sleep(0.5)
driver.find_element(By.XPATH, "//*[@class='zsRT0d']").click()

driver.find_element(By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-Bz112c-M1Soyc nCP5yc AjY5Oe LQeN7 TUT4y zlyfOd']").click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='VfPpkd-WsjYwc VfPpkd-WsjYwc-OWXEXe-INsAgc KC1dQ Usd1Ac AaN0Dd  wbv5Uc']")))
driver.find_element(By.XPATH, "//div[@class='VfPpkd-WsjYwc VfPpkd-WsjYwc-OWXEXe-INsAgc KC1dQ Usd1Ac AaN0Dd  wbv5Uc']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[@class='DvoDQ']").click()
time.sleep(.5)

#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='yR1fYc']")))
#driver.find_element(By.XPATH, "//div[@class='yR1fYc']").click()
time.sleep(10000)