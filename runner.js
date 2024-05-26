const { exec } = require('child_process');
const path = require('path');

//const scriptPath = path.join(__dirname, '/pre-env.sh');

exec(`bash ${__dirname}/pre-env.sh`, (error, stdout, stderr) => {
    if (error) {
        console.error(`Error executing script: ${error}`);
        return;
    }

    console.log({
        stdout: stdout,
        stderr: stderr
    });

});
