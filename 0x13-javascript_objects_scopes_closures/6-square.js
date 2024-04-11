#!/usr/bin/node

/*
Square class that defines a square and inherits from Square of 5-square.js..
charPrint(c) that prints the rectangle using the character c
If c is undefined, use the character X
*/

module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
  }
};
