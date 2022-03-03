import requests
from bs4 import BeautifulSoup

def valuemir4():

    url = "https://www.mir4draco.com/price"

    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}

    site = requests.get(url, headers=headers)

    soup = BeautifulSoup(site.content, 'html.parser')

    #mir4 = (soup.find('span', class_='amount').get_text())
    spans = soup.find_all('span','amount')
    for span in spans:
        print (span.text)
    

print (valuemir4())