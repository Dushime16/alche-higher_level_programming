#!/usr/bin/node
const parsedNum = parseInt(process.argv[2], 10);

if (Number.isNaN(parsedNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parsedNum);
}
