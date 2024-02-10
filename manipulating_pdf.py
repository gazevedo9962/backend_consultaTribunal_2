# importa as bibliotecas necessárias
import PyPDF2
import re
from string_bt import *
from extract import *
import sys

#print(sys.argv)
string_args=cat_string_list(sys.argv)
#path, value_secao = cat_arg("-p", string_args), cat_arg("-vs", string_args)
value_secao = sys.argv[1]
path = sys.argv[2]
pdf_file = open(path, 'rb')

def raspar_pdf_2(path,value_secao):
	#Open PDF
	pdf_file = open(path, 'rb')
	#Read PDF
	read_pdf = PyPDF2.PdfReader(pdf_file)
	#Cat all number pages
	number_of_pages = len(read_pdf.pages)
	#Cat first page
	page = read_pdf.pages[0]
	page_content = page.extract_text()
	#Transform in string
	parsed = ''.join(page_content)
	#value="Subseção V - Intimações de Despachos"
	#print(parsed.split(value_secao))

	echo_all(parsed.split(value_secao))

	#Definindo a seção
	corte=parsed.split(value_secao)[ len(parsed.split(value_secao)) - 1]

	#Analisando se existem processos
	#Caso 1 : " p_processo_1 === 'Processo' "
	if len(re.findall(p_processo_1, corte)) >= 1 and re.findall(p_processo_1, corte):
		print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
		print(re.search(p_processo_1, corte))
		print(re.findall(p_processo_1, corte))
		numeros_processos = re.findall(p_processo_1, corte)
		print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
	#Caso 2 : " p_processo_2 === 'Nº' "
	else:
		print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
		print(re.search(p_processo_2, corte))
		print(re.findall(p_processo_2, corte))
		numeros_processos = re.findall(p_processo_2, corte)
		print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

	#Retirando cada processo existente um por um somente se existem processos 
	#na seção armazenada na váriavel corte
	if numeros_processos:
		total_numeros_processos = len(numeros_processos)
		#Lista onde ficara todos os processos da seção
		list_dados_processos = []
		for n in numeros_processos:
			#index de n
			i = numeros_processos.index(n)
			#Será o numero do processo do qual será retirado da seção
			corte_inicial = corte.replace(n, "#sini")
			elemento = i+1
			if elemento == total_numeros_processos:
				#Será o numero do processo sucessor do qual será retirado da seção
				corte_final = corte_inicial
				#Se o número do processo for o último, então o delimitador final e vazio
				processoOfcorte = split_interval("#sini", "", corte_final)
				#ultimo_elemento_corte_final = corte_final.split()[ len(corte_final.split()) - 1 ]
			else:
				#Será o numero do processo sucessor do qual será retirado da seção
				corte_final = corte_inicial.replace(numeros_processos[i + 1], "#sfin")
				processoOfcorte = split_interval("#sini", "#sfin", corte_final)

			#processoOfcorte = split_interval("#sini", corte_final.split()[ len(corte_final.split()) ], corte_final)
			print(processoOfcorte)
			list_dados_processos.append({ "numero_processo": n, "text": processoOfcorte })

	#Se os dados forem defindos corretamente então exiba eles e retorne os mesmos			
	if list_dados_processos:
		echo_all(list_dados_processos)
		return list_dados_processos
	#Caso contrário a extração dos dados deu errado então,
	#não existem processos
	#ou os padrões p_processo_1 ou p_processo_2 estão errados,
	#ou a seção em questão poder ser uma seção administrativa,
	#tal que os padrões se diferenciam das outras seções
	else:
		print("Não foi possóvel definir os processos\n\
			Alguma coisa deu errado ... ")

    #write("./dados/json/details_pdf.json", list_dados_processos, "json")

