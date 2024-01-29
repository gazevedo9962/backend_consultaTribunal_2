
const axios = require('axios').default;
const fs = require('fs');
const { argv } = require('process');
const command = require("./command")
// http://gazevedo996.pythonanywhere.com/
// "http://localhost:6546/"

function getdata () {
  axios.get("http://0.0.0.0:5896/tjsp/servicos/consulta/cadernos", {
    params: {
        "cadernos": argv[2] || 0,
        "secoes": argv[3] || 0
    }
  })
  .then(function (response) {
    // manipula o sucesso da requisição
    console.log(response);
  })
  .catch(function (error) {
    // manipula erros da requisição
    console.error(error);
  })
  .finally(function () {
    // sempre serÃ¡ executado
  });
}
getdata();
