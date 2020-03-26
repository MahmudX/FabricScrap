import re
from bs4 import BeautifulSoup
import requests
import scanpage
import json


def type1(soup):
    try:
        output = []
        fabric = soup.find(
            'div', attrs={"class": "col-xs-12 col-sm-6 align-left tech-details"})
        fabList = fabric.find_all('li')
        for x in fabList:
            span = x.find_all('span')
            title = span[0].text
            data = re.sub('[ +()?→Â]', ' ', x.text.replace(title, '')
                          ).replace("&puncsp", '').replace("\n", '').replace("\u00b7", '').strip()
            output.append(title + " : " + data)
        return output
    except:
        return type2(soup)


def type2(soup):
    try:
        fabric = soup.find('ul', attrs={"data-for": "fa"})
        Items = fabric.find_all('li')
        output = []
        for x in Items:
            subitems = x.find_all('span')
            output.append(
                re.sub(' +', ' ', (subitems[0].text + " : " + subitems[1].text).strip().replace("\n", '').replace("\u00b7", '').replace("&puncsp", '')))
        return output
    except:
        return type3(soup)


def type3(soup):
    try:
        output = []
        fabric = soup.find('div', attrs={"class": "col-md-4 col-sm-4"})
        fabList = fabric.find_all('li')
        for x in fabList:
            output.append(
                re.sub('[ +()?→Â]', ' ', x.text).replace("\n", '').replace("\u00b7", '').replace("&puncsp", '').strip())
        return output
    except:
        return type4(soup)


def type4(soup):
    output = []
    fabric = soup.find(
        'div', attrs={"class": "col-xs-12 col-sm-6 align-left tech-details"})
    fabList = fabric.find_all('li')
    for x in fabList:
        output.append(
            re.sub('[ +()?→Â]', ' ', x.text).replace("\n", '').replace("\u00b7", '').replace("&puncsp", '').strip())
    return output


