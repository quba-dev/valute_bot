import requests
from bs4 import BeautifulSoup
import lxml
import csv

def get_html(url):
    r = requests.get(url)
    return r.text

def get_links(html):
    soup = BeautifulSoup(html,'lxml')
    valutes = soup.find('div', class_='rate-list active').find('table', class_='vl-list').find_all('td', class_='td-rate')
    valute = []
    spisok = []
    for i in valutes:
        b = i.find('div', class_='td-rate__wrp').text
        valute.append(b.replace(' ','').replace('\n', '').replace('—',''))
    for x in valute[:8]:
        spisok.append(x)
    # r = open('test.txt', 'w') запись курсов всех валют из всех банков в файл
    # r.write(str(valute))
    # print(valute)
    return spisok

def main():
    url = 'http://valuta.kg/'
    all_links = get_links(get_html(url))
    return all_links
    
main()