from urllib.request import urlopen as uReq
import bs4
import pandas as pd
from bs4 import BeautifulSoup as soup


my_url = 'https://www.franklywearing.com/creator-products?product_id=103'

uClient = uReq(my_url)

page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, "html.parser")

# print(page_soup.prettify())

products = page_soup.ul

containers = page_soup.findAll("div", {"class": "product-shoe-info shoe"})

names = []
for i in containers:
    names.append(i.a.img["alt"])

price_soup = page_soup.findAll("span", {"class": "money"})

prices = []
for i in price_soup:

    prices.append(i.text.strip())


print(names)
print(prices)


f = open('hello.csv', 'w', encoding='utf-8')
for i in range(len(names)):
    f.write(names[i].replace(",", "|") + "," + prices[i].replace(",", "|") + '\n')
f.close()
