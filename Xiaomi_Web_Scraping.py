import requests
from bs4 import BeautifulSoup
from time import sleep
import xlsxwriter

headers = {"User-agent": "Mozilla/5.0 (Windows NT 10.3; Win64; x64; en-US) AppleWebKit/601.29 (KHTML, like Gecko) Chrome/55.0.1010.318 Safari/603.1 Edge/16.37345"}


def get_url():
    for count in range(2,10): 

        url = f"https://xiaomi.com.ge/product-category/all-product/page/{count}/"

        response = requests.get(url, headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("div", class_ = "product-element-bottom")

        for i in data:
        
            card_url = i.find("a").get("href")
            yield card_url


def array():
    for card_url in get_url():
        
        response = requests.get(card_url, headers)
        sleep(3)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find("div", class_ = "col-lg-6 col-12 col-md-6 woodmart-price-outside summary entry-summary")
        name = data.find("h1", class_="product_title entry-title").text
        price = data.find("bdi").text
        product = data.find("p").text
        yield name, price, product, card_url

def writer(parametr):
    book = xlsxwriter.Workbook(r"C://Users//Maya//Desktop//Xiaomi_data.xlsx")
    page = book.add_worksheet("products")

    row = 0
    column = 0

    page.set_column("A:A", 65)
    page.set_column("B:B", 20)
    page.set_column("C:C", 50)
    page.set_column("D:D", 70)

    for item in parametr():
        
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        row = row + 1
    
    book.close()

writer(array)


    
