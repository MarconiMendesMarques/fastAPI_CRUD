import databases
import sqlalchemy


userPostgres = 'postgres'
passworldPostgres = 'marc1307'
host = 'localhost'
bdname = 'postgres'

bdUsuariosURL = "postgresql+asyncpg://" + userPostgres + ":" + passworldPostgres + "@" + host + "/" + bdname

metadata = sqlalchemy.MetaData()
database = databases.Database(bdUsuariosURL)
