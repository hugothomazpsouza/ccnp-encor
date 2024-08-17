import json

data = {'nome': 'Hugo', 'idade': 31}  # Define um dicionário Python
json_data = json.dumps(data)  # Usa json.dumps() para converter o dicionário em uma string JSON
print(json_data)  # Saída: '{"nome": "Hugo", "idade": 25}'