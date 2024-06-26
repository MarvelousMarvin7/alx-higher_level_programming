#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let size = '';
      for (let j = 0; j < this.width; j++) {
        size += c;
      }
      console.log(size);
    }
  }
}

module.exports = Square;
