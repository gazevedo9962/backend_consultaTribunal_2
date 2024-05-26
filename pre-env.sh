#!/usr/bin/bash

####################### ANTENÇÃO !!! #########################
# -----------> Caso erro execute o arquivo error-pre-env.sh

PORT=443
apt-get install python3 -y
echo $(python3 -m site --user-base)
export PATH="${PATH}:/home/root/.local/bin"
apt-get update
apt-get install -y python3-pip
# Atualizar pip 
python3 pip install --upgrade pip
pip install -r requirements.txt  
python3 -m pip install webdriver-manager --upgrade 
python3 -m pip install packaging
python3 -m pip install docker-compose
# Instalar PyYAML usando binários para evitar compilação do código-fonte
python3 pip install --only-binary :all: PyYAML
# Instalar outras dependências
python3 pip install fastapi uvicorn selenium
uvicorn main:app --host 0.0.0.0 --port $PORT


