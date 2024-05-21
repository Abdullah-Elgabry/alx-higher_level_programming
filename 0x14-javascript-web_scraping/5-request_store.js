#!/usr/bin/node
// This script will gets the contents of a webpage and stores it in a file.

const req = require('request');
const filesv = require('fs');
const args = process.argv.slice(2);

function swft (url, fileName) {
  req.get(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      filesv.writeFile(fileName, body, 'utf8', function (err) {
        if (err) {
          console.log(err);
        }
      });
    }
  });
}

if (args.length === 2) {
  const url = args[0];
  const fileName = args[1];
  swft(url, fileName);
}
