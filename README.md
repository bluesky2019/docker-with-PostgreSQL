# docker-with-PostgreSQL


##Funcionalidades do Script:

Gerenciamento de Container:

Cria um novo container ou utiliza um existente

Persistência de dados com volume Docker

Configuração automática de usuário/senha

Acesso ao PostgreSQL:

Shell interativo via psql

Credenciais padrão:

Usuário: postgres

Senha: senha123

Banco padrão: postgres

Operações Disponíveis:

Criar um novo banco de dados:
sql

CREATE DATABASE meu_banco;
Conectar a um banco:
sql
\c meu_banco

Criar tabelas:
sql
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    data_cadastro DATE DEFAULT CURRENT_DATE
);

Inserir dados:
sql
INSERT INTO clientes (nome, email) 
VALUES ('João Silva', 'joao@empresa.com');

Consultas:
sql
SELECT * FROM clientes;
Sair do shell:
sql
\q

Como Personalizar:
Para alterar credenciais, modifique as variáveis de ambiente no comando docker run:

python
"-e", "POSTGRES_PASSWORD=nova_senha",
"-e", "POSTGRES_USER=novo_usuario",
Para mapear porta diferente:

python
"-p", "5433:5432",  # Porta host:container
Para configurações adicionais, crie um arquivo postgresql.conf e monte no container:

python
"-v", "c:/caminho/para/postgresql.conf:/etc/postgresql/postgresql.conf",
Este script fornece controle total sobre seu ambiente PostgreSQL em container Docker, com persistência de dados e acesso completo ao SGBD.



## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://medium.com/@gilnei809/gilnei-azambuja-borges-analista-de-dados-e-administrador-de-banco-de-dados-8774175b0e46)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gilnei-azambuja-borges-1a83432b)
[![HUGGING FACE](https://img.shields.io/badge/HuggingFace-e5f21d?style=for-the-badge&logo=HuggingFace&logoColor=yellow)](https://huggingface.co/bluesky2019)
[![KAGGLE](https://img.shields.io/badge/Kaggle-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://www.kaggle.com/gilneiborges)


Se você gostou das minhas postagens e gostaria de contribuir com uma pequena doação, eu agradeceria! Tenha uma ótima semana. Siga meu link para os valores em dólares no PAYPAL: https://www.paypal.com/donate/?hosted_button_id=FW4VNKJWXLTCJ
