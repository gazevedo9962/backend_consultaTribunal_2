const axios = require('axios').default;
const { exec } = require('child_process');
const fs = require('fs');
const { argv } = require('process');
// http://gazevedo996.pythonanywhere.com/
// "http://localhost:6546/"

async function command (command, args) {
  const commandArgs = `${command} "${args}"`;
  console.log(commandArgs);
  exec(commandArgs, (error, stdout, stderr) => {
      if (error) {
          console.log(`error: ${error.message}`);
          return
      }
      if (stderr) {
          console.log(`stderr: ${stderr}`);
      }
      console.log("==Tudo pronto para começar==")
  });
}

function getdata () {
  axios.get("https://fastapi-selenium-production-30d6.up.railway.app/servicos/consulta?cadernos=0&secoes=0", {
    params: {
      "cadernos": argv[2] || 0,
      "secoes": argv[3] || 0
    }
  })
  .then(function (response) {
    // manipula o sucesso da requisição
    console.log(response);
    command("chrome", response.data.url)
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
