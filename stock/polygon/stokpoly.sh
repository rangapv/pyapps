#!/usr/bin/env python3
#author:rangapv@yahoo.com
#14-11-24

import os
import re
import subprocess
from polygon import RESTClient 
#from subprocess import PIPE

class fetch:
        #apple = yf.Ticker("AAPL")
    def polyget(self,API):
       client = RESTClient(API)
       return client

#main BEGINS
if __name__ == "__main__":
 p1 = fetch()
 #print (f'client is {p1}')
 API_KEY = "4u9WRFur29Qpp54aPXcuRRcsvYsG4myp"
 #API_KEY = "insert-api-key"
 client1 = p1.polyget(API_KEY)
 #print(f'client1 is {client1}')

 aggs = []
 list1 = ["META"]
 #list1 = ["AAPL", "NVDA", "META", "AMZN", "GOOG" ]
 for x in list1:
  aggs = client1.get_previous_close_agg(x)
  #print(f'Timestamp is {aggs.PreviousCloseAgg}') 
  #aggs = client1.get_aggs(
  #  x,
  #  1,
  #  "day",
  #  "2024-11-15",
  #  "2024-11-15"
    #limit=1 
  #)
    #sggs.append(a)
  details = client1.get_ticker_details(x)
  print(f'aggs is {aggs}')
  detailcap = details.market_cap
  #p2 = print (f"{details}")
  #grep1 = details + "| grep 'timestamp='"
  #print("grep1 is {grep1}")
  aggs1 = aggs[0]
  #aggs2 = aggs1[1] 
  #print(f"aggs1 is {aggs2}")
  pl = subprocess.run(['echo "{}" | grep timestamp'.format(aggs1)], capture_output=True, shell=True, text=True, check=False)
  l21 = pl.stdout
 # os.system(grep1)
  p3 = "awk \'{split($0,a,\",\"); print a[6]}\'"
  l22 = subprocess.run(['echo "{}" | {}'.format(l21,p3)], capture_output=True, shell=True, text=True, check=False)
  l23 = l22.stdout
  #print (f"pl is {pl}")
  #print (f"l21 is {l21}")
  #print (f"l22 is {l23}")
  p4 = "awk \'{split($0,a,\"=\"); print a[2]}\'"
  l23 = subprocess.run(['echo "{}" | {}'.format(l23,p4)], capture_output=True, shell=True, text=True, check=False)
  p5 = l23.stdout
  print(f"timesstap numeral is {p5}")
  print (f"the stock with ticker symbol \"{x}\" has a market cap of {detailcap}")
 
  #print(f"aggs for \"{x}\" s {aggs}")

