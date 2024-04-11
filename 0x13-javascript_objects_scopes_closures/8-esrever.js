#!/usr/bin/node

/*
function that returns the reversed version of a list..
without using built-in method reverse
*/

exports.esrever = function (list) {
  return list.reduceRight(function (array, current) {
    array.push(current);
    return array;
  }, []);
};
