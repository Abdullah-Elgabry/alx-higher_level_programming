#!/usr/bin/node
// This script will prints all char of a Star Wars movie

const argv = require('process').argv;
const req = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

req(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const char = JSON.parse(body).char;
  for (const x in char) {
    req(char[x], (error, response, body) => {
      if (error) {
        console.log(error);
      }

      const name = JSON.parse(body).name;
      console.log(name);
    });
  }
});
