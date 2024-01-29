arquivo = open('texto.txt', 'r')

conteudo = arquivo.read()
print(str(conteudo).replace("\n", ""))