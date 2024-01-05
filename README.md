# Introdução:
Projeto desenvolvido para o teste técnico na verzel, decidi criar uma aplicação full stack conforme o que foi pedido com algumas features extras:
Toda a aplicação foi colocada em deploy, mas se preferir pode executar diretamente na sua maquina seguindo o tópico.

## Front-End
  - Repositório: https://github.com/maaxizin25/verzel-cars-front
  - Deploy: https://verzel-cars-front.vercel.app/

## Back-End
  - Documentação URLs: https://www.postman.com/speeding-meadow-554291/workspace/verzel/overview
  - Link Deploy: https://verzel-backend-production.up.railway.app/api
## Figma:
  - Aplicação completa design: https://www.figma.com/file/T23SAjmXtK3C7uIH0HrtbQ/Untitled?type=design&node-id=0%3A1&mode=dev


# Começando com o projeto BACKEND:

## Para iniciar a nossa aplicação serão 7 passos simples:

1. Modificar o arquivo .env-example para rodar o backend localmente com as váriaveis.
  - SECRET_KEY= STRING
  - POSTGRES_DB= NAME YOUR DATABASE
  - POSTGRES_USER= YOUR USER DATABASE
  - POSTGRES_PASSWORD= PASSWORD DATABASE
  - HOST= LOCALHOST or YOUR HOST
  - PORT= PORT OF HOST

2. Instalar o Python, a versão utilizada no projeto está no arquivo runtime.txt: "Python 3.10.12"

3. Criar o arquivo venv para as dependências:
   - Executar no terminal: "python3 -m venv venv"
4. Mudando para a VENV e instalando as dependências:
   - source venv/bin/activate (UBUNTU)
   C:\> <venv>\Scripts\activate.bat (WINDOWS)
5. Instalar as dependências:
    - pip install -r requirements.txt
6. Executar as migrações:
   - Python manage.py makemigrations
   - Python manage.py migrate
7. Executando a aplicação:
   - Python manage.py runserver




