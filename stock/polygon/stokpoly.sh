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
 API_KEY = "080dt12muu7EP9aOOYYTb1LDEOhPsTr3"
 client1 = p1.polyget(API_KEY)
 print(f'client1 is {client1}')

 aggs = []
 list1 = ["AAPL", "NVDA", "META", "AMZN", "GOOG", "TSLA", "MSFT" ]
 for x in list1:
  aggs = client1.get_aggs(
    x,
    1,
    "minute",
    "2024-11-14",
    "2024-11-14",
   # limit=10 
  )
    #aggs.append(a)

 print(f"aggs is {aggs}")
