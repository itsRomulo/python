import requests
from time import sleep 
import pvuvalue


def send_msg(text):
    token = "1953843301:AAHZEQDGMmN1jhtoXvgrTK-7NtfZUpepTik"
    chat_id_rom = "1621159417"
    chat_id_jovra = "1116879369"

    url_req = "https://api.telegram.org/bot"+ token +"/sendMessage" + "?chat_id=" + chat_id_rom + "&text="+text 
    
    url_req2 = "https://api.telegram.org/bot"+ token +"/sendMessage" + "?chat_id=" + chat_id_jovra + "&text="+text
    results = requests.get(url_req)
    results2 = requests.get(url_req2)
    print(results.json())
    print(results2.json())
cont = 1
while cont < 100:     
    if cont < 100:
        cont =+ 1
        vpvu = (pvuvalue.valorpvu())
        msg = ("Valor do PVU Atual: "+vpvu)
        send_msg(msg)
        sleep(3600)
        



'''<span data-v-72605638="" data-v-e1888a94="" style="color: green;">Group 4 in an hour</span>'''