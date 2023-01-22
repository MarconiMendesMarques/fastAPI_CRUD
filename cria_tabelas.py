from typing import Optional

import databases
import ormar
import sqlalchemy

# Preencher os dados de DATABASE_URL e database com a string contendo os dados do banco 
# Exemplo: postgresql_asyncpg://<usuario>:<senha>@<host>/<nome do banco> 

DATABASE_URL = ""
database = databases.Database("")
metadata = sqlalchemy.MetaData()


class Usuario(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "usuarios"

    id: int = ormar.Integer(primary_key=True)
    cpf: str = ormar.String(max_length=14)
    nome: str = ormar.String(max_length=100)
    email: str = ormar.String(max_length=100)
    telefone: str = ormar.String(max_length=50)

engine = sqlalchemy.create_engine(DATABASE_URL)

metadata.drop_all(engine)
metadata.create_all(engine)