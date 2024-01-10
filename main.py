from fastapi import FastAPI, BackgroundTasks, HTTPException, Request
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
async def get_service(request: Request, model_service: ModelService):
    #rasc - func - get_service
    #cadernos: Union[str, int] = 0, secoes: Union[str, int] = 0 
    options_values = {
                "cadernos": request.query_params["cadernos"] or 0,
                "secoes": request.query_params["secoes"] or 0
                }
    driver=createDriver()
    data = getTjsp_teste(driver, options_values)
    driver.close()    
    return data

@app.get("/tjsp/cadernos")
async def get_cadernos(request: Request):
    #rasc - func - get_cadernos
    #print(request.query_params["teste"])
    #json.dumps(data, indent=4, sort_keys=True)
    if [ open("./dados/cadernos.json", 'r',  -1, "utf-8") ]:
        with open("./dados/cadernos.json", 'r',  -1, "utf-8") as arquivo:
            if [arquivo]:
                dados_cadernos = json.load(arquivo)        
                
    if [ dados_cadernos ]:
        return dados_cadernos
    else:    
        return "Caderno não está definido ... "
    
#def post ...
@app.post("/backgroundDemo")
async def demo_post(inp: Msg, background_tasks: BackgroundTasks):
    
    background_tasks.add_task(doBackgroundTask, inp)
    return {"message": "Success, background task started"}


