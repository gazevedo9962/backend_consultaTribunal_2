#!/usr/bin/python

import re

def cat_string_list(list):
    string = ""
    for value in list:
        string = string + " " + value    
    return string    

def cat_arg(parametro, string_arg):
    array_string = string_arg.split()
    for s in array_string:
        if [ s == parametro ]:
            path = array_string[ array_string.index(parametro) + 1 ]
    return path 

def echo_e(elemento, name):
    print(f"\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&| {name} INI |&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n")
    print(elemento)
    print(f"\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&| {name} FIN |&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n")

def echo_all(array):
    for e in array:
        index = array.index(e)
        print(f"\n-------------------------| Elemento {index} INI |----------------------------------\n")
        print(e)
        print(f"\n-------------------------| Elemento {index} FIN |----------------------------------\n")
    

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

p_text = re.compile('[\w\s\d\,\-\.]+')
p_traço = re.compile('[\s]{1}-[\s]{1}')
p_processo = re.compile('\d+[-]{1}\d{2}\.{1}\d{4}\.{1}\d{1}\.{1}\d{2}\.{1}\d{4}')
p_processo_1 = re.compile('Processo \d+[-]{1}\d{2}\.{1}\d{4}\.{1}\d{1}\.{1}\d{2}\.{1}\d{4} -')
p_processo_2 = re.compile('\n[\w]*[\s]*\d+[-]{1}\d{2}\.{1}\d{4}\.{1}\d{1}\.{1}\d{2}\.{1}\d{4}[\;]*[\s]*[\-]?')
p_OAB_1 = re.compile('\(\w{3} \d{5,6}\/{1}\w{2}\)\w*')
p_OAB_2 = re.compile('\d{5,6}\/{1}\w{2}\)\w*')
p_OAB_3 = re.compile('\(\w{3}\n\d{5,6}\/{1}\w{2}\)\w*')
p_OAB_4 = re.compile('\w{3,4} \d{5,6}\/{1}\w{2}\)\w*')

def get_Processo(processo_old):

    dados_processo = ""
    instancias = []
    numero_processo = ""

    def convert(match_obj):
        return re.search("(\d{6}\/{1}\w{2}\))", match_obj.group()).group()

    def cat_process():
        numero_processo = s_ini        
        print(f"Este é o Processo: {numero_processo}")
        print(f"\
            |\n\
            |\n\
            v")
        print(  re.sub('(\d{6}\/{1}\w{2}\)\w+)', convert, split_interval(s_ini, s_final, processo_old)) )
        text_processo = re.sub('(\d{6}\/{1}\w{2}\)\w+)', convert, split_interval(s_ini, s_final, processo_old))
        for e_processo in text_processo.split(" - "):
                e_processo_semquebras = re.sub('\n', '', e_processo)
                print("-------------------------------------------------------------------------------------------------------------------")
                print("-------------------------------------------------------------------------------------------------------------------")
                print("-------------------------------------------------------------------------------------------------------------------")
                if e_processo_semquebras != "":
                    print(f"Instância:\n{e_processo_semquebras}")
                    instancias.append({"index": e_processo.split(" - ").index(e_processo_semquebras), "instancia": e_processo_semquebras })
                print("-------------------------------------------------------------------------------------------------------------------")
                print("-------------------------------------------------------------------------------------------------------------------")
                print("-------------------------------------------------------------------------------------------------------------------")        

        dados_processo = {"nº": numero_processo, "processo": text_processo, "instancias": instancias }
        return dados_processo

    def undefault_process():        
        for e in processo_old:
            if e == "-" or e == "Processo" or e == "Petição":
                return True

    print(processo_old)
    print(processo_old.split())
    print(re.search(p_processo, processo_old))
    print(re.findall(p_OAB_1, processo_old))
    print(re.findall(p_OAB_2, processo_old))
    print(re.findall(p_OAB_3, processo_old))
    print(re.findall(p_OAB_4, processo_old))

    if re.search(p_processo, processo_old):
        s_ini = re.search(p_processo, processo_old).group()
        if re.findall(p_OAB_2, processo_old) != []:
            s_final = re.findall(p_OAB_2, processo_old)[ len(re.findall(p_OAB_2, processo_old)) - 1 ]
            return cat_process()
        elif re.findall(p_OAB_1, processo_old) != []:
            s_final = re.findall(p_OAB_1, processo_old)[ len(re.findall(p_OAB_1, processo_old)) - 1 ]
            return cat_process()
        elif re.findall(p_OAB_3, processo_old) != []:
            s_final = re.findall(p_OAB_3, processo_old)[ len(re.findall(p_OAB_3, processo_old)) - 1 ]
            return cat_process()
        elif re.findall(p_OAB_3, processo_old) != []:
            s_final = re.findall(p_OAB_3, processo_old)[ len(re.findall(p_OAB_3, processo_old)) - 1 ]    
            return cat_process()
        elif undefault_process():
            s_final = processo_old.split()[ len( processo_old.split() ) - 1 ]    
            return cat_process()
        else:
            print("Processo não foi definido corretamente")

'''
string_cobaia="Nº 1018818-97.2021.8.26.0114 - Processo Digital. Petições para juntada devem ser apresentadas exclusivamente por"
print(re.search(p_processo_2, string_cobaia))
'''
