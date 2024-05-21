#!/usr/bin/node
// This script will reads and prints the content of a file.

const path = process.argv[2];
const filesv = require('fs');

filesv.readFile(path, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
