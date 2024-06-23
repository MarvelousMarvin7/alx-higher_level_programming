#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const second = args.sort(function (a, b) {
    return b - a;
  })[1];
  console.log(second);
}
