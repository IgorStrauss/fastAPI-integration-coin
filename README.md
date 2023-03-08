FASTAPI

Aplicação educacional, para aplicação de conceitos adquiridos
nos cursos de Python, fastAPI e Docker.

Dependências:

    Docker

    Docker-compose

    Python-version > 3.8

    Poetry

    Postgres + Pgadmin (docker image)

    API do mercadobitcoin


Conteudo:

    Cadastrar e deletar usuário

    Adicionar e remover ativos favoritos

    Listar usuários e seus ativos favoritos

    Para cada ativo favorito do usuário, mostrar o preço
    máximo e o mínimo do dia anterior (resumo do dia)

Models:

    User:

    id      -   int(pk)
    name    -   string


Favorite:

    id        -   int(pk)
    symbol    -   string
    user_id   -   int(fk)

Caso necessário no momento de startup a aplicação, utilizar:
    export DATABASE_URL=postgresql+asyncpg://admin:admin@localhost:5432/fastapi