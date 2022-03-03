import requests
import time 
import json

#pip install python-telegram-bot



#TOKEN DO BOT QUE ENVIARÁ AS MENSAGENS
token = "1953843301:AAHZEQDGMmN1jhtoXvgrTK-7NtfZUpepTik"

#REQUISIÇÃO JSON AGENTE DISPONIVEL
def agentedisponivel():

    dados = json.dumps({
  "acao": "agente_disponivel",
  "agente": "agente_001",
  "status": "agente_disponivel"
})
    headers = {'Content-Type':'application/json'}
    
    

    
    results = requests.post("http://3.229.194.219:9094/api/agendamento/agente_disponivel", headers=headers, data=dados)
    
    resultado = results.json()
    print(resultado['result'])
    if ((resultado['result']) == 'agente_001'):
        return "Agente Disponivel"
    else: 
        return "Agente não disponivel"    


#REQUISIÇÃO JSON MONITOR PA
def monitor_pa():

    dados = json.dumps({
  
  "agente": "agente_001"
 
})
    headers = {'Content-Type':'application/json'}
    
    

    
    results = requests.post("http://3.229.194.219:9094/api/agendamento/monitor_pa", headers=headers, data=dados)
    
    resultado = results.json()

    return resultado 




#ENVIO DE MENSAGEM VIA TELEGRAM
def send_msg(text,chat_id):
    
    #chat_id_rom = "1621159417"
    id = chat_id
     

    url_req = "https://api.telegram.org/bot"+ token +"/sendMessage" + "?chat_id=" + str(id) + "&text="+text 
    
    
    results = requests.get(url_req)
    
    print(results.json())
    


#VERIFICA AS MENSAGENS RECEBIDAS
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
                send = first_name +', seja bem vindo ao Bot. Digite /comando para visualizar as funções disponíveis.'
                send_msg(send, chat_id)

            elif "/agentedisponivel" in message:
                send = agentedisponivel()
                send_msg(send, chat_id) 

            elif "/cpc" in message:
                cpc = monitor_pa()
                for i in cpc['content']:
                    send = ("Contato Positivo: "+ str(i['CLI_fgCPC']))
                send_msg(send, chat_id) 

            elif "/marcoudata" in message:
                marcoudata = monitor_pa()
                for i in marcoudata['content']:
                    send = ("Marcou Data: " + str(i['CLI_fgMarcouData']))
                send_msg(send, chat_id)    

            elif "/agendagerada" in message:
                agendagerada = monitor_pa()
                for i in agendagerada['content']:
                    send = ("Gerou Agenda: " + str(i['CLI_fgGeradaAgenda']))
                send_msg(send, chat_id) 

            #elif "/grafico" in message:
                
             #   bot.send_photo
                    
                          

            else :
                send = 'COMANDOS: \n \n /agentedisponivel \n /cpc \n /marcoudata \n /agendagerada'
                send_msg(send, chat_id)        

    return (last_update_id)                





if __name__ == '__main__':
    import time
    update_id = "0"
    while True:
        update_id = get_msg(update_id)
        time.sleep(5)