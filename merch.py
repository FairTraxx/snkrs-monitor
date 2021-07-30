import requests

##get GTIN and corresponsing nike size
#productId = "9fe5060d-5285-50b3-94d6-d789acaf82a1"

def getgtin(productId):
    url = "https://api.nike.com/merch/skus/v2/?filter=productId({prod})&filter=country(US)".format(prod=productId)

    payload={}
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.nike.com/',
    'appid': 'com.nike.commerce.snkrs.web',
    'Content-Type': 'application/json; charset=UTF-8',
    'X-B3-TraceId': 'bf0622a5c1b94f33',
    'X-B3-SpanId': '93460049fb3ccff8',
    'X-B3-ParentSpanId': '261b2076d813f91e',
    'Origin': 'https://www.nike.com',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'TE': 'trailers',
    'Cookie': '_abck=A16D243D854464FFACDED3F3C53B303B~-1~YAAQVmrcF5ygmCx6AQAA+FEHkAZdmxTJLcm0AWfrh0qy/P1Yh+dDz/LFmkxvy+a3y6g/16szsO3Egy7qTIXM6klDMmPoj4dxr6vDqjfDUWzjcdpWwsn87rm17VCb9MuOIEfIy0iNlLz//dM3Ck2SxwAyxQXQUA+9FwEYOCBjiABcW+oc0385qyQ35Qopj7zM/8yC7iWfZ4gZR5dxhA+pinXgp9P0U1AXLS6x2r6UsItED36N/FrXrHMBQ9gIpLO3J49PqPBp9bgvjxJWwYc95ZBcbGMRmiTtgrR3q3CIlEHz8rFRoE6CyRucHW81jvohUBWhFNygk8hUuIrjMlZ5m4SCT1sST2t2qwFNrF/OeGMMWmULKnz9Ejc8WEcD4J3Rt8GH3iA0byfnGy5XjkW0ZjrEUjk=~-1~-1~-1; bm_sz=7706526C8E4FA4314731DC89CA466855~YAAQVmrcF5ugmCx6AQAA+FEHkAxZ1ZYGU/eppsS6la95pODvb/OW/KcBLUGjIH2xWbhFZhdyO4YTbkY8jsU20Oy4fbbECS6UaVJ4klYsXMXbsJhVxoxMwlvJulfUuOnoSG5AGmuSk6WJ7l3+fQ2ie+PcD7zPp6qQ+hQdYG9vSqsya6ube75hUZ1qKaqWkLIMF/o6SPSV68l3F/SxVtkM4CjVl9AZcLM0Cyai6TxntxyutKh9h15Y1YlsftnESLVKLtkwBmTAlF0TMY0yGiyplwFwq6aG7Puo'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text



    
