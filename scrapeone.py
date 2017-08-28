import requests
from bs4 import BeautifulSoup

url = "https://www.bloomberg.com/quote/TATA:IN"

req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")

eqtyName = soup.find("h1", {"class": "name"})
eqtyPrice = soup.find("div", {"class": "price"})
eqtyTick = soup.find("div", {"class": "ticker"})
eqtyCurr = soup.find("div", {"class": "currency"})
exch = soup.find("div", {"class": "exchange"})

name = eqtyName.text
ticker = eqtyTick.text.upper()
price = eqtyPrice.text
currency = eqtyCurr.text
exchange = exch.text.upper()

print(name, "(", ticker, ")", currency, price)
print(exchange)
