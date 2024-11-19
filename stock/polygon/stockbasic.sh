#!/usr/bin/env python3
#author:rangapv@yahoo.com
#14-11-24

from polygon import RESTClient
from polygon.rest import models

API_KEY = "H96GA05xheVXEGHuyXpB1hPQKOWve71Y"
client = RESTClient(API_KEY)

aggs = client.get_aggs(
    "AAPL",
    1,
    "day",
    "2024-11-14",
    "2024-11-14",
)
print(aggs)
details = client.get_ticker_details("AAPL")
detailcap = details.market_cap
print (detailcap)
