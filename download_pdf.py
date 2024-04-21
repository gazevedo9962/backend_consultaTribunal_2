from pathlib import Path
import requests
import sys
from string_bt import *
 
string_args=cat_string_list(sys.argv)
url, path = cat_arg("-u", string_args), cat_arg("-p", string_args)
filename = Path(path)
response = requests.get(url)
filename.write_bytes(response.content)
#print(response.content)
print(filename)
#Exemplo:
#cmd => py download_pdf.py -u "https://dje.tjsp.jus.br/cdje/getPaginaDoDiario.do?cdVolume=18&nuDiario=3912&cdCaderno=11&nuSeqpagina=263&uuidCaptcha=" -p "./diario2.pdf"
