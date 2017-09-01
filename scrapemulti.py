import requests
from bs4 import BeautifulSoup

# This file will get 10 Quotes current stock price from Bloomberg.
# BSE and NSE wasnt working

urls = ["https://www.bloomberg.com/quote/GOOGL:US",
        "https://www.bloomberg.com/quote/TATA:IN",
        "https://www.bloomberg.com/quote/TCS:IN",
        "https://www.bloomberg.com/quote/IOCL:IN",
        "https://www.bloomberg.com/quote/PG:IN",
        "https://www.bloomberg.com/quote/CTSH:US",
        "https://www.bloomberg.com/quote/STAR:MK",
        "https://www.bloomberg.com/quote/SBIN:IN",
        "https://www.bloomberg.com/quote/GE:US",
        "https://www.bloomberg.com/quote/005930:KS"]

for url in urls:
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
