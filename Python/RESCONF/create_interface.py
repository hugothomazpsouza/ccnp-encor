# Especifica qual versão do Python será usada
#!/usr/bin/env python3

# Importa o módulo requests, que lida com cabeçalhos HTTP e dados de formulários
# Importa o módulo json, que permite trabalhar com dados no formato JSON
import requests
import json

# Desabilita avisos sobre certificados autoassinados
requests.packages.urllib3.disable_warnings()

# Credenciais
USER = 'admin'
PASS = 'C1sco12345'

# URL para a solicitação GET. A variável url contém o endpoint RESTCONF ao qual a solicitação GET será enviada.
url = "https://devnetsandboxiosxe.cisco.com/restconf/data/ietf-interfaces:interfaces"

# Dados do payload para a solicitação POST. O payload contém a configuração da interface a ser enviada no corpo da solicitação.
payload = json.dumps({
  "ietf-interfaces:interface": {
    "name": "Loopback101",
    "description": "Configured by RESTCONF",
    "type": "iana-if-type:softwareLoopback",
    "enabled": True,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "172.16.101.1",
          "netmask": "255.255.255.0"
        }
      ]
    }
  }
})

'''Define yang+json como os formatos de dados. Os cabeçalhos Content-Type e Accept 
são configurados para indicar que a solicitação e a resposta 
usarão o formato yang-data+json'''
headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}

# Executa a solicitação POST. A função requests.request envia a solicitação POST para o 
# endpoint especificado. As credenciais de autenticação são passadas usando a 
# tupla (USER, PASS). O parâmetro verify=False desabilita a verificação do 
# certificado SSL/TLS, o que é necessário devido ao uso de um certificado autoassinado.
response = requests.request('POST', url, auth=(USER, PASS), 
                            headers=headers, data=payload, verify=False)

# Imprime os resultados. O código de status HTTP da resposta e o corpo da resposta são impressos no console.
print('Status Code:' + str(response.status_code))
print('Response Text:' + response.text)