from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from extract import *
import os
from enum import Enum

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

@app.get("/servicos/{model_service}")
async def get_service(model_service: ModelService, cadernos: str | int = 0, secoes: str | int = 0):
    print(ModelService, model_service)
    if model_service is ModelService.consulta:
        return {
                "this is consult ...": model_service,
                "cadernos": cadernos,
                "secoes": secoes
                }
#def post ...
@app.post("/backgroundDemo")
async def demo_post(inp: Msg, background_tasks: BackgroundTasks):
    
    background_tasks.add_task(doBackgroundTask, inp)
    return {"message": "Success, background task started"}

