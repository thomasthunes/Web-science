from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from random import shuffle

op = Options()
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=op, service=s)
driver.get('https://www.nytimes.com/games/wordle/index.html')
time.sleep(3)
driver.find_element(By.ID, 'pz-gdpr-btn-closex').click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, 'Welcome-module_button__ZG0Zh').click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, 'game-icon').click()
time.sleep(1)

# key_rows = driver.find_elements(By.CLASS_NAME, "Keyboard-module_row__ilOKU")
key_rows = driver.find_elements(By.XPATH, '//div[@class="Keyboard-module_row__ilOKU"]/*')
# backslash = driver.find_element(By.CLASS_NAME, 'Key-module_key__kchQI Key-module_oneAndAHalf__bq8Tw')

print(key_rows)

keys = dict()
for key in key_rows:
    char = key.text
    if char != '':
        keys[char] = key

backslash = driver.find_elements(By.XPATH, '//button[@class="Key-module_key__kchQI Key-module_oneAndAHalf__bq8Tw"]')[1]
words = open('five_letter_words', 'r').read().split('\n')
#shuffle(words)


def delete_word():
    for i in range(5):
        backslash.click()


absent_chars = set()
present_chars = set()
correct_chars = dict()

def is_double_letter(word, the_char):
    count = 0
    for char in word:
        if char == the_char:
            count += 1
    if count > 1:
        return True
    return False


def is_possible_word(word):
    useful_chars = 0
    for char in word:
        if char in absent_chars:
            return False
        if char in present_chars:
            useful_chars += 1

        if char in correct_chars:
            if correct_chars[char] != word.index(char):
                return False

    if not useful_chars == len(present_chars):
        return False

    for correct_char, index in correct_chars.items():
        if word[index] != correct_char and not is_double_letter(word, correct_char):
            return False
    return True


words_tried = 0
for word in words:
    words_tried += 1
    if not is_possible_word(word):
        continue
    for char in word:
        keys[char.upper()].click()

    keys['ENTER'].click()
    time.sleep(2)

    tiles = driver.find_elements(By.CLASS_NAME, 'Tile-module_tile__UWEHN')
    for tile in tiles:
        status = tile.get_attribute('aria-label').split(' ')
        if len(status) == 2:
            if status[1] == 'absent':
                absent_chars.add(status[0])
            if status[1] == 'present':
                present_chars.add(status[0])
            if status[1] == 'correct':
                present_chars.add(status[0])
                correct_chars[status[0]] = word.index(status[0])

print(words_tried)
time.sleep(10)
