#!/usr/bin/node
/* prints the title of a Star Wars movie where the episode
   number matches a given integer */

const request = require('request');
const episode = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${episode}`;

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log('statusCode:', response.statusCode);
  }
});
