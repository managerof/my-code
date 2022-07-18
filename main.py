import requests
from bs4 import BeautifulSoup

url = 'https://minfin.com.ua/currency/nbu/'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

table = soup.find('table', {'class' : 'sc-1mi6rpw-9 kdhvRG'})
tr =  table.find('td', {'class' : 'sc-133jxom-0 iFPkTo'})

print(tr)
