import requests
from bs4 import BeautifulSoup

url = 'https://steamcommunity.com/market/listings/730/Antwerp%202022%20Contenders%20Sticker%20Capsule'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

span = soup.findall('span', {'class'{'market_commodity_orders_header_promote'})

print(span)
