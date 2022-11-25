import requests
from bs4 import BeautifulSoup
import re
for URL in range(0,2569,25):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}

    soup = BeautifulSoup(requests.get(f'https://www.fabreminerals.com/search_results.php?LANG=EN&SearchTerms=&submit=Buscar&MineralSpeciment=&Country=&Locality=&PriceRange=&checkbox=enventa&First={URL}', headers=headers).text, "lxml")

    names = [n.getText(strip=True) for n in soup.select("table tr td font>a")]

    prices = [p.getText(strip=True).split("Price:")[-1] for p in soup.select("table tr td font>font")]   
       
    names[:] = [" ".join(n.split()) for n in names if not n.startswith("[") ]
    prices[:] = [p for p in prices if p]

    with open("MineralsList.txt", "a+", encoding='utf-8') as file:
        for name, price in zip(names, prices):
                # print(f"{name}\n{price}")
                # print("-" * 50)
                filename = str(name)+"|"+str(price)+"\n"
                split1 = filename.split(' / ')          
                cutted1 = split1.pop(0)
                split2 = cutted1.split(": ")
                cutted2 = split2.pop(1)
                try:
                    two_prices = cutted2+"|"+split1.pop(0)+"\n"
                except IndexError:
                    two_prices = cutted2+"\n"
                file.write(two_prices)
                      

