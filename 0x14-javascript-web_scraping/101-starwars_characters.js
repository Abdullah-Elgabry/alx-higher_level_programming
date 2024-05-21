#!/usr/bin/node
// This script will prints all characters of a Star Wars movie


const argv = require('process').argv;
const req = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

function star_char (urls) {
  const url = urls.shift();
  req(url, (error, response, body) => {
    if (urls.length) {
      star_char(urls);
    }
    if (error) {
      console.log(error);
    }

    console.log(JSON.parse(body).name);
  });
}

req(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const characters = JSON.parse(body).characters;

  star_char(characters);
});
