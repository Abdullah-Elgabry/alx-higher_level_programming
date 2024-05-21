#!/usr/bin/node
// This script will display the status code of a GET request

const req = require('request');
const url = process.argv[2];

req(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
