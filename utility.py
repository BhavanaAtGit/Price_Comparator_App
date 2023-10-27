import requests
from bs4 import BeautifulSoup

def get_price_from_flipkart(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="dyC4hf")
    price_element = box.find("div", class_="_30jeq3 _16Jk6d")
    price = price_element.text.strip()
    return price

def get_price_from_reliance_digital(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    price_element = soup.find("li", class_="pdp__priceSection__priceListText")
    price = price_element.text.strip()
    index = price.index('.')
    substring = price[price.index('₹'):index]
    return substring

def get_price_from_vijay_sales(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    price_element = soup.find("div", "priceMRP")
    price = price_element.text.strip()
    index = price.index('M')
    substring = price[price.index('₹'):index]
    return substring


