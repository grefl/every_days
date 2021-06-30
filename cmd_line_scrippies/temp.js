const fs = require('fs');

const [cmd, country] = process.argv.slice(2)

const SET_COUNTRY = '--set-country';
const LIST_COUNTRIES = '--list-countries';
const AVAILABLE_CMDS = '--cmds';
const accepted_types = ['SWEDEN', 'REST', 'SPAIN'];




if (cmd === SET_COUNTRY) {
  
  console.log('setting country');

  if (accepted_types.includes(country)) {

    try {
    
      const str =  fs.readFileSync('./test.json')?.toString();  
      const json = JSON.parse(str);
      
      json.APP_VERSION = country;
      fs.writeFileSync('./test.json', JSON.stringify(json, null, 2))
    } catch(e) {

      if (e.code === 'ENOENT') error('no such file')
      else error(e);
    }
    
  }

  else {
    error(`"${country}" is not an accepted country. Use "--list-countries" to see available countries.`);
  }

}

else if (cmd === AVAILABLE_CMDS){
  console.log(`use "--set-country"`); 
}

else if (cmd === LIST_COUNTRIES) {
  console.log(`Use ${accepted_types.join(' or ')}`);
}

else {
  error(`"${cmd}" is not an accepted cmd. Use "--cmds" to see available commands.`);
}

function error(msg) {
  throw new Error(msg);
}
