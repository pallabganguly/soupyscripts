import requests
from bs4 import BeautifulSoup

# This file will get 10 Quotes current stock price from Bloomberg.
# BSE and NSE wasnt working

quotes = ["GOOGL:US",
          "TATA:IN",
          "TCS:IN",
          "IOCL:IN",
          "PG:IN",
          "CTSH:US",
          "STAR:MK",
          "SBIN:IN",
          "GE:US",
          "005930:KS"]

for quote in quotes:
    url = "https://www.bloomberg.com/quote/"+quote
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


    print(name, " (", ticker, ") ", currency," ", price, sep = "")
    print(exchange)
