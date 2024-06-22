#!/usr/bin/node
const args = process.argv.slice(2);

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return factorial(n - 1) * n;
  }
}

console.log(factorial(Number(args[0])));
