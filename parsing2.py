import requests
from bs4 import BeautifulSoup

url = 'https://steamcommunity.com/market/search?q=Antwerp+2022+Contenders+Sticker+Capsule'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

table = soup.find('span', {'class' : 'market_table_value normal_price'})
tr =  table.find('span', {'class' : 'normal_price'})
tr = tr.text
tr = tr[1:5]
price = (float(tr) * 30)
print('Цена капсулы Antwerp 2022 Contenders Sticker Capsule в долларах -', tr,'$')
print('Цена капсулы Antwerp 2022 Contenders Sticker Capsule в гривнах -', ("%.2f" % price), '₴')