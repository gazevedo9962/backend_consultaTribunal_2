from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Query
from pydantic import BaseModel
from extract import *
import os
from enum import Enum
from typing import Union
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

SECRET = os.getenv("SECRET")
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    tearDown(driver)
    return homepage

@app.get("/tjsp-teste")
async def get_tjsp_teste():
    driver=createDriver()
    data = getTjsp_url(driver)
    tearDown(driver)
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
    data = consulta(driver, options_values)
    tearDown(driver)    
    return data

@app.get("/tjsp/servicos/{model_service}/up_db")
async def get_up_db(request: Request, model_service: ModelService):
    #rasc - func - get_service
    #cadernos: Union[str, int] = 0, secoes: Union[str, int] = 0 
    driver=createDriver()
    data = up_db(driver)
    tearDown(driver)    
    return data    

@app.get("/tjsp/servicos/{model_service}/secoes")
async def get_secoes(request: Request, model_service: ModelService):
    #rasc - func - get_service
    #cadernos: Union[str, int] = 0, secoes: Union[str, int] = 0 
    options_values = {
                "cadernos": request.query_params["cadernos"] or 0,
                "secoes": request.query_params["secoes"] or 0
                }
    with open("./dados/json/cadernos.json") as arquivo:
        cadernos = json.load(arquivo)
    secoes = cadernos[int(options_values["cadernos"])]["secao"] 
    return secoes[int(options_values["secoes"])]

@app.get("/tjsp/servicos/{model_service}/secoes2")
async def get_secoes2(request: Request, model_service: ModelService):
    #rasc - func - get_service
    #cadernos: Union[str, int] = 0, secoes: Union[str, int] = 0 
    options_values = {
                "cadernos": request.query_params["cadernos"] or 0,
                "secoes": request.query_params["secoes"] or 0
                }
    with open("./dados/json/secao.json") as arquivo:
        secoes = json.load(arquivo)
    return secoes[int(options_values["cadernos"])]

@app.get("/tjsp/servicos/{model_service}/cadernos")
async def get_cadernos(request: Request, model_service: ModelService):
    #rasc - func - get_cadernos
    #print(request.query_params["teste"])
    #json.dumps(data, indent=4, sort_keys=True)
    options_values = {
                "cadernos": request.query_params["cadernos"] or 0
                }
    with open("./dados/json/cadernos.json") as arquivo:
        cadernos = json.load(arquivo)
    return cadernos[int(options_values["cadernos"])] 

@app.get("/tjsp/servicos/{model_service}/cadernos_secoes")
async def get_cadernos_secoes(request: Request, model_service: ModelService):
    #rasc - func - get_cadernos
    #print(request.query_params["teste"])
    #json.dumps(data, indent=4, sort_keys=True)
    options_values = {
        "cadernos": request.query_params["cadernos"] or 0,
        "secoes": request.query_params["secoes"] or 0
        }

    with open("./dados/json/cadernos.json") as arquivo1:
        cadernos = json.load(arquivo1)
    with open("./dados/json/secao.json") as arquivo2:
        secoes = json.load(arquivo2)
        
    data = { "list_cadernos": cadernos, "list_secoes": secoes[int(options_values["secoes"])] }
    return data

@app.get("/Downloads/")
async def get_items(request: Request):

       results = {}
       PASTA_ATUAL = "./"
       entry = PASTA_ATUAL + request.query_params["file"] + "/"

       dirs = os.listdir(PASTA_ATUAL)
       # ******************** Pega todas as pastas ********************
       #results["folders"] = [val for val in dirs if os.path.isdir(entry+val)]
       # ********************  Pega todos os arquivos ********************
       #results["files"] = [val for val in dirs if os.path.isfile(PASTA_ATUAL+val) ]
       results["files"] = [val for val in dirs if os.path.isfile(PASTA_ATUAL+val) and val == request.query_params["file"] ]
       #results["path_vars"] = query_items["q"]

       for file in results["files"]:
        print(type(file)) 
        if file == request.query_params["file"]:
            return FileResponse(PASTA_ATUAL+file)
        else:
            return "Nenhum arquivo foi encontrado"
            #return results["files"]

#def post ...
@app.post("/backgroundDemo")
async def demo_post(inp: Msg, background_tasks: BackgroundTasks):
    
    background_tasks.add_task(doBackgroundTask, inp)
    return {"message": "Success, background task started"}


