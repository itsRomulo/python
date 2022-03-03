import requests
from time import sleep 



def send_msg(text):
    token = "(TOKEN DO SEU BOT DO TELEGRAM)"
    chat_id1 = "(SUA CHAT ID)" 
    

    url_req = "https://api.telegram.org/bot"+ token +"/sendMessage" + "?chat_id=" + chat_id1 + "&text="+text 
    
    results = requests.get(url_req)
   
    print(results.json())
    
cont = 1
while cont < 100:     
    if cont < 100:
        cont =+ 1
        
       
        send_msg('MENSAGEM PARA RECEBER NO TELEGRAM')
        sleep(3600)
        
