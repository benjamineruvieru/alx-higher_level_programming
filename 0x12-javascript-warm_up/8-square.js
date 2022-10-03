#!/usr/bin/node
const convertedNum = parseInt(process.argv[2]);
if (isNaN(convertedNum)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < convertedNum; i++) {
    console.log('X'.repeat(convertedNum));
  }
}
