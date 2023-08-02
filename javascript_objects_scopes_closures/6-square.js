#!/usr/bin/node
const DefSquare = require('./5-square');

class Square extends DefSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let yCounter;
    for (yCounter = 0; yCounter < this.height; yCounter++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;