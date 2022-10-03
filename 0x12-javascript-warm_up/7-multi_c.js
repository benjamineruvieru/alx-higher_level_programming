#!/usr/bin/node
const convertedNum = parseInt(process.argv[2]);
if (isNaN(convertedNum)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < convertedNum; i++) {
    console.log('C is fun');
  }
}
