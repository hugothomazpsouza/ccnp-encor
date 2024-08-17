# Especifica qual versão do Python será usada
#!/usr/bin/env python3

# Importa o módulo requests, que lida com cabeçalhos HTTP e dados de formulários
import requests

# Desabilita avisos sobre certificados autoassinados
requests.packages.urllib3.disable_warnings()

# Credenciais
USER = 'admin'
PASS = 'C1sco12345'

# URL para a solicitação GET. A variável url contém o endpoint RESTCONF ao qual a solicitação GET será enviada.
url = "https://devnetsandboxiosxe.cisco.com/restconf/data/ietf-interfaces:interfaces"

'''Define yang+json como os formatos de dados. Os cabeçalhos Content-Type e Accept 
são configurados para indicar que a solicitação e a resposta 
usarão o formato yang-data+json'''
headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}

'''Executa a solicitação GET. A função requests.get envia a solicitação GET para o 
endpoint especificado. As credenciais de autenticação são passadas usando a 
tupla (USER, PASS). O parâmetro verify=False desabilita a verificação do 
certificado SSL/TLS, o que é necessário devido ao uso de um certificado autoassinado.'''
response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False)

# Imprime os resultados. O código de status HTTP da resposta e o corpo da resposta são impressos no console.
print('Status Code:' + str(response.status_code))
print('Response Text:' + response.text)