import os
from utils.write_fetch import write_fetch

category = "semi"
filetype = "json"

tickers = open(f"tickers/{category}.txt", "r")
for ticker in tickers.readlines():
   write_fetch(f"https://financialmodelingprep.com/api/v3/historical-price-full/{ticker.strip()}?apikey={os.environ['FMP_KEY']}", f"{category}/historical-price-full/{ticker.strip()}.{filetype}")
   print(ticker.strip())
tickers.close()