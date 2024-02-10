import json
with open("../dados/json/cadernos.json") as arquivo:
    dados = json.load(arquivo)
    print( dados[0] )