#!/usr/bin/node
let counter;
const ARGV = process.argv;
let bigNum = 0;
let secondBig = 0;

if (ARGV[2] === undefined) {
  console.log(0);
} else if (ARGV[3] === undefined) {
  console.log(0);
} else {
  for (counter = 2; counter < ARGV.length; counter++) {
    if (parseInt(ARGV[counter]) > bigNum) {
      bigNum = parseInt(ARGV[counter]);
    }
  }
  for (counter = 2; counter < ARGV.length; counter++) {
    if (parseInt(ARGV[counter]) > secondBig && ARGV[counter] < bigNum) {
      secondBig = parseInt(ARGV[counter]);
    }
  }
  console.log(secondBig);
}