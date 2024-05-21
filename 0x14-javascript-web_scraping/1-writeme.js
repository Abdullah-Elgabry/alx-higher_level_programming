#!/usr/bin/node
// This script will writes a string to a file

const filesv = require('fs');
const path = process.argv[2];
const dta = process.argv[3];

filesv.writeFile(path, dta, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
