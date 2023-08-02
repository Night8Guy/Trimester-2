#!/usr/bin/node
let xCounter;
let yCounter;
const ARGV = process.argv;
const num = parseInt(ARGV[2]);
if (ARGV[2] === undefined || isNaN(num)) {
  console.log('Missing size');
} else {
  let output = '';
  for (xCounter = 0; xCounter < num; xCounter++) {
    output += 'X';
  }
  for (yCounter = 0; yCounter < num; yCounter++) {
    console.log(output);
  }
}