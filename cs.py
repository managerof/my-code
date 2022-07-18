import requests
from bs4 import BeautifulSoup

url = 'https://steamcommunity.com/market/listings/730/Sticker%20%7C%20VINI%20%7C%20Antwerp%202022'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

table = soup.find('div', {'class' : 'market_commodity_order_summary'})
tr =  table.find('span', {'class' : 'market_commodity_orders_header_promote'})

tr = tr.text
tr = tr[1:5]
table = table.text
print(table)