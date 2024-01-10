from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from extract import *
import os
from enum import Enum
from typing import Union
import json

SECRET = os.getenv("SECRET")
app = FastAPI()

#def class ...
class Msg(BaseModel):
    msg: str
    secret: str

class ModelService(str, Enum):
    consulta = "consulta"

#def get ...
@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}

@app.get("/homepage")
async def demo_get():
    driver=createDriver()
    homepage = getGoogleHomepage(driver)
    driver.close()
    return homepage

@app.get("/tjsp-teste")
async def get_tjsp_teste():
    driver=createDriver()
    data = getTjsp_teste(driver)
    driver.close()
    return data

@app.get("/tjsp/servicos/{model_service}")
async def get_service(model_service: ModelService, cadernos: Union[str, int] = 0, secoes: Union[str, int] = 0 ):
    options_values = {
                "cadernos": cadernos,
                "secoes": secoes
                }
    driver=createDriver()
    data = getTjsp_teste(driver, options_values)
    driver.close()    
    #json.dumps(data, indent=4, sort_keys=True)
    return data

@app.get("/tjsp/cadernos")
async def get_cadernos():
    with open("./dados/cadernos.json", 'r',  -1, "utf-8") as arquivo2:
        dados_cadernos = json.load(arquivo2)        
    #json.dumps(data, indent=4, sort_keys=True)
    return dados_cadernos

#def post ...
@app.post("/backgroundDemo")
async def demo_post(inp: Msg, background_tasks: BackgroundTasks):
    
    background_tasks.add_task(doBackgroundTask, inp)
    return {"message": "Success, background task started"}