'''
	for e_value in value_array:
		index_value = value_array.index(e_value)
		print("************************************************************************************************************************************")
		print("************************************************************************************************************************************")
		
		if e_value:
			for e_parsed in parsed.split():
				index_parsed = parsed.split().index(e_parsed)
				if e_value == e_parsed:
					print("true")
					for e in value_array:
						if e == parsed.split()[ index_parsed + fraction_value ]:
							fraction_value = fraction_value + 1
						else:
							break
				else:
					print("N° não está definido")
    
	if fraction_value == len( value_array ):
			print("Existe a Seção:")
			corte = parsed.split( value_array[ len(value_array) - 1  ] )
			for e in corte:
				print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
				print( e )
				print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
				break

	print("************************************************************************************************************************************")
	print("************************************************************************************************************************************")		
    
	print("-------------------------------------------------------------------------------------------------------------------")
	print("-------------------------------------------------------------------------------------------------------------------")
	print("-------------------------------------------------------------------------------------------------------------------")

	list_dados_processos = []
	if corte:
		print(corte)
	else:
		print("Não foi definido o corte")

	corte = corte[len(corte) - 1 ]
'''
''' 
	#print(corte)
	#notFound_process_Processo = 0

	for e in corte.split("Processo"):
		index = corte.split("Processo").index(e)
		print("************************************************************************************************************************************")
		print("************************************************************************************************************************************")
		print("************************************************************************************************************************************")
		print(f"Elemento {index}")
		if get_Processo(e):
			dados_processo = get_Processo(e)
			print(dados_processo)
			if len(dados_processo["processo"]) <= 3:
				print("Processo não foi gerado corretamente ou não existe")
			else:
				list_dados_processos.append( dados_processo )
		else:
			print("Processo não está definido")
			notFound_process_Processo = index + 1
			print("************************************************************************************************************************************")
			print("************************************************************************************************************************************")
			print("************************************************************************************************************************************")
    
	
	if notFound_process_Processo == len(corte.split("Processo")):
		notFound_process_N = 0
		for e in corte.split("Nº"):
			index = corte.split("Nº").index(e)
		print("************************************************************************************************************************************")
		print("************************************************************************************************************************************")
		print("************************************************************************************************************************************")
		print(f"Elemento {index}")

	if get_Processo(e):
		dados_processo = get_Processo(e)
		print(dados_processo)
		list_dados_processos.append(dados_processo)
	else:
		print("N° não está definido")
		notFound_process_N = index + 1
		
		print("************************************************************************************************************************************")
		print("************************************************************************************************************************************")
		print("************************************************************************************************************************************")		
'''
    

raspar_pdf_2(path,value_secao)

