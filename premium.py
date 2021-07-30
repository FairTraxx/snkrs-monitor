import requests
import json
from bs4 import BeautifulSoup
from snkreq import getallsnkrsitems
from merch import getgtin
from stock import getStock
#sku = "CD0461-002"

def snkrsmonitorpremium(sku):
    
    itemrequest = json.loads(getallsnkrsitems())

    for products in itemrequest['threads']:
         #print(products['product']['style'])
         if sku == products['product']['style'] + "-" + products['product']['colorCode']:
             
             prodname = products['product']['title']
             image = products['product']['imageUrl']
             status = products['product']['merchStatus']
             price = products['product']['price']['fullRetailPrice']
             pid = products['product']['id']
             color = products['product']['colorDescription']
             startdate = products['product']['startSellDate']
             all_gtins = getgtin(pid)
             #print(all_gtins)
             gtin_result = json.loads(all_gtins)
             d1 = {}
             for obj in gtin_result['objects']:
                 d1[obj['gtin']] = obj['nikeSize']
             # get stock for product from stock.py
             available = getStock(sku)
             avail_res = json.loads(available)
             d2 = {}
             print(d1)
             print(d2)
             for obj in avail_res['objects']:
                 d2[obj['gtin']] = obj['level']
             # print(d2)
 
             # merge both dicts with gtin keys that match each other
             d = {}
             for key in set(list(d1.keys()) + list(d2.keys())):
                 try:
                     d.setdefault(key, []).append(d1[key])
                 except KeyError:
                     d.setdefault(key, []).append('To be announced size')
                     pass
 
                 try:
                     d.setdefault(key, []).append(d2[key])
                 except KeyError:
                     d.setdefault(key, []).append('OOS')
                     pass
 
             size_list = list(d.values())

    final_results = {
        "name": prodname,
        "status": status,
        "fullprice": price,
        "image": image,
        "color": color,
        "startdate": startdate,
        #"productid": pid,
        "size": size_list
    }
    return final_results
    #print(itemrequest)

#print(snkrsmonitorpremium(sku))