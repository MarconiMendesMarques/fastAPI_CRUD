# fastAPI_CRUD

# API

# Instalação

- Baixar o arquivo fastAPI_CRUD.zip
- Descompactar na pasta desejada
- Criar ambiente virtual -> 
  python -m venv <nome_do_ambiente>
- Ativar ambiente criado ->
  source <nome_do_ambiente>/bin/activate (MacOs / Linux) 
- Verificar dependências e apps instalados -> 
  pip freeze (para verificar as dependências e app instalados. Não deve haver nada) 
- Instalar dependências/apps ->
  pip install -r requirements.txt 
- Editar e executar cria_tabelas.py para a criação das tabelas no banco de dados -> python cria_tabelas.py
- Rodar o servidor uvicorn (localhost) ->
  uvicorn main:app 
- No browser -> http://127.0.0.1:8000/docs
