#!/usr/bin/node
const args = process.argv.slice(2);

const x = Number(args[0]);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  let i = 0;

  while (i < x) {
    console.log('X' .repeat(x));
    i++;
  }
}
