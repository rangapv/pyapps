#!/usr/bin/env python3
#author:rangapv@yahoo.com
#14-11-24

from polygon import RESTClient 

class fetch:
        #apple = yf.Ticker("AAPL")
    def polyget(self,API):
       client = RESTClient(API)
       return client

#main BEGINS
if __name__ == "__main__":
 p1 = fetch()
 print (f'client is {p1}')
 API_KEY = "H96GA05xheVXEGHuyXpB1hPQKOWve71Y"
 client1 = p1.polyget(API_KEY)
 print(f'client1 is {client1}')

 aggs = []
 list1 = ["META", "TSLA" ]
 #list1 = ["AAPL", "NVDA", "META", "AMZN", "GOOG" ]
 for x in list1:
  aggs = client1.get_aggs(
    x,
    1,
    "day",
    "2024-11-15",
    "2024-11-15"
    #limit=1 
  )
    #sggs.append(a)
  details = client1.get_ticker_details(x)
  detailcap = details.market_cap
  print (f"the stock with ticker symbol \"{x}\" has a market cap of {detailcap}")
  print(f"aggs for \"{x}\" s {aggs}")

