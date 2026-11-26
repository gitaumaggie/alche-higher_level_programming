#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;

    const count = films.filter(film =>
      film.characters.some(character => character.endsWith('/18/'))
    ).length;

    console.log(count);
  }
});
