const axios = require('axios').default;
const fs = require('fs');
const { argv } = require('process');
const command = require("./command")
// http://gazevedo996.pythonanywhere.com/
// "http://localhost:6546/"

function getdata () {
  axios.get("https://fastapi-selenium-production-30d6.up.railway.app/tjsp/cadernos", {
    params: {
      "teste": "Olá",
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
    // sempre será executado
  });
}
getdata();
