#!/usr/bin/node

// function that converts a number from base 10 -> base passed as argument

exports.converter = function (base) { return num => num.toString(base); };
