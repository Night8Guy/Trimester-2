#!/usr/bin/node
let counter;
const ARGV = process.argv;
const num = parseInt(ARGV[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (counter = 0; counter < num; counter++) {
    console.log('C is fun');
  }
}