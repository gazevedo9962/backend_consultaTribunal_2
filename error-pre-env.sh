#!/usr/bin/bash

# Atualizar o sistema e instalar ferramentas de desenvolvimento
sudo apt-get update
sudo apt-get install build-essential python3-dev
# Ativar um ambiente virtual
source venv/bin/activate
# Atualizar pip 
pip install --upgrade pip
# Instalar PyYAML usando binários para evitar compilação do código-fonte
pip install --only-binary :all: PyYAML
# Instalar outras dependências
pip install fastapi uvicorn selenium
# Rodar o servidor Uvicorn
uvicorn main:app --reload
