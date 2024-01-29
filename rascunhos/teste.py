import json
with open("./dados/cadernos.json") as arquivo:
    dados = json.load(arquivo)
    print( dados[0] )