const axios = require('axios').default;
const fs = require('fs');
const { argv } = require('process');
const command = require("./command");
// http://gazevedo996.pythonanywhere.com/
// "http://localhost:6546/"

const getdata = async () => {
    const url = "https://esaj.tjsp.jus.br/cdje/getPaginaDoDiario.do?cdVolume=18&nuDiario=3888&cdCaderno=10&nuSeqpagina=1&uuidCaptcha="
    const response = await axios.get(url, {
        responseType: 'arraybuffer'
      });
    const pdfcontents = response.data;
    await fs.writeFile('file.pdf', pdfcontents, function(err) {
                if(err) {
                return console.log(err);
                }
                console.log("The file was saved!");
                });

    }
getdata();

