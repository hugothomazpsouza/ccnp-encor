import json

with open("user.json", "r") as json_file: 
    json_file_content = json.load(json_file)

print(json_file_content)

print('##################################################')

# Abre o arquivo user.json e carrega o conteúdo
with open('user.json', 'r') as file:
    users = json.load(file)

# Imprime as informações do usuário com id 10 diretamente
for user in users:
    if user['id'] == 10:
        print("Informações do usuário com ID 10:")
        print(f"Nome: {user['nome']}")
        print(f"Idade: {user['idade']}")
        print(f"Email: {user['email']}")
        break
