from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json

def write(path, dado, dadotype):
    #echo {dado} > \"{path}\" &&\
    print(f"{path}")
    if [dadotype == "json"]:
         arquivo = open(path, "w", -1, "utf-8")
         arquivo.write(json.dumps(dado, ensure_ascii=False, indent=4, sort_keys=True))
    else:
        arquivo = open(path, "w", -1, "utf-8")
        arquivo.write(str(dado))

def createDriver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    prefs = {"profile.managed_default_content_settings.images":2}
    chrome_options.headless = True


    chrome_options.add_experimental_option("prefs", prefs)
    myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    return myDriver

def getGoogleHomepage(driver: webdriver.Chrome) -> str:
    driver.get("https://www.google.com")
    return driver.page_source

def getTjsp_teste(driver: webdriver.Chrome, options_values) -> str:
    driver.get("https://dje.tjsp.jus.br/cdje/index.do")
    driver.implicitly_wait(20)
    wait = WebDriverWait(driver, 10)
    sleep(0.5)
    #select option cadernos ...
    select_cadernos = Select(driver.find_element(By.ID, "cadernos"))
    if int(options_values['cadernos']) < len(select_cadernos.options):
        select_cadernos.select_by_value(options_values['cadernos'])
    else:
        select_cadernos.select_by_value(0)    
    list_cadernos = []
    value_cadernos = 0
    
    for o in select_cadernos.options:
        list_cadernos.append({"text": o.text, "value": o.get_property("value"), "index": value_cadernos})
        value_cadernos = value_cadernos + 1

    sleep(0.5)
    #select option secao ...
    select_secoes = Select(driver.find_element(By.ID, "secoes"))
    if int(options_values['secoes']) < len(select_secoes.options):
        select_secoes.select_by_value(options_values['secoes'])
    else:
        select_secoes.select_by_value(0)
    list_secoes = []
    value_secoes = 0
    
    for o in select_secoes.options:
        list_secoes.append({"text": o.text, "value": o.get_property("value"), "index": value_secoes})
        value_secoes = value_secoes + 1
    
    #select_secoes.select_by_visible_text("Seção de Direito Privado")
    sleep(0.5)
    #consultar ...
    consultar = driver.find_element(By.ID, "consultar")
    consultar.click()
    
    # Wait for the new window or tab
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
    data = { 
            "url": url_geral,
            "source": driver.page_source,
            "list_cadernos": list_cadernos,
            "list_secoes": list_secoes
            }
    #write("./dados/secao.json", list_secoes, "json")
    write("./dados/cadernos.json", list_cadernos, "json")
    return data

def doBackgroundTask(inp):
    print("Doing background task")
    print(inp.msg)
    print("Done")

#rasc
#echos(list_texts_secoes)
#write("./dados/secao.json", list_secoes, "json")
#write("./dados/cadernos.json", list_cadernos, "json")