########################### Rascunho #####################################################
'''
def raspar_pdf():
# Abre o arquivo pdf 
# lembre-se que para o windows você deve usar essa barra -> / 
# lembre-se também que você precisa colocar o caminho absoluto
#pdf_file = open('./dados/tmp/pdf/arquivo_6nwa5N.pdf', 'rb')
	string_args=cat_string_list(sys.argv)
	path, value_secao = cat_arg("-p", string_args), cat_arg("-vs", string_args)
	pdf_file = open(path, 'rb')

#Faz a leitura usando a biblioteca
	read_pdf = PyPDF2.PdfReader(pdf_file)

#extrai apenas o texto
	page_content = page.extract_text()

# faz a junção das linhas 
	parsed = ''.join(page_content)
    #value="Subseção V - Intimações de Despachos"
	value=value_secao
    print("-------------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------")
    
    print(parsed.split())
    print(value.split())
    value_array = value.split()
    fraction_value = 0
    
    print("-------------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------")
    
    for e_value in value_array:
		index_value = value_array.index(e_value)
	print("************************************************************************************************************************************")
	print("************************************************************************************************************************************")
	print("************************************************************************************************************************************")
    
	if e_value:
			for e_parsed in parsed.split():
				index_parsed = parsed.split().index(e_parsed)
			if e_value == e_parsed:
					print("true")
				for e in value_array:
						if e == parsed.split()[ index_parsed + fraction_value ]:
							fraction_value = fraction_value + 1
					else:
							break
							else:
								print("N° não está definido")
    
	if fraction_value == len( value_array ):
			print("Existe a Seção:")
		corte = parsed.split( value_array[ len(value_array) - 1  ] )
		for e in corte:
				print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
			print( e )
			print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
				break
    
	print("************************************************************************************************************************************")
	print("************************************************************************************************************************************")
	print("************************************************************************************************************************************")		
    
    print("-------------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------")
    
    list_dados_processos = []
    corte = corte[len(corte) - 1 ]
    print(corte)
    notFound_process_Processo = 0
    
    for e in corte.split("Processo"):
		index = corte.split("Processo").index(e)
	print("************************************************************************************************************************************")
	print("************************************************************************************************************************************")
	print("************************************************************************************************************************************")
	print(f"Elemento {index}")
	if get_Processo(e):
			dados_processo = get_Processo(e)
		print(dados_processo)
		if len(dados_processo["processo"]) <= 3:
				print("Processo não foi gerado corretamente ou não existe")
					else:
				list_dados_processos.append( dados_processo )
				else:
					print("Processo não está definido")
					notFound_process_Processo = index + 1
				print("************************************************************************************************************************************")
				print("************************************************************************************************************************************")
				print("************************************************************************************************************************************")
    
    if notFound_process_Processo == len(corte.split("Processo")):
		notFound_process_N = 0
	for e in corte.split("Nº"):
			index = corte.split("Nº").index(e)
		print("************************************************************************************************************************************")
		print("************************************************************************************************************************************")
		print("************************************************************************************************************************************")
		print(f"Elemento {index}")
		if get_Processo(e):
				dados_processo = get_Processo(e)
			print(dados_processo)
			list_dados_processos.append(dados_processo)
		else:
				print("N° não está definido")
			notFound_process_N = index + 1
		print("************************************************************************************************************************************")
		print("************************************************************************************************************************************")
		print("************************************************************************************************************************************")		
      
    print(list_dados_processos)
    write("./dados/json/details_pdf.json", list_dados_processos, "json")
    
    print("################################################################")
    print("################################################################")
    print("################################################################")
    for e in list_dados_processos:
		print(e)
    print("################################################################")
    print("################################################################")
    print("################################################################")
'''
'''
print(parsed.split("\n"))
print(f"Processso:\n{e}")
	for e_processo in e.split(" - "):
		e_processo_semquebras = re.sub('\n', '', e_processo)
		print("-------------------------------------------------------------------------------------------------------------------")
		print("-------------------------------------------------------------------------------------------------------------------")
		print("-------------------------------------------------------------------------------------------------------------------")
		print(f"Elemento do Processo {index}")
		print(f"Instância:\n{e_processo_semquebras}")
		print("-------------------------------------------------------------------------------------------------------------------")
		print("-------------------------------------------------------------------------------------------------------------------")
		print("-------------------------------------------------------------------------------------------------------------------")

print("-----------------------------------------------------------------------------------------------------")
for e in parsed.split("Nº"):
	index = parsed.split("Nº").index(e)
	print(index)
	print(e)
print("-----------------------------------------------------------------------------------------------------")
for e in parsed.split("Processo"):
	print(e)			
		'''
'''
# pega o numero de páginas
	number_of_pages = len(read_pdf.pages)
	print(number_of_pages)
#lê a primeira página completa
	page = read_pdf.pages[0]
print("####################################################################")
print("####################################################################")
print("####################################################################")
print("##################### Sem eliminar as quebras #####################")
print("####################################################################")
print("####################################################################")
print("####################################################################")
print(parsed)
print("####################################################################")
print("####################################################################")
print("####################################################################")

# remove as quebras de linha
parsed_semquebras = re.sub('\n', '', parsed)
print("##################### Após eliminar as quebras #####################")
print("####################################################################")
print("####################################################################")
print("####################################################################")
print(parsed_semquebras)
print("####################################################################################")
print("####################################################################################")
print("####################################################################################")
print("##################### nPegando apenas as 20 primeiras posições #####################")
print("####################################################################################")
print("####################################################################################")
print("####################################################################################")
novastring = parsed_semquebras[0:20]
print(novastring)
print("################################################################")
print("################################################################")
print("################################################################")
print("##################### PEGANDO OS PROCESSOS #####################")
print("################################################################")
print("################################################################")
print("################################################################")
'''
'''
  print("################################################################")
    print("################################################################")
    print("################################################################")
    for e in list_dados_processos:
		print(e)
    print("################################################################")
    print("################################################################")
    print("################################################################")
'''