# Começando com o projeto BACKEND:

## Para iniciar a nossa aplicação serão 7 passos simples:

1. Modificar o arquivo .env-example para rodar o backend localmente com as váriaveis.
  SECRET_KEY= STRING
  POSTGRES_DB= NAME YOUR DATABASE
  POSTGRES_USER= YOUR USER DATABASE
  POSTGRES_PASSWORD= PASSWORD DATABASE
  HOST= LOCALHOST or YOUR HOST
  PORT= PORT OF HOST

2. Instalar o Python, a versão utilizada no projeto está no arquivo runtime.txt: "Python 3.10.12"

3. Criar o arquivo venv para as dependências:
    Executar no terminal: "python3 -m venv venv"
4. Mudando para a VENV e instalando as dependências:
   source venv/bin/activate (UBUNTU)
   C:\> <venv>\Scripts\activate.bat (WINDOWS)
5. Instalar as dependências:
    pip install -r requirements.txt
6. Executar as migrações:
   - Python manage.py makemigrations
   - Python manage.py migrate
7. Executando a aplicação:
   - Python manage.py runserver


# Aplicação BACKEND

- Documentação com rotas no POSTMAN:
  https://www.postman.com/speeding-meadow-554291/workspace/verzel/overview


# Aplicação FRONT-END:

- Repositório:
  https://github.com/maaxizin25/verzel-cars-front
# Figma:
- Aplicação completa design
https://www.figma.com/file/T23SAjmXtK3C7uIH0HrtbQ/Untitled?type=design&node-id=0%3A1&mode=dev
