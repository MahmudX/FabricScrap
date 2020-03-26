from bs4 import BeautifulSoup
import requests


def GetFabricLinks(url):
    r = requests.get(url)
    output = []
    file1 = open("MyFile.txt", "a+", encoding="utf-8")
    file1.write(r.text)
    soup = BeautifulSoup(r.text, "html.parser")
    main = soup.find('main', attrs={'class': 'content'})
    # print(main)
    fabrics = soup.find_all('div', attrs={'class': 'fabric-item'})
    # print(fabrics)
    for x in fabrics:
        link = x.find('a')['href']
        output.append(link)
    return output


def GetTailoredClothLinks(url):
    # gallery-cell is-coat is-new
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
    #gallery-cell is-shirt
    r = requests.get(url)
    output = []
    soup = BeautifulSoup(r.text, "html.parser")
    products = soup.find_all(
        'div', attrs={'class': 'gallery-cell is-shirt'})
    for x in products:
        link = x.find('a')['href']
        output.append(link)
    return output
