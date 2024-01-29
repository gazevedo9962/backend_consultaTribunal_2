import os

teste = os.environ.get('teste')
print(f"teste: {teste}")
#print(os.environ)

os.system("export teste2=2")
teste2 = os.environ.get('teste2')
print(teste2)