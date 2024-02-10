const axios = require('axios').default;
const fs = require('fs');
const { argv } = require('process');
const command = require("./command");
// http://gazevedo996.pythonanywhere.com/
// "http://localhost:6546/"

const getdata = async () => {
    const url = "https://esaj.tjsp.jus.br/cdje/getPaginaDoDiario.do?cdVolume=18&nuDiario=3888&cdCaderno=10&nuSeqpagina=1&uuidCaptcha="    const response = await axios.get(url, {
        responseType: 'arraybuffer',
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS"
        }
      });
    const pdfcontents = response.data;
    console.log(response)
    await fs.writeFile('file.pdf', pdfcontents, function(err) {
                if(err) {
                return console.log(err);
                }
                console.log("The file was saved!");
                });

    }
getdata();

