import os
import subprocess
import sys
from polygon import RESTClient
import datetime
from numerize import numerize

def handler(event, context):
    r1 = hello()

    r2 = imagels()
    stock_dict1 = stock1() 
    print(f'stck_dict1 is {stock_dict1}')
    myList = [stock_dict1 [i][0] for i in sorted(stock_dict1.keys()) ]

    myList1 = {key:value[0] for key,value in stock_dict1.items()}
    sList1 = dict(sorted(myList1.items(), key=lambda item: item[1], reverse=True))
    #myList2 = dict(filter(lambda x : x[0],count.myList1()))
    #dct = myList1
    #myList2 = lambda dic: dic.keys()[0],dic.pop(dic.keys()[0])
    #myList2(dic)
    #myList2 = dict(filter(lambda x : x[0][0] , dct.items()))
    #print(f'myList1 is {myList1}')
    #print(f'myList2 is {myList2}')
    #print(myList)
    #print (f'stock_dict1 is {stock_dict1}')
    #print (f'mylist is {myList}')
    #print (f'myList1 is {sList1}')
    return sList1 

def temp():
    myList = [stock_dict1 [i][0] for i in sorted(stock_dict1.keys()) ]
    myList1 = [(i,stock_dict1 [i][0]) for i in sorted(stock_dict1.keys()) ]
    #print(myList)

    uplist = sorted(myList1,key=lambda x: x[1])
    revlist = sorted(myList1,key=lambda x: x[1], reverse=True)

    myList.sort()
    myList1.sort()

    print(f'TOP most-valuable-company from the list\n')
    i = 1
    for key,value in revlist:
        print (f"{i}. {key} with the value $ {numerize.numerize(value,4)}")
        valueprev = value
        i = i + 1


    return r2 
def hello():
    return "Hello World"

def imagels():
    t1 = subprocess.run("ls -la", capture_output=True, shell=True, text=True, check=True)
    imgtlen = t1.stdout
    #print(contlen)
    len1 = len(imgtlen.splitlines())
    #print("**********************")
    #print(f'total images are {len1-1}')
    return(f'total files in the container running are {len1-1} and the list is \n {t1.stdout}')

def getit(client11,list21,stock_dict2):
    #self.list2 = list21
    #print(stock_dict2)
    print(f'in getit lsit is {list21}')
    for x in list21:
      aggs = client11.get_previous_close_agg(x)
      details = client11.get_ticker_details(x)
      detailcap = details.market_cap
      aggs1 = aggs[0]
      pl = subprocess.run(['echo "{}" | grep timestamp'.format(aggs1)], capture_output=True, shell=True, text=True, check=False)
      l21 = pl.stdout
      p3 = "awk \'{split($0,a,\",\"); print a[6]}\'"
      l22 = subprocess.run(['echo "{}" | {}'.format(l21,p3)], capture_output=True, shell=True, text=True, check=False)
      l23 = l22.stdout
      p4 = "awk \'{split($0,a,\"=\"); print a[2]}\'"
      l23 = subprocess.run(['echo "{}" | {}'.format(l23,p4)], capture_output=True, shell=True, text=True, check=False)
      p5 = l23.stdout
      now1 = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
      now2 = datetime.datetime.now().strftime('%d-%m-%y')
      stock_dict2 = { **stock_dict2, x : [ detailcap , now2 ] }
      #p1.printout()
      print(f'in getit print dict')
      print(stock_dict2)

    return stock_dict2

def stock1():
    #print (f'client is {p1}')
    #API_KEY = os.getenv('API_POLYGON')
    API_KEY = "QHDVTpqPTAu3RdI54_kiAVefPuoSVrAU" 
    client1 = RESTClient(API_KEY)

    aggs = []
    list1 = ["META", "NVDA","AAPL"]
    stock_dict = {}
    #list1 = ["AAPL", "NVDA", "META", "AMZN", "GOOG" ]
    new24_dict = getit(client1,list1,stock_dict)
    print (f'new24 is {new24_dict}')
    list2 = ["SNOW","BRK.B","LLY","AVGO","DE"]
    #sleep(60)
    #new25_dict = getit(client1,list1,new24_dict)
    return new24_dict
