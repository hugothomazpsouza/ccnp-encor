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

```
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

Execute o Playbook:

No terminal, execute o seguinte comando para aplicar a configuração:

```
ansible-playbook -i hosts set_hostname.yml
```