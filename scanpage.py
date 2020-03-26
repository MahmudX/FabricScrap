from bs4 import BeautifulSoup
import requests


def GetFabricLinks(url):
    r = requests.get(url)
    output = []
    file1 = open("MyFile.txt", "a+", encoding="utf-8")
    file1.write(r.text)
    soup = BeautifulSoup(r.text, "html.parser")
    fabrics = soup.find_all('div', attrs={'class': 'fabric-item'})
    for x in fabrics:
        link = x.find('a')['href']
        output.append(link)
    return output


def GetTailoredClothLinks(url):
    r = requests.get(url)
    output = []
    soup = BeautifulSoup(r.text, "html.parser")
    clothes = soup.find_all(
        'div', attrs={'class': 'gallery-cell is-coat is-new'})
    for x in clothes:
        link = x.find('a')['href']
        output.append(link)
    return output


def GetStockedProducts(url):
    r = requests.get(url)
    output = []
    soup = BeautifulSoup(r.text, "html.parser")
    products = soup.find_all(
        'div', attrs={'class': 'gallery-cell is-shirt'})
    for x in products:
        link = x.find('a')['href']
        output.append(link)
    return output


def GetAllFeaturedProducts(url):
    r = requests.get(url)
    output = []
    soup = BeautifulSoup(r.text, "html.parser")
    products = soup.find_all(
        'div', attrs={'class': 'col-xxs-6 col-xs-6 col-sm-4 featured-product'})
    for x in products:
        link = x.find('a')['href']
        output.append(link)
    return output
