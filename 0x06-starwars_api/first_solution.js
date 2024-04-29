#!/usr/bin/node

// const fetch = require('fetch');
async function fetchProducts (url) {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error(`Could not get products: ${error}`);
  }
}

const movieId = process.argv[2];
const fetchPromise = fetchProducts(`https://swapi-api.alx-tools.com/api/films/${movieId}`);
fetchPromise
  .then(async (data) => {
    const characters_url = data.characters;
    for (const item of characters_url) {
      const data1 = await fetchProducts(item);
      console.log(data1.name);
    }
  });
