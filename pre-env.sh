#!/usr/bin/bash

####################### ANTENÇÃO !!! #########################
# -----------> Caso erro execute o arquivo error-pre-env.sh

PORT=443
apt-get install python3 -y
echo $(python3 -m site --user-base)
apt-get update
apt-get install -y python3-pip
pip install -r requirements.txt  
python3 -m pip install webdriver-manager --upgrade 
python3 -m pip install packaging
python3 -m pip install docker-compose
uvicorn main:app --host 0.0.0.0 --port $PORT


