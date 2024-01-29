import re
import os
from teste9 import split_interval

def echo_mensagem(mensagem):
		print(f"\
################################################################\n\
################################################################\n\
################################################################\n\
##################### {mensagem} ##########################\n\
################################################################\n\
################################################################\n\
################################################################")

def echo_array(array,mensagem):
	os.system("clear;")
	echo_mensagem("Exibindo o array")
	for e in array:
			print("************************************************************************\n")
			print(f"----> {e} ///\n")
			print("************************************************************************")
	echo_mensagem("Fim da Exibição")			

string_cobaia = "0000304-29.2022.8.26.0260 (processo principal 1017296- 76.2021.8.26.0068) - Cumprimento de sentença -\
 Sucumbenciais - Prevsaude Comercial de Prod. e de Benefic. de F armacia Ltda - \
Prevsaude Serviços Médicos Ltda. - Regularize  \
o executado o recolhimento das custas finais remanescentes, ten do em vista o valor mínimo legal (5 Ufesps, conforme art. 4º, \
§ 1º, da Lei nº 11.608/2003), no valor total de R$ 176,80, para  janeiro/2024. -"

string_cobaia_2 = "Processo 1023883-97.2022.8.26.0224 - Procedimento Comum Cível -  Perdas e Danos - Caio Miranda Rocha Bertolotti \n- Anna Carolina Lopez Perez Candido e outro - Anna Carolina Lop ez Perez Candido e outro - Caio Miranda Rocha Bertolotti - \
Vistos. Fls. 1382/1383: Providencie a z. Serventia a certificaç ão do recolhimento das custas iniciais devidas em razão do pedi do \
reconvencional, na forma estabelecida na decisão de fls. 1382/1 383. Sem prejuízo, providencie a z. Serventia a certificação do  \
recolhimento das custas iniciais da ação principal. Após, torne m os autos conclusos para saneamento. Int. e Dil. - ADV: PAULO \
CÉSAR DREER (OAB 179178/SP), PAULO CÉSAR DREER (OAB 179178/SP),  KATHERINE BEZERRA COSTOYA (OAB 408820/\
SP), KATHERINE BEZERRA COSTOYA (OAB 408820/SP), KATHERINE BEZER RA COSTOYA (OAB 408820/SP), KATHERINE \
BEZERRA COSTOYA (OAB 408820/SP)\
JUÍZO DE DIREITO DA 2ª VARA REGIONAL DE COMPETÊNCIA EMPRESARIAL  E DE CONFLITOS RELACIONADOS À \
ARBITRAGEM\
JUIZ(A) DE DIREITO ANDRÉA GALHARDO PALMAESCRIVÃ(O) JUDICIAL LÍDIA SATSUKI HONKE YANOEDITAL DE INTIMAÇÃO DE PARTES E ADVOGADOS\
RELAÇÃO Nº 0035/2024"

print(string_cobaia_2.split())
p = re.compile('[.]*[\w\s\d\,\-,\.,\(\)]+[.]*')
p_text = re.compile('[\w\s\d\,\-\.]+')
p_traço = re.compile('[\s]{1}-[\s]{1}')
p_processo = re.compile('\d+[-]{1}\d{2}\.{1}\d{4}\.{1}\d{1}\.{1}\d{2}\.{1}\d{4}')
p_OAB_1 = re.compile('\(\w{3} \d{6}\/{1}\w{2}\)\w*')
p_OAB_2 = re.compile('\d{6}\/{1}\w{2}\)\w+')
echo_array(re.findall(p_processo, string_cobaia_2), "split regex")
echo_array(re.findall(p_OAB_2, string_cobaia_2), "split regex")
#print(re.match(p_processo, string_cobaia))
#print(re.search(p_processo, string_cobaia).group())
def get_Processo(processo_old):
	s_ini = re.search(p_processo, processo_old).group()
	s_final = re.findall(p_OAB_2, processo_old)[ len(re.findall(p_OAB_2, processo_old)) - 1 ]
	def convert(match_obj):
		return re.search("(\d{6}\/{1}\w{2}\))", match_obj.group()).group()
	print(f"Este é o Processo: {s_ini}")
	print(f"\
		|\n\
		|\n\
		v")
	print(re.sub('(\d{6}\/{1}\w{2}\)\w+)', convert, split_interval(s_ini, s_final, processo_old)))

	e_processo = re.sub('(\d{6}\/{1}\w{2}\)\w+)', convert, split_interval(s_ini, s_final, processo_old))
	for e_processo in e_processo.split(" - "):
			e_processo_semquebras = re.sub('\n', '', e_processo)
			print("-------------------------------------------------------------------------------------------------------------------")
			print("-------------------------------------------------------------------------------------------------------------------")
			print("-------------------------------------------------------------------------------------------------------------------")
			if e_processo_semquebras != "":
				print(f"Instância:\n{e_processo_semquebras}")
			print("-------------------------------------------------------------------------------------------------------------------")
			print("-------------------------------------------------------------------------------------------------------------------")
			print("-------------------------------------------------------------------------------------------------------------------")

print(string_cobaia_2)
get_Processo(string_cobaia_2)
#rascunho
#print(re.fullmatch(p, string_cobaia))
#print(re.search(p, string_cobaia))
#print(re.search('.+\s-\s.+', string_cobaia))
#print(re.split(r'[\s]{1}-[\s]{1}', string_cobaia))
#re.search(' - \d+', '21544message65465465 - awdasdfa - asdas - 1212312')
#echo_array(re.split(p_traço, string_cobaia), "split regex")
#m.group()
#print(re.search(' - \d+', '21544message65465465 - awdasdfa - asdas - 1212312')) 
'''
for e in re.findall(p,string_cobaia):
	print('-------------------------------------------------------------------')
	print(e)
	print('-------------------------------------------------------------------')
'''	
'''
print(f"Esta é a palavra final:")
print(f"\
	|\n\
	|\n\
	v")
print(re.sub('(\d{6}\/{1}\w{2}\)\w+)', convert, s_final))
'''
#s_sub = re.search("\d{6}\/{1}\w{2}\)", s_final).group()