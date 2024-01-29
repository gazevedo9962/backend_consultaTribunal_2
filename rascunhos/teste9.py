string_cobaia = "0000304-29.2022.8.26.0260 (processo principal 1017296- 76.2021.8.26.0068) - Cumprimento de sentença -\
 Sucumbenciais - Prevsaude Comercial de Prod. e de Benefic. de F armacia Ltda - \
Prevsaude Serviços Médicos Ltda. - Regularize  \
o executado o recolhimento das custas finais remanescentes, tendo em vista o valor mínimo legal (5 Ufesps, conforme art. 4º, \
§ 1º, da Lei nº 11.608/2003), no valor total de R$ 176,80, para  janeiro/2024. -"
def split_interval(s_inicial, s_final, string):
	s_inicial = s_inicial
	s_final = s_final
	permissao_iteration = False
	string_iteration=""
	for e in string.split():
		#print(e)
		index = string.index(e)
		if permissao_iteration:
			string_iteration = string_iteration + " " + e
		if e == s_inicial:
			permissao_iteration = True	
		if e == s_final and permissao_iteration:
			permissao_iteration = False
			break	

	return string_iteration			

print(split_interval("Regularize","-",string_cobaia))		
print(string_cobaia.split())