import requests
from bs4 import BeautifulSoup

def valorpvu():

    url = "https://coinmarketcap.com/pt-br/currencies/plantvsundead/"

    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}

    site = requests.get(url, headers=headers)

    soup = BeautifulSoup(site.content, 'html.parser')

    pvu = (soup.find('div', class_='priceValue').get_text())

    return pvu  

print (valorpvu())