# Linux, TCL and EEM scripts directly on Cisco IOS

Para entrar no mode tcl, digite:

```
tclsh
```

Para entrar no mode tcl, digite:

```
tclquit
```

Ping scrit
```
foreach ipaddr {
10.10.20.48
10.0.0.1
192.168.1.1
} {ping $ipaddr}
```

Copiar para dentro da flash e executar dentro do dispositivo

Abrir powershell e transferir via scp:

Copiar da máquina para o router. Exemplo:
```
scp.exe .\ping.tcl admin@devnetsandboxiosxe.cisco.com:ping.tcl
```

Copiar do router para o máquina. Exemplo:
```
scp.exe admin@devnetsandboxiosxe.cisco.com:flash:/packages.conf .
```

Executar o script:
```
tclsh flash:ping.tcl
```

Documentação: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ios_tcl/configuration/12-4t/ios-tcl-12-4t-book/nm-script-tcl.html


# Embedded Event Manager (EEM) 
```
!
event manager applet loopbacl10_down
event syslog pattern "1 interface Lo10 line-protocol Up -> Down" period 1
action 1.0 cli command "enable"
action 2.0 cli command "config terminal"
action 3.0 cli command "interface loopback10"
action 4.0 cli command "shutdown"
action 5.0 cli command "no shutdown"
action 6.0 syslog msg "A Int loop10 foi desativada, mas ativamos novamente"
!
end
!
```

Habilitar o Debug

```
!
debug event manager action cli
!
```

Evento de ping
```
event manager applet PingTest
 event none
 action 1.0 cli command "enable"
 action 2.0 cli command "ping 192.168.0.1 repeat 2"
 action 2.1 regexp "Success rate is ([0-9]+) percent" "$_cli_result" match rate1
 action 2.2 if $rate1 ge 50
 action 2.3  puts "Ping to 192.168.0.1: SUCCESS"
 action 2.4 else
 action 2.5  puts "Ping to 192.168.0.1: FAILED"
 action 2.6 end
 action 3.0 cli command "ping 192.168.0.2 repeat 2"
 action 3.1 regexp "Success rate is ([0-9]+) percent" "$_cli_result" match rate2
 action 3.2 if $rate2 ge 50
 action 3.3  puts "Ping to 192.168.0.2: SUCCESS"
 action 3.4 else
 action 3.5  puts "Ping to 192.168.0.2: FAILED"
 action 3.6 end
 action 4.0 cli command "ping 192.168.0.3 repeat 2"
 action 4.1 regexp "Success rate is ([0-9]+) percent" "$_cli_result" match rate3
 action 4.2 if $rate3 ge 50
 action 4.3  puts "Ping to 192.168.0.3: SUCCESS"
 action 4.4 else
 action 4.5  puts "Ping to 192.168.0.3: FAILED"
 action 4.6 end
 action 5.0 cli command "ping 192.168.0.4 repeat 2"
 action 5.1 regexp "Success rate is ([0-9]+) percent" "$_cli_result" match rate4
 action 5.2 if $rate4 ge 50
 action 5.3  puts "Ping to 192.168.0.4: SUCCESS"
 action 5.4 else
 action 5.5  puts "Ping to 192.168.0.4: FAILED"
 action 5.6 end
 !
 end
 !
 !Executar evento
 event manager run PingTest
 !
 ```

Documentação: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/eem/configuration/xe-16/eem-xe-16-book.html


#Linux Shell Script:

Habilitar (in enable mode)
```
terminal shell
```

Teste direto no shell:
```
for x in 1 2 3 4
do
ping 192.168.0.$x
done
```

Create a Function
```
function testecho(){
  echo 192.168.0.1
  echo 192.168.0.2
  echo 192.168.0.3
  echo 192.168.0.4
}
```
```
function testping(){
  ping 192.168.0.1 repeat 2
  ping 192.168.0.2 repeat 2
  ping 192.168.0.3 repeat 2
  ping 192.168.0.4 repeat 2
}
```

Mudar descrição da interface
```
function set_interface_description () {
    configure terminal
        interface $1
            description $2
    end
}
```


Visualizar as function creadas
```
show shell functions
```

Documentação: https://www.cisco.com/c/en/us/td/docs/ios/netmgmt/configuration/guide/Convert/IOS_Shell/nm_ios_shell.html
