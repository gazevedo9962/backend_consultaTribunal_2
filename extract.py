from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json
import os
from selenium.webdriver.chrome.options import Options
#from manipulating_pdf import *

#Função para sair do Navegador
def tearDown(driver):
        driver.quit()

#Retorna o conteudo do arquivo, sem o símbolo de nova linha
def cat_file(path):
    arquivo = open(path, 'r')
    conteudo = arquivo.read()
    conteudo = str(conteudo).replace("\n", "")
    return conteudo 

#Escreve em um determinado arquivo um dado no formato (dadotype) json se especificado 
#caso não especificado o dado será escrito no formato padrão (texto).
def write(path, dado, dadotype):
    #echo {dado} > \"{path}\" &&\
    print(f"{path}")
    if dadotype:
        if dadotype == "json":
         arquivo = open(path, "w", -1, "utf-8")
         arquivo.write(json.dumps(dado, ensure_ascii=False, indent=4, sort_keys=True))
    else:
        arquivo = open(path, "w", -1, "utf-8")
        arquivo.write(str(dado))

#Inicializa um rôbo no navegador chorme com configurações especificas
#A principal é que o scraping será feito no modo sem UI.
def createDriver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    
    prefs = {"profile.managed_default_content_settings.images":2}
    chrome_options.headless = True

    chrome_options.add_experimental_option("prefs", prefs)
    myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    return myDriver

def getGoogleHomepage(driver: webdriver.Chrome) -> str:
    driver.get("https://www.google.com")
    data = driver.page_source
    driver.quit()
    return data

def consulta(driver: webdriver.Chrome, options_values) -> str:
    driver.get("https://dje.tjsp.jus.br/cdje/index.do")
    driver.implicitly_wait(20)
    wait = WebDriverWait(driver, 10)
    
    sleep(0.2)
    #***************** Select option cadernos ... *****************
    select_cadernos = Select(driver.find_element(By.ID, "cadernos"))
    if int(options_values['cadernos']) < len(select_cadernos.options):
        select_cadernos.select_by_value(options_values['cadernos'])
    else:
        select_cadernos.select_by_value(str(0))    

    sleep(0.2)
    #***************** Select option secao ... *******************
    select_secoes = Select(driver.find_element(By.ID, "secoes"))
    if int(options_values['secoes']) < len(select_secoes.options):
        select_secoes.select_by_value(options_values['secoes'])
    else:
        select_secoes.select_by_value(str(0))

    # Consultar ...
    consultar = driver.find_element(By.ID, "consultar")
    consultar.click()
    
    #***************** Wait for the new window or tab *********************
    wait.until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])
    print(driver.current_url)

    #************************** Def url PDF *******************************
    strings_url = driver.current_url.split(".do")
    string_inicial = "https://dje.tjsp.jus.br/cdje/getPaginaDoDiario.do"
    string_final = "&uuidCaptcha="
    url_geral = string_inicial + strings_url[1] + string_final

    #************************** Def dados PDF *******************************
    os.system("echo $(node ./javascript/genKey.js 5) > ./dados/tmp/var/random")
    random = cat_file('./dados/tmp/var/random') 
    print(random)
    name_pdf = f"arquivo_{random}"
    path_pdf = f"./dados/tmp/pdf/{name_pdf}.pdf"

    #Wait for frame pdf is open in new window
    #driver.execute_script("window.location.replace( document.getElementsByName('bottomFrame')[0].contentWindow.location.href )")
    #sleep(0.5)
    #print(driver.current_url)
    
    data = { 
            "url": url_geral,
            "source": driver.page_source
            }

    #************************ Armazenando dados ************************
    #cat \"./dados/tmp/log/files.txt\";
    write("./dados/resp_source/index.html", "<!DOCTYPE html>\n" + data["source"], False)
    os.system(f"\
        python download_pdf.py -u \"{url_geral}\" -p \"{path_pdf}\";\
        echo \"{name_pdf}.pdf\" >> \"./dados/tmp/log/files.txt\";\
        ls -a \"./dados/tmp/pdf\"; ")
        
    '''    
    ####################### IGONORE !!! #########################
    with open("./dados/json/cadernos.json") as arquivo:
        cadernos = json.load(arquivo)

    secoes = cadernos[int(options_values["cadernos"])]["secao"]
    value_secao_text = secoes[ int(options_values['secoes']) ]["text"]
    data["details_processo"] = raspar_pdf_2(path_pdf,value_secao_text)

     os.system(f"\
        rm -rf \"{path_pdf}\";\\
         ")
    ####################### IGONORE !!! #########################
    '''
    #Retornando data
    return data

