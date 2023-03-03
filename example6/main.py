import time

import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver



def get_data(url):
    headers={
        "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / avif, image / webp, * / *;q = 0.8",
        "Accept - Language": "en - US, en;q = 0.5",
        "Cache - Control": "max - age = 0",
        "Connection": "keep - alive",
        "User - Agent": "Mozilla / 5.0(Windows NT 10.0; rv: 91.0) Gecko / 20100101 Firefox / 91.0"
    }

    r=requests.get(url=url,headers=headers)

    with open("index.html","w",encoding='utf-8') as file:
        file.write(r.text)

    # get hotels urls
    r=requests.get("https://api.rsrv.me/hc.php?a=hc&most_id=1317&l=ru&sort=most",headers=headers)
    soup=BeautifulSoup(r.text,"lxml")

    hotels_cards=soup.find_all("div",class_="hotel_card_dv")

    for hotel_url in hotels_cards:
        hotel_url=hotel_url.find("a").get("href")
        print(hotel_url)


# def get_data_with_selenium(url):
#     options=webdriver.FirefoxOptions()
#     options.set_preference("general.useragent.override", "Mozilla / 5.0(Windows NT 10.0; rv: 91.0) Gecko / 20100101 Firefox / 91.0" )
#
#     try:
#         driver=webdriver.Firefox(
#             executable_path=r"C:\Users\tkac0\Desktop\parsing\lesson6\geckodriver.exe",
#             options=options
#         )
#         driver.get(url=url)
#         time.sleep(5)
#
#         with open("index_selenium.html","w",encoding="utf-8") as file:
#             file.write(driver.page_source)
#
#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.close()
#         driver.quit()
#
#
#     with open("index_selenium.html")
#     # get hotels urls
#
#     #soup = BeautifulSoup(r.text, "lxml")
#
#     hotels_cards = soup.find_all("div", class_="hotel_card_dv")
#
#     for hotel_url in hotels_cards:
#         hotel_url = hotel_url.find("a").get("href")
#         print(hotel_url)




if __name__ == '__main__':
    # get_data("https://www.tury.ru/hotel/most_luxe.php")
    get_data_with_selenium("https://www.tury.ru/hotel/most_luxe.php")
