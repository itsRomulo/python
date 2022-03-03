import requests
import time 

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
   
    #for i in results['result']:
    #    first_name = i['message']['chat']['first_name']
    #    chat_id = i['message']['chat']['id']
    #    last_update_id = i['update_id']
    #    message = (i['message']['text'])



send_msg("Teste")

    