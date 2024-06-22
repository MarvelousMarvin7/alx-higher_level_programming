#!/usr/bin/node
const args = process.argv.slice(2);

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  args.forEach((arg) => {
    console.log(`${arg}`);
  });
}
