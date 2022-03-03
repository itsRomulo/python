import json
import requests

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
    



def monitorpa():

    dados = json.dumps({
 
  "agente": "agente_001"
  
})
    headers = {'Content-Type':'application/json'}
    
    

    
    results = requests.post("http://3.229.194.219:9094/api/agendamento/monitor_pa", headers=headers, data=dados)
    
    resultado = results.json()

    
    return resultado



send = monitorpa()
for i in send['content']:
        print(i['CLI_fgCPC'])
