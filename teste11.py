import json

with open("./dados/json/cadernos.json") as arquivo1:
    cadernos = json.load(arquivo1)
with open("./dados/json/secao.json") as arquivo2:
    secoes = json.load(arquivo2)  
data = { "list_cadernos": cadernos[int(0)], "list_secoes": secoes[int(0)] }

print(data)