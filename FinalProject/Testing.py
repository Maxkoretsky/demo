import urllib
from bs4 import BeautifulSoup
import requests
import lxml

# The url Specified 
page_link = "https://stockx.com/supreme-waist-bag-fw18-black"
page = requests.get(page_link)
tree = html.fromstring(page.content)

# html from StockX
# <div class="ds-range value-container"><span class="value">$101<span> - </span>$107</span></div>

price = tree.xpath('//div[@class="="ds-range value-container"]/text()')

print(price)
