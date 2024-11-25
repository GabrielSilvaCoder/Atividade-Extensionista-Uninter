Este projeto foi desenvolvido em Django e contém as instruções para rodar a aplicação.
Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas no sistema:

    Python (recomendado: versão 3.8 ou superior)
    pip (gerenciador de pacotes do Python)
    Ambiente virtual configurado (venv)

Como rodar a aplicação localmente

1. Configure o ambiente virtual

    Linux/Mac: Execute no terminal:

    source venv/bin/activate

Windows: Execute no terminal:

    venv\Scripts\activate

2. Instale as dependências

    pip install -r requirements.txt

3. Configure o banco de dados

Crie as tabelas no banco de dados com o comando:

    python manage.py migrate

4. Inicie o servidor

Para iniciar o servidor local, execute:

    python manage.py runserver

5. Acesse a aplicação

Abra o navegador e acesse o endereço:   http://127.0.0.1:8000/

6. (Opcional) Crie um superusuário

Caso o houver interesse na área administrativa da aplicação

    python manage.py createsuperuser

Acesse através do endereço:     http://127.0.0.1:8000/admin