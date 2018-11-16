from requests import get

url = "https://stockx.com/supreme-waist-bag-fw18-black"

response = get(url)

from bs4 import BeautifulSoup

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

price_blackbag = html_soup.find_all('div', class_ = s-range value-container)
print(type(price_blackbag))
print(len(price_blackbag))