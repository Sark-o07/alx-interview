#!/usr/bin/node
const request = require('request');

// This function returns a Promise object holding the JSON Data
function fetchData(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const data = JSON.parse(body);
        resolve(data);
      } else {
        reject(error);
      }
    });
  });
}

// Function to fetch data for a single actor URL
async function fetchActorData(actorUrl) {
  const actorData = await fetchData(actorUrl);
  console.log(actorData.name);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
const filmdata = fetchData(url);
filmdata.then(
  async (filmData) => {
    const charactersUrl = filmData.characters;
    // Fetch data for each actor URL one by one
    for (const actorUrl of charactersUrl) {
      await fetchActorData(actorUrl);
    }
  },
);
