#!/usr/bin/node
// This script will prints the number of movies
// where the character “Wedge Antilles” is present


const req = require('request');
function mov_inc (apiEndpoint) {
  const ch_id = 18;
  req.get(apiEndpoint, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const films = JSON.parse(body).results;
      let inc = 0;
      for (let k = 0; k < films.length; k++) {
        const characters = films[k].characters;
        for (let L = 0; L < characters.length; L++) {
          if (characters[L].includes(ch_id)) {
            inc++;
          }
        }
      }
      console.log(inc);
    }
  });
}

const args = process.argv.slice(2);

if (args.length === 1) {
  const apiEndpoint = args[0];
  mov_inc(apiEndpoint);
}
