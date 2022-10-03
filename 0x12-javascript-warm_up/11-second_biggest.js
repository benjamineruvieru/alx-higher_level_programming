#!/usr/bin/node
let list = process.argv.slice(2);
if (list.length === 1) {
  console.log(0);
} else if (list.length === 0) {
  console.log(0);
} else {
  const largest = list.reduce((a, b) => Math.max(parseInt(a), parseInt(b)));
  list.splice(list.indexOf(largest.toString()), 1);
  console.log(list.reduce((a, b) => Math.max(parseInt(a), parseInt(b))));
}
