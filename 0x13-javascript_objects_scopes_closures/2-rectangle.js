#!/usr/bin/node

// If width or height = 0 or not a positive integer, create an empty object

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }
};
