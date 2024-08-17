# Tutorial Básico de Python para o Exame ENCOR

O exame ENCOR exige que você tenha algum conhecimento básico de Python para processar arquivos, enviar solicitações de API REST e lidar com as respostas. Este tutorial foi projetado para ajudá-lo a entender esses conceitos.

## Compreendendo o Tipo Dicionário em Python

Primeiro, entenda o tipo dicionário em Python:

```python
# Isso cria um objeto Python (tipo dicionário):
data = {
    "nome": "Hugo",
    "idade": 31
}
```

## Trabalhando com o Pacote JSON (import json)

A função `json.dumps()` é usada para converter objetos Python (dicionário, lista, string, inteiro, booleano, etc.) em strings JSON. O nome da função significa "despejar" os dados como uma string, note que o "s" final em "dumps" representa "string". Aqui está um exemplo simples:

```python
import json

data = {'nome': 'Hugo', 'idade': 31}  # Define um dicionário Python
json_data = json.dumps(data)  # Usa json.dumps() para converter o dicionário em uma string JSON
print(json_data)  # Saída: '{"nome": "Hugo", "idade": 25}'
```

## Trabalhando com o Pacote JSON (import json)

A função `json.loads()` converte uma string JSON em um dicionário Python, sendo o oposto de `json.dumps()`. Podemos adicionar este código ao exemplo acima:

```python
import json

# Converte a string JSON em um dicionário Python
dict_obj = json.loads(json_data)
print(dict_obj)  # Saída: {'name': 'John', 'age': 25}
print(type(dict_obj))  # Saída: <class 'dict'>
```

## Mais sobre `json.dumps()`

O método `json.dumps()` é muito poderoso para lidar com estruturas mais complexas. Ele pode gerenciar listas, dicionários aninhados e outros objetos Python complexos com facilidade. Abaixo está outro exemplo de uso de `json.dumps()` para um objeto Python complexo:

```python
import json

# Define um objeto Python complexo
data = {
    'nome': 'Hugo',
    'idade': 31,
    'animais': ['Cachorro', 'Gato'],
    'perfil': {
        'trabalho': 'Network Engineer',
        'cidade': 'João Pessoa'
    }
}

# Usa json.dumps() para converter o objeto em uma string JSON
json_data = json.dumps(data)
print(json_data)
# Saída:
# '{"nome": "Hugo", "idade": 31, "animais": ["Cachorro", "Gato"], "perfil": {"trabalho": "Network Engineer", "cidade": "João Pessoa"}}'
```

## Trabalhando com arquivos JSON (ler e escrever arquivos, converter para string JSON ou objeto Python)

Existem algumas maneiras de manipular um arquivo JSON em Python:

### Ler um arquivo JSON

Podemos usar o método `file.load()` (note: `load`, não `loads`) para ler um objeto de arquivo e fazer o parsing ao mesmo tempo:

```python
import json

with open("user.json", "r") as json_file: 
    json_file_content = json.load(json_file)

print(json_file_content)
```

### Escrevendo em um Arquivo JSON

A função `json.dump()` é semelhante à `json.dumps()`, mas em vez de converter o objeto Python para uma string JSON, ela escreve os dados JSON diretamente em um arquivo.

```python
import json

# Define um dicionário Python
data = {'name': 'Hugo', 'age': 31}

# Usa json.dump() para escrever o dicionário em um arquivo JSON
with open('data.json', 'w') as f:
    json.dump(data, f)

# Verifica o conteúdo do arquivo
with open('data.json', 'r') as f:
    print(f.read())
# Saída:
# '{"name": "Hugo", "age": 31}'
```

## Resumo 

| Método       | Uso                                                                 |
|--------------|---------------------------------------------------------------------|
| `json.loads()` | Recebe uma string JSON e a converte em um dicionário Python          |
| `json.load()`  | Lê um arquivo JSON e o analisa diretamente em um dicionário          |
| `json.dumps()` | Recebe qualquer objeto e o retorna como uma string JSON              |
| `json.dump()`  | Recebe qualquer objeto e escreve diretamente em um arquivo           |






