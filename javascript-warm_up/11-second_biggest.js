#!/usr/bin/node

const argumentsList = process.argv.slice(2).map(Number);

if (argumentsList.length < 2) {
  console.log(0);
} else {
  argumentsList.sort((a, b) => b - a);
  console.log(argumentsList[1]);
}
