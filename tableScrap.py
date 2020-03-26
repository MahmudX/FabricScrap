import re
from bs4 import BeautifulSoup
import csv
import requests
import scanpage


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
                          ).replace("&puncsp", '').strip()
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
                re.sub(' +', ' ', (subitems[0].text + " : " + subitems[1].text).strip().replace("\n", '')))
        return output
    except:
        return type3(soup)


def type3(soup):
    output = []
    fabric = soup.find('div', attrs={"class": "col-md-4 col-sm-4"})
    fabList = fabric.find_all('li')
    for x in fabList:
        output.append(x.text)
    return output


def main():
    # urls = ["https://propercloth.com/products/biella-navy-wool-shearling-collar-flight-jacket-726.html"]
    # datafile = open('datafile.csv', 'a+',
    #                 newline='', encoding="utf-8")
    # writer = csv.writer(datafile)
    # for url in urls:
    #     r = requests.get(url)
    #     soup = BeautifulSoup(r.text, "html.parser")
    #     s = type2(soup)
    #     s.insert(0, url)
    #     writer.writerow(s)
    print(scanpage.GetStockedProducts("https://propercloth.com/dress-shirts"))


if __name__ == "__main__":
    main()
