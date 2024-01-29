const axios = require('axios').default;
const fs = require('fs');
const { argv } = require('process');
const command = require("./command");
//import download from 'downloadjs'
const download = require("downloadjs")
// http://gazevedo996.pythonanywhere.com/
// "http://localhost:6546/"

function getdata () {
    axios
        .get(`https://esaj.tjsp.jus.br/cdje/getPaginaDoDiario.do?cdVolume=18&nuDiario=3888&cdCaderno=10&nuSeqpagina=1&uuidCaptcha=`, {
            headers: this.headers,
            responseType: 'blob', // had to add this one here
        })
        .then(response => {
           const content = response.headers['content-type'];
           download(response.data, "diario.pdf", content)
        })
        .catch(error => console.log(error));
}
getdata();
