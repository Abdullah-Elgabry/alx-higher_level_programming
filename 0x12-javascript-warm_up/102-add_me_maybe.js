#!/usr/bin/node

// This function will -> increments and calls a function.

exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
