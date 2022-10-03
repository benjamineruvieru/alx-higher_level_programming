#!/usr/bin/node
const list = process.argv.slice(2);
if (list.length === 1) {
  console.log(0);
} else if (list.length === 0) {
  console.log(0);
} else {
  console.log(list.reduce((a, b) => Math.max(parseInt(a), parseInt(b))));
}
