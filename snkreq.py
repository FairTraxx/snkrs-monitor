import requests

def getallsnkrsitems():
    url = "https://api.nike.com/snkrs/content/v1/?country=US&language=en&offset=0&orderBy=published"

    payload={}
    headers = {
    'Cookie': '_abck=A16D243D854464FFACDED3F3C53B303B~-1~YAAQTLOe1TqjMO16AQAAUwWD7gbXscUS5ILradJ2gGcTWFwMX5D7i9xSoqz8mb9RU1hBgtvwEg+6e04V7ob9hdv6cX9Ret/0MsLvRsY3OW8K2m43Ru5ej8LYuC30FJ1/jy+0I29C5uX2wJm82qditl37YuDT/haPjbzniSt7PxFrI9n6gtjKlR5/0WyPGQ2nVHN3TGM8RKFdeBewqSKqaTSVKD+9cT97IEHot72fcZY6RrA6QdN090UBljwnpJ8/QHJmtsiAU2UaT/L3yC23+VstfxH6u7wG2ctTEo6VmUGd/3uFjaCmlV75w/RN0T0AVyMkP5PAxJO4U7PsvVsl0orL5hhfIlLrfMYFOBOjFrwPed+0gvwaQ/6616pMjw5jxWFYH3sAitu+cCquebXgaA+UI94=~-1~-1~-1; bm_sz=6137C1A5591FDA04E83B1027FE4B29C1~YAAQTLOe1TujMO16AQAAUwWD7gz43JsDjcjAyg/X7dxS+XjKK7IwALB886MhhyfODOnqJX5UEAX1R/RxCO9Pug80UBV06U9OAnXqk6lJaFdiLDZ+FGd03bTaM0slkwUAT+d4xaS7Lm0MLNGZhdWescTNYRUZkPfDKXTQhj4LmwpfxGq/0SfoLgNpIE+zzgBoHQW9wcqbnF4xnkQX88wEFcuzogiAPKHGDX4WgoOe9v+0WNHSjftMvWEOxw6AC4m/W689f/vNm8lf7c6veKZjDPU5AHc2ASRc0VQu91vNy1dKv7v59i4yDXhVlfH3xSjDKxnzjk2LuZOtSNMEdDXwwclNxEPi8M/oZv0sSi+1NXF6Ti7PGiQSJWKv4km58g==~4277811~4470068'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text

