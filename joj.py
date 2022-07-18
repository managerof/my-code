import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=%D1%86%D0%B5%D0%BD%D0%B0+%D0%BD%D0%B0+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD&ei=v0nQYsPFKtaP8gLSsbQg&ved=0ahUKEwiDocXK6_j4AhXWh1wKHdIYDQQQ4dUDCA0&uact=5&oq=%D1%86%D0%B5%D0%BD%D0%B0+%D0%BD%D0%B0+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QBzIGCAAQHhAHMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6DQguEMcBENEDELADEEM6CAgAEB4QBxATOgoIABAeEAcQBRATOgoIABAeEAgQBxATOgQIABBDOgkIABANEEYQggI6BAgAEA06CQgAEEMQRhCCAkoECEEYAEoECEYYAFD7EVizUmCFWGgHcAF4AYABf4gB4gySAQQyMS4ymAEAoAEByAEKwAEB&sclient=gws-wiz'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

#table = soup.find('div',{'class' : 'css-6sm2ml'})
#tr = table.findAll('div',{'data-bn-type' : 'text'})
#bnb = soup.findAll('div',{'data-bn-type' : 'text'})

bnbprice = soup.find('span', {'class' : 'pclqee'})

print(bnbprice)