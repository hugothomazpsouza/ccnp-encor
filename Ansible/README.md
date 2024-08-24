#Passos para Instalar o Ansible no Ubuntu:
##Atualize o sistema:

- Abra o terminal e execute:
```
sudo apt update
Instale o Ansible:
```

- Instale o Ansible e suas dependências:

```
sudo apt install ansible -y
```

- Instale o Python e a Biblioteca paramiko:

O Ansible usa o SSH para gerenciar dispositivos, e paramiko é uma biblioteca Python necessária para conectar-se aos roteadores via SSH.

```
sudo apt install python3-pip -y
pip3 install paramiko
```

- Instale a coleção Ansible para Cisco:

Ansible possui módulos específicos para Cisco, que podem ser instalados com o comando abaixo:

```
ansible-galaxy collection install cisco.ios
```

# Script Ansible para Configurar o Hostname em um Roteador Cisco:

- Crie o Arquivo de Inventário:

Crie um arquivo chamado hosts que contém o IP do roteador e as informações de autenticação:

```
[cisco_routers]
router1 ansible_host=devnetsandboxiosxe.cisco.com ansible_user=admin ansible_password=C1sco12345 ansible_network_os=ios ansible_connection=network_cli
```

- Escreva o Playbook Ansible:

Crie um arquivo chamado set_hostname.yml com o seguinte conteúdo:

```yaml
---
- name: Configure hostname on Cisco router
  hosts: cisco_routers
  gather_facts: no
  tasks:
    - name: Set hostname
      cisco.ios.ios_config:
        lines:
          - hostname Router-123
...
```

Descrição das Linhas
---
Marca o início do arquivo YAML. Esse cabeçalho é opcional, mas ajuda a garantir que o arquivo seja interpretado corretamente.

- name: Configure hostname on Cisco router
Define o nome do play, que descreve a ação que será realizada. Neste caso, o playbook está configurando o hostname em um roteador Cisco.

hosts: cisco_routers
Especifica o grupo de hosts definidos no arquivo de inventário onde o playbook será executado. cisco_routers é o grupo de roteadores Cisco.

gather_facts: no
Define se o Ansible deve coletar informações detalhadas sobre os hosts antes de executar as tarefas. no indica que não deve coletar essas informações.

tasks:
Inicia a seção onde as tarefas são definidas. Cada tarefa é uma ação que o Ansible deve realizar.

- name: Set hostname
Nome da tarefa específica. Fornece uma descrição do que a tarefa faz. Neste caso, está configurando o hostname.

cisco.ios.ios_config:
Especifica o módulo Ansible a ser usado para essa tarefa. cisco.ios.ios_config é o módulo para aplicar configurações em dispositivos Cisco IOS.

lines:
Define as linhas de configuração que serão aplicadas no dispositivo. As linhas são especificadas abaixo.

- hostname Router-123
Linha de configuração específica que será aplicada ao roteador, definindo o hostname como Router-123.

Execute o Playbook:

No terminal, execute o seguinte comando para aplicar a configuração:

```
ansible-playbook -i hosts set_hostname.yml
```