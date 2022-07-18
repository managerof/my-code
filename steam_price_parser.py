import requests
from bs4 import BeautifulSoup

url = 'https://steamcommunity.com/market/listings/730/Sticker%20%7C%20Cloud9%20%7C%20Antwerp%202022'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

price = soup.findAll('span',{'class':'market_commodity_orders_header_promote'})

print(price)