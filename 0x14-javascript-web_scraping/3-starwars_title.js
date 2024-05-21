#!/usr/bin/node
// This script will prints the title of a Star
// Wars movie where the episode number matches a given integer.

const req = require('request');
const mov = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + mov;

req(url, (error, response, body) => {
  if (error) { console.log(error); }
  const jsonBody = JSON.parse(body);
  console.log(jsonBody.title);
});
