import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/watch?v=nopEs-K4ExM'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

price = soup.findAll('a',{'class':'yt-simple-endpoint style-scope ytd-toggle-button-renderer'})

print(price)
print(soup)