#!/usr/bin/node
const convertedNum = parseInt(process.argv[2]);
if (isNaN(convertedNum)) {
  console.log('Not a number');
} else {
  console.log('My number:', convertedNum);
}
