const axios = require('axios').default;
const { exec } = require('child_process');
const fs = require('fs');
const { argv } = require('process');
// http://gazevedo996.pythonanywhere.com/
// "http://localhost:6546/"
function getdata () {
  axios.get("https://fastapi-selenium-production-30d6.up.railway.app/servicos/consulta?cadernos=0&secoes=adqadq", {
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
    // sempre será executado
  });
}
getdata();
