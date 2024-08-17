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

```
scp.exe .\ping.tcl admin@devnetsandboxiosxe.cisco.com:ping.tcl
```

Executar o script:
```
tclsh flash:ping.tcl
```



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
action 6.0 syslog msg "Porque a int loop10 foi desativada?
!
end
!
```