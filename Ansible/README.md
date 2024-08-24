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

# Exemplo de Playbook Ansible para Configurar uma Interface Loopback

Crie um arquivo chamado configure_loopback.yml com o seguinte conteúdo:

```yaml
---
- name: Configure Loopback interface on Cisco router
  hosts: cisco_routers
  gather_facts: no
  connection: network_cli
  tasks:
    - name: Configure Loopback interface
      cisco.ios.ios_config:
        lines:
          - interface Loopback150
          - ip address 192.168.150.1 255.255.255.255
          - description Loopback interface for management
        # Optional: Use `match` to control how Ansible checks the current configuration
        match: line
```

Descrição das Linhas
---
Marca o início do arquivo YAML.

- name: Configure Loopback interface on Cisco router
Nome do playbook, descrevendo a configuração de uma interface Loopback em um roteador Cisco.

hosts: cisco_routers
Define o grupo de hosts onde o playbook será executado. O grupo cisco_routers deve estar definido no seu arquivo de inventário (hosts).

gather_facts: no
Indica que não deve coletar informações adicionais sobre os hosts antes de executar as tarefas.

connection: network_cli
Especifica o método de conexão a ser usado para dispositivos de rede. network_cli é o método correto para dispositivos Cisco IOS.

tasks:
Inicia a seção onde as tarefas são definidas.

- name: Configure Loopback interface
Nome da tarefa que configura a interface Loopback.

cisco.ios.ios_config:
O módulo usado para aplicar configurações em dispositivos Cisco IOS.

lines:
Define as linhas de configuração que serão aplicadas ao dispositivo. Neste caso, são as configurações para a interface Loopback.

interface Loopback0
Seleciona a interface Loopback 0 para configuração.

ip address 192.168.1.1 255.255.255.0
Define o endereço IP e a máscara de sub-rede para a interface Loopback.

description Loopback interface for management
Adiciona uma descrição para a interface Loopback.

#Optional: Use match to control how Ansible checks the current configuration
Comentário opcional. O parâmetro match pode ser usado para definir como o Ansible verifica a configuração atual. Usar match: line pode ser útil para garantir que o Ansible reconheça mudanças na configuração existente.





# Script Ansible que execute o comando show ip interface brief em um roteador

- Crie um arquivo chamado show_ip_interface_brief.yml com o seguinte conteúdo:

```yaml
---
- name: Execute 'show ip interface brief' on Cisco router
  hosts: cisco_routers
  gather_facts: no
  connection: network_cli
  tasks:
    - name: Run 'show ip interface brief'
      cisco.ios.ios_command:
        commands:
          - show ip interface brief
      register: command_output

    - name: Display command output
      debug:
        msg: "{{ command_output.stdout[0] }}"
...
```

Descrição das Linhas
---
Marca o início do arquivo YAML, indicando que este é um documento YAML.

- name: Execute 'show ip interface brief' on Cisco router
Nome do playbook, descrevendo que ele executará o comando show ip interface brief em um roteador Cisco.

hosts: cisco_routers
Define o grupo de hosts onde o playbook será executado. O grupo cisco_routers deve estar definido no seu arquivo de inventário (hosts).

gather_facts: no
Indica que não deve coletar informações adicionais sobre os hosts antes de executar as tarefas.

connection: network_cli
Especifica o método de conexão a ser usado para dispositivos de rede. network_cli é o método correto para dispositivos Cisco IOS.

tasks:
Inicia a seção onde as tarefas são definidas.

- name: Run 'show ip interface brief'
Nome da tarefa que executará o comando no roteador Cisco.

cisco.ios.ios_command:
O módulo usado para enviar comandos para o dispositivo Cisco. O parâmetro commands recebe uma lista de comandos a serem executados.

commands:
Lista dos comandos que serão executados no dispositivo. Neste caso, contém o comando show ip interface brief.

register: command_output
Armazena a saída do comando na variável command_output.

- name: Display command output
Nome da tarefa que exibirá a saída do comando.

debug:
Módulo usado para exibir mensagens de depuração.

msg: "{{ command_output.stdout[0] }}"
Mensagem exibida pelo módulo debug, mostrando a saída do comando. stdout[0] refere-se à saída do primeiro comando na lista de comandos executados.




# ###################################################

# Aqui estão alguns exemplos de comandos para cada uma das ferramentas do Ansible mencionadas:


-O comando ansible é usado para executar comandos diretamente em um ou mais hosts gerenciados.
Exemplo:
```
ansible all -i hosts -m ping
```
all: Aplica o comando a todos os hosts definidos no arquivo hosts.
-i hosts: Especifica o arquivo de inventário.
-m ping: Usa o módulo ping para verificar a conectividade com os hosts.


- ansible-playbook
O comando ansible-playbook é usado para executar playbooks, que são arquivos YAML contendo uma série de tarefas a serem executadas em hosts gerenciados.

Exemplo:
```
ansible-playbook -i hosts set_hostname.yml
```
-i hosts: Especifica o arquivo de inventário.
set_hostname.yml: O arquivo de playbook a ser executado.

- ansible-doc
O comando ansible-doc é usado para visualizar a documentação dos módulos e plugins do Ansible.

Exemplo:
```
ansible-doc cisco.ios.ios_config
```
cisco.ios.ios_config: O módulo para o qual você deseja ver a documentação.

- ansible-pull
O comando ansible-pull é usado para puxar e executar um playbook de um repositório de controle remoto em um nó cliente.

Exemplo:
```
ansible-pull -U https://github.com/username/repository.git playbook.yml
-U https://github.com/username/repository.git: URL do repositório Git onde o playbook está armazenado.
playbook.yml: O arquivo de playbook a ser executado.
```

- ansible-vault
O comando ansible-vault é usado para criar, editar, e acessar arquivos criptografados com o Ansible Vault.

Exemplos:
- Criar um novo arquivo criptografado:
```
ansible-vault create secrets.yml
```
Você será solicitado a inserir uma senha para criptografar o arquivo.

- Editar um arquivo criptografado:
```
ansible-vault edit secrets.yml
```

- Descriptografar um arquivo:
```
ansible-vault decrypt secrets.yml
```

- Visualizar o conteúdo de um arquivo criptografado:
```
ansible-vault view secrets.yml
```