def up_db(driver: webdriver.Chrome) -> str:
    driver.get("https://dje.tjsp.jus.br/cdje/index.do")
    driver.implicitly_wait(20)
    wait = WebDriverWait(driver, 10)
    
    sleep(0.2)
    #***************** Select option cadernos ... *****************
    select_cadernos = Select(driver.find_element(By.ID, "cadernos"))  
    list_cadernos = []
    value_cadernos = 0
    
    for caderno in select_cadernos.options:

        if int(value_cadernos) < len(select_cadernos.options):
            select_cadernos.select_by_value(str(value_cadernos))
        else:
            select_cadernos.select_by_value(str(0))

        sleep(0.2)
        select_secoes = Select(driver.find_element(By.ID, "secoes"))
        list_secoes = []
        value_secoes = 0   
        for secao in select_secoes.options:
            list_secoes.append({"text": secao.text, "value": secao.get_property("value"), "index": value_secoes})
            value_secoes = value_secoes + 1

        list_cadernos.append({"text": caderno.text, "value": caderno.get_property("value"), "index": value_cadernos, "secao": list_secoes})
        value_cadernos = value_cadernos + 1                
    
    sleep(0.2)
    #*************************** Consultar ... ***************************
    consultar = driver.find_element(By.ID, "consultar")
    consultar.click()
    
    #******************* Wait for the new window or tab *******************
    wait.until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])
    print(driver.current_url)
    strings_url = driver.current_url.split(".do")
    string_inicial = "https://dje.tjsp.jus.br/cdje/getPaginaDoDiario.do"
    string_final = "&uuidCaptcha="
    url_geral = string_inicial + strings_url[1] + string_final 
    #Wait for frame pdf is open in new window
    #driver.execute_script("window.location.replace( document.getElementsByName('bottomFrame')[0].contentWindow.location.href )")
    #sleep(0.5)
    #print(driver.current_url)

    #******************* def data *******************
    data = { 
            "url": url_geral,
            "source": driver.page_source,
            "list_cadernos": list_cadernos
            }

    #************************ def secoes ************************
    list_secoes = []
    for  x in list_cadernos:
        list_secoes.append(x["secao"])

    #************************ Armazenando dados ************************
    write("./dados/json/cadernos.json", list_cadernos, "json")
    write("./dados/json/secao.json", list_secoes, "json")
    write("./dados/resp_source/index.html", "<!DOCTYPE html>\n" + data["source"], False)
    
    #************************ Retornando data ************************
    return data    

def getTjsp_secao(driver: webdriver.Chrome, options_values) -> str:
    driver.get("https://dje.tjsp.jus.br/cdje/index.do")
    driver.implicitly_wait(20)
    wait = WebDriverWait(driver, 10)
    
    sleep(0.2)
    #***************** Select option cadernos ... *****************
    select_cadernos = Select(driver.find_element(By.ID, "cadernos"))
    if int(options_values['cadernos']) < len(select_cadernos.options):
        select_cadernos.select_by_value(options_values['cadernos'])
    else:
        select_cadernos.select_by_value(str(0))    

    sleep(0.2)
    #***************** Select option secao ... *****************
    select_secoes = Select(driver.find_element(By.ID, "secoes"))
    if int(options_values['secoes']) < len(select_secoes.options):
        select_secoes.select_by_value(options_values['secoes'])
    else:
        select_secoes.select_by_value(str(0))
    list_secoes = []
    value_secoes = 0
    
    for o in select_secoes.options:
        list_secoes.append({"text": o.text, "value": o.get_property("value"), "index": value_secoes})
        value_secoes = value_secoes + 1
    
    #select_secoes.select_by_visible_text("Seção de Direito Privado")
    #sleep(0.5)
    return list_secoes

def getTjsp_caderno(driver: webdriver.Chrome, options_values) -> str:
    driver.get("https://dje.tjsp.jus.br/cdje/index.do")
    driver.implicitly_wait(20)
    wait = WebDriverWait(driver, 10)
    
    sleep(0.2)
    #select option cadernos ...
    select_cadernos = Select(driver.find_element(By.ID, "cadernos"))
    list_cadernos = []
    value_cadernos = 0
    
    for o in select_cadernos.options:
        list_cadernos.append({"text": o.text, "value": o.get_property("value"), "index": value_cadernos})
        value_cadernos = value_cadernos + 1

    return list_cadernos

def doBackgroundTask(inp):
    print("Doing background task")
    print(inp.msg)
    print("Done")

#rasc - func - getTjsp_url
#echos(list_texts_secoes)
#write("./dados/secao.json", list_secoes, "json")
#write("./dados/json/cadernos.json", list_cadernos, "json")
#Exibindo page pdf source
#os.system("cat ./dados/resp_source/index.html") 
