import requests
import time 
token = "1953843301:AAHZEQDGMmN1jhtoXvgrTK-7NtfZUpepTik"
import pvuvalue





def send_msg(text,chat_id):
    
    #chat_id_rom = "1621159417"
    id = chat_id
     

    url_req = "https://api.telegram.org/bot"+ token +"/sendMessage" + "?chat_id=" + str(id) + "&text="+text 
    
    
    results = requests.get(url_req)
    
    print(results.json())
    



def get_msg(update_id):

    
    url_get = 'https://api.telegram.org/bot{0}/getUpdates?offset={1}'.format(token, update_id)
    response = requests.get(url_get)
    response_json = (response.json())
    last_update_id = update_id
    for i in response_json['result']:
        first_name = i['message']['chat']['first_name']
        chat_id = i['message']['chat']['id']
        last_update_id = i['update_id']
        message = (i['message']['text'])

        if last_update_id != update_id:
            #COMANDOS
            if (message == 'Oi'):
                send = first_name +', seja bem vindo ao melhor Bot do Mundo.'
                send_msg(send, chat_id)
            
            elif "/pvu" in message:
                
                vpvu = (pvuvalue.valorpvu())
                send = ("Valor do PVU Atual: "+vpvu)
                send_msg(send, chat_id)    
            else :
                send = 'COMANDOS:  \n Oi \n Cecília \n Amor \n Tudo'
                send_msg(send, chat_id)        

    return (last_update_id)                





if __name__ == '__main__':
    import time
    update_id = "936626188"
    while True:
        update_id = get_msg(update_id)
        time.sleep(5)