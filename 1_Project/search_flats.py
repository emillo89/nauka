import requests
from bs4 import BeautifulSoup

city = ['Warszawa','Krakow', 'Lodz', 'Wroclaw', 'Poznan', 'Gdansk', 'Szczecin', 'Bydgoszcz', 'Lublin', 'Bialystok']


def parse_price(price):
    return price.replace(' ', '').replace('zł', '')


def parse_page(number):
    print(f'Number {number}')
    URL = 'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/krakow'
    resonse = requests.get(f'{URL}?page={number}')
    content = resonse.text
    soup = BeautifulSoup(content, 'html.parser')
    for offer in soup.find_all('li', class_='css-p74l73'):

        city = offer.find('span', class_='css-17o293g').getText().split(',')[0]
        try:
            area = offer.find('div', class_='css-i38lnz').getText()
        except IndexError:
            area = offer.find('div', class_='css-i38lnz').getText()
        else:
            if 'pokój' in area:
                area = area.replace('pokój', 'pokoje')
            elif 'pokoi' in area:
                area = area.replace('pokoi', 'pokoje')
            area = area.split('pokoje')[1].split(' ')[0]

        price = parse_price(offer.find('span', class_='css-rmqm02').getText())
        rooms = offer.find('div', class_='css-i38lnz').getText().split('m²')[1].split(' ')[0]

        print(f'{city} - {area} - {price} - {rooms}')


for i in range(1,5):
    parse_page(i)









