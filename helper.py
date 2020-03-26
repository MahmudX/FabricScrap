from bs4 import BeautifulSoup
import json
import scanpage
from tableScrap import type1
import requests


def SingleScrap():
    urlInput = input("Enter a valid URL: ")
    r = requests.get(urlInput)
    soup = BeautifulSoup(r.text, "html.parser")
    s = type1(soup)
    s.insert(0, urlInput)
    print(json.dumps(s))
    yn = input("Save as JSON? Y/N:")
    if yn == 'Y' or yn == 'y':
        writableData = []
        with open('singleDatas.json', 'r') as f:
            try:
                writableData = json.load(f)
            except:
                writableData = []
        with open('singleDatas.json', 'w') as f:
            writableData.append(s)
            json.dump(writableData, f, indent=4)
    else:
        pass


def GetTailoredCloth():
    urls = scanpage.GetTailoredClothLinks(
        "https://propercloth.com/tailored-clothing")
    writableData = []
    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        s = type1(soup)
        s.insert(0, url)
        writableData.append(s)
    with open('tailoredData.json', 'w') as f:
        json.dump(writableData, f, indent=4)


def GetAllFeaturedProducts():
    urls = scanpage.GetAllFeaturedProducts(
        "https://propercloth.com/collections/mojave")
    writableData = []
    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        s = type1(soup)
        s.insert(0, url)
        writableData.append(s)
    with open('featuredProducts.json', 'w') as f:
        json.dump(writableData, f, indent=4)
