const { exec } = require('child_process');

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
module.exports = command  
