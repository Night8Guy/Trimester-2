#!/usr/bin/node
const ARGV = process.argv;

const num = parseInt(ARGV[2]);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}