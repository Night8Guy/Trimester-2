#!/usr/bin/node
exports.converter = function (base) {
    return function converToBaseN (num) {
      return (num.toString(base));
    };
  };