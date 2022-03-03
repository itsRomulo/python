import requests
from time import sleep 
import os


def send_msg(text,chatid):
    token = "1953843301:AAHZEQDGMmN1jhtoXvgrTK-7NtfZUpepTik"


    url_req = "https://api.telegram.org/bot"+ token +"/sendMessage" + "?chat_id=" + chatid + "&text="+text 
    
 
    results = requests.get(url_req)
    
    print(results.json())
    

#msg = ('Teste')
#idchat = '1116879369'
#send_msg(msg,idchat)
       
        



#<span data-v-72605638="" data-v-e1888a94="" style="color: green;">Group 4 in an hour</span>

 #  chat_id_rom = "1621159417" 
  #  chat_id_jovra = "1116879369" 
  #  url_req2 = "https://api.telegram.org/bot"+ token +"/sendMessage" + "?chat_id=" + chat_id_jovra + "&text="+text '''
#results2 = requests.get(url_req2)