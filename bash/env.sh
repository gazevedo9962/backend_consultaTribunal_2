#!/usr/bin/bash

sudo apt-get install python3 -y
echo $(python3 -m site --user-base)
ENV PATH /home/root/.local/bin:${PATH}
sudo apt-get update 
sudo apt-get install -y python3-pip 
pip install -r requirements.txt  
pip install webdriver-manager --upgrade && pip install packaging
sudo ufw allow http
sudo ufw allow 8000
uvicorn main:app --host 0.0.0.0 --port 8000

