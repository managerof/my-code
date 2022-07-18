import requests
from bs4 import BeautifulSoup

url = 'https://minfin.com.ua/currency/nbu/'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

table = soup.find('table', {'class' : 'sc-1mi6rpw-1 gnPEbq'})
tr = table.find('td', {'class' : 'sc-1mi6rpw-8 gYhawK'})
tr = tr.text

doll = 'Курс доллара к гривне ' + str(tr)[:5]

print(doll)