#!/usr/bin/node
// This script will prints all char of a Star Wars movie

const req = require('request');
const ident = process.argv[2];
const pth = `https://swapi-api.alx-tools.com/api/films/${ident}`;

req.get(pth, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;
    for (const character of characters) {
      req.get(character, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const names = JSON.parse(body);
          console.log(names.name);
        }
      });
    }
  }
});
