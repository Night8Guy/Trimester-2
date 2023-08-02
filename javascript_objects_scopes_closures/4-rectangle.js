#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if (w >= 1 && h >= 1) {
        this.width = w;
        this.height = h;
      }
    }
  
    print () {
      let yCounter;
      for (yCounter = 0; yCounter < this.height; yCounter++) {
        console.log('X'.repeat(this.width));
      }
    }
  
    rotate () {
      const temp = this.width;
      this.width = this.height;
      this.height = temp;
    }
  
    double () {
      this.width *= 2;
      this.height *= 2;
    }
  }
  
  module.exports = Rectangle;