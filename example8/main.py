import requests
from bs4 import BeautifulSoup
import csv

#
# url='https://coinmarketcap.com/'
# headers={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0"
# }
# req=requests.get(url,headers=headers)
# src=req.text
#
#
# with open("index.html","w",encoding='utf-8') as file:
#      file.write(src)

with open("index.html","r",encoding='utf-8') as file:
    src=file.read()

soup=BeautifulSoup(src,"lxml")

all_coins=soup.find(class_="h7vnx2-2 juYUEZ cmc-table")

coins_name=all_coins.find_all(class_="sc-1eb5slv-0 iworPT")
coins_cost=all_coins.find_all("a",class_="cmc-link")



name_list=[]
for coin in coins_name:
    name_list.append(coin.text)


price_list=[]
for price in coins_cost:
    price=price.find("span")
    if price is not None:
        if price.text!='':
            price_list.append(price.text)

print(name_list)
print(price_list)

with open(f'coins.csv', 'w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file,)

    for i in range(len(name_list)):
        writer.writerow([name_list[i],price_list[i]])




