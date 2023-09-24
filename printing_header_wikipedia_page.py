from urllib.request import urlopen
from bs4 import BeautifulSoup
import scrapy
html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html.read(), 'html.parser')
test = bs.find("ligmaballs")

