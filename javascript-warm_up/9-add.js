#!/usr/bin/node
const ARGV = process.argv;
const num1 = parseInt(ARGV[2]);
const num2 = parseInt(ARGV[3]);

console.log(add(num1, num2));

function add (a, b) {
  return a + b;
}