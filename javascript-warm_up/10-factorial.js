#!/usr/bin/node
const ARGV = process.argv;
const num = parseInt(ARGV[2]);

console.log(nFactorial(num));

function nFactorial (n) {
  if (n === 0 || n === 1 || isNaN(num)) {
    return (1);
  } else {
    return (n * nFactorial(n - 1));
  }
}