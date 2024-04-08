#!/usr/bin/node

//This code will print -> the first argument passed to it.

console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : process.argv[2]);
