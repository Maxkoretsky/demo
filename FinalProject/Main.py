# This file was created by Maxim Koretsky
# Credits : 
# https://docs.python-guide.org/scenarios/scrape/
# https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/
# https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe

from bs4 import BeautifulSoup
import requests
import csv
import urllib2


# URL of site scrap
quotepage = "https://stockx.com/supreme-waist-bag-fw18-black"


# # query the website and return the html to the variable ‘page’
# page = urllib.urlopen(quotepage)

# # parse the html using beautiful soup and store in variable `soup`
# soup = beautifulsoup(page, html.parser)

# # Take out the <div> of name and get its value
# name_box = soup.find('h1', attrs={'class': 'name'})

# # strip () is used to remove starting and trailing
# name = name_box.text.strip()
# print(name) 

# # get trade value 
# price_box = soup.find(‘div’, attrs={‘class’:’price’})
# price = price_box.text
# print(price)
