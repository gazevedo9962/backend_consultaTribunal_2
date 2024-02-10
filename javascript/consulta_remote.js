const axios = require('axios').default;
const fs = require('fs');
const { argv } = require('process');
const command = require("./command");
// http://gazevedo996.pythonanywhere.com/
// "http://localhost:6546/"

function getdata () {
  axios.get("https://fastapi-selenium-production-30d6.up.railway.app/tjsp/servicos/consulta", {
        params: {
            "cadernos": argv[2] || 0,
            "secoes": argv[3] || 0
          },
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS"
        }
      })
  .then(function (response) {
    // manipula o sucesso da requisição
    console.log(response);
    //command("google-chrome", response.data.url);
  })
  .catch(function (error) {
    // manipula erros da requisição
    console.error(error);
  })
  .finally(function () {
    // sempre será executado
  });
}
getdata();
