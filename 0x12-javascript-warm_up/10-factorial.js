#!/usr/bin/node
const convertedNum = parseInt(process.argv[2]);
let factorial = 1;
if (isNaN(convertedNum)) {
  console.log(1);
} else {
  fac(1);
}
function fac (num) {
  factorial = num * factorial;
  const nextnum = num + 1;
  if (nextnum <= convertedNum) {
    fac(nextnum);
  } else {
    console.log(factorial);
  }
}
