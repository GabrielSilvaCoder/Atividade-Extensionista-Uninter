Projeto Django - Guia de Execução

Este projeto foi desenvolvido em Django e contém as instruções necessárias para configurar e rodar a aplicação localmente.
Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas no sistema:

    Python (versão 3.8 ou superior recomendada)
    pip (gerenciador de pacotes do Python)
    Ambiente virtual configurado (venv)

Como rodar a aplicação localmente

1. Configurar o ambiente virtual

    Linux/Mac: Execute no terminal:

source venv/bin/activate

Windows: Execute no terminal:

    venv\Scripts\activate

2. Instalar as dependências

Com o ambiente virtual ativado, instale as dependências necessárias:

pip install -r requirements.txt

3. Configurar o banco de dados

Crie as tabelas no banco de dados com o comando:

python manage.py migrate

4. Iniciar o servidor

Para iniciar o servidor local, execute:

python manage.py runserver

5. Acessar a aplicação

Abra o navegador e acesse o endereço:

http://127.0.0.1:8000/

(Opcional) Criar um superusuário

Caso queira acessar a área administrativa da aplicação, crie um superusuário executando:

python manage.py createsuperuser

Acesse a área administrativa pelo endereço:

http://127.0.0.1:8000/admin

