# Para criar um contêiner com uma página web, vamos usar Docker. Aqui está um passo-a-passo para criar um contêiner que serve uma página web simples usando um servidor web leve, como o Nginx.

Passos:

1.	Instalar Docker:
- Se você ainda não tem o Docker instalado, siga as instruções no site oficial: Docker Install.
https://docs.docker.com/engine/install/

2.	Criar a estrutura do projeto:

- Crie um diretório para o seu projeto.
```
mkdir web_container
cd web_container
```

3.	Criar a página web:
- Dentro do diretório do projeto, crie um arquivo HTML (index.html) e copie esse código abaixo .
```html
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>My Docker Web Page</title>
</head>
<body>
    <h1>Hello from Docker!</h1>
</body>
</html>
```

4.	Criar um Dockerfile:
- No mesmo diretório, crie um arquivo chamado Dockerfile com o seguinte conteúdo:
```
# Use uma imagem base do Nginx
FROM nginx:alpine

# Copie o arquivo HTML para o diretório padrão de páginas web do Nginx
COPY index.html /usr/share/nginx/html/index.html

# Exponha a porta 80
EXPOSE 80

# Comando para rodar o Nginx
CMD ["nginx", "-g", "daemon off;"]
```

5.	Construir a imagem Docker:
- Execute o comando abaixo para construir a imagem Docker a partir do Dockerfile.
```
docker build -t my-web-container .
```

6.	Executar o contêiner:
- Execute o contêiner usando a imagem que você acabou de construir.
```
docker run -d -p 8080:80 my-web-container
```

7.	Acessar a página web:
- Abra o navegador web e acesse http://localhost:8080. Você deve ver a página web que você criou.

Explicação:
•	Dockerfile:
o	FROM nginx:alpine: Usa a imagem base do Nginx.
o	COPY index.html /usr/share/nginx/html/index.html: Copia o arquivo index.html para o diretório onde o Nginx espera encontrar arquivos web.
o	EXPOSE 80: Expõe a porta 80 do contêiner.
o	CMD ["nginx", "-g", "daemon off;"]: Inicia o Nginx no modo de primeiro plano.
•	Comandos Docker:
o	docker build -t my-web-container .: Constrói a imagem Docker e a marca com o nome my-web-container.
o	docker run -d -p 8080:80 my-web-container: Executa o contêiner em segundo plano (-d) e mapeia a porta 80 do contêiner para a porta 8080 do host.
Esse exemplo cria um contêiner Docker que serve uma página web simples usando o Nginx. Você pode personalizar a página HTML e adicionar mais arquivos conforme necessário.
 
1. Instalação e Verificação
•	Verificar a versão do Docker:
```
docker --version
```
2. Imagens
•	Listar imagens Docker disponíveis localmente:
```
docker images
```

3. Contêineres
•	Listar contêineres em execução:
```
docker ps
```
•	Listar todos os contêineres (em execução e parados):
```
docker ps -a
```

•  Parar um contêiner:
```
docker stop <container_id>
```
•Reiniciar um contêiner:
```
docker restart <container_id>
```
•  Remover um contêiner:
```
docker rm <container_id>
```

Comando para executar comando dentro do docker
```
docker exec -it <container_id_or_name> /bin/bash
```
Exemplos:
```
docker exec -t 62bdf41df160 ls /
docker exec -t 62bdf41df160 ls /usr/share/nginx/html/
docker exec -t 62bdf41df160 cat /usr/share/nginx/html/index.htm
```


- Verificar parte de redes no docker
```
ifconfig 
docker exec -t <container_id_or_name> ifconfig
docker network inspect bridge
```



