#!/usr/bin/node

// This code will print -> My number: <first argument converted in integer>

const num = Math.floor(Number(process.argv[2]));
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
