#!/usr/bin/env python3
#author:rangapv@yahoo.com
#12-11-24

import os
import yfinance as yf

class fetch:
        #apple = yf.Ticker("AAPL")
    def df(self,tick1):
        apple = yf.Ticker(tick1)
        return apple

#main begins
if __name__ == "__main__":
    s = fetch()
    list1 = ["AAPL", "NVDA", "META", "AMZN", "GOOG", "TSLA", "MSFT" ]
    for x in list1:
        d1= s.df(x)
        print(d1.history(period="1d"))

