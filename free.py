import requests
import json
from bs4 import BeautifulSoup
from snkreq import getallsnkrsitems

def snkrsmonitor(sku):

    itemrequest = json.loads(getallsnkrsitems())

    for products in itemrequest['threads']:
         #print(products['product']['style'])
         if sku == products['product']['style'] + "-" + products['product']['colorCode']:
             image = products['product']['imageUrl']
             title = products['product']['title']
             status = products['product']['merchStatus']
             price = products['product']['price']['fullRetailPrice']

    final_results = {
        "name": title,
        "status": status,
        "fullprice": price,
        "image": image,
    }
    return final_results

