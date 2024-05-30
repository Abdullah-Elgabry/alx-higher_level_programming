// fetch all movies from api and add them into list

let url = 'https://swapi.co/api/films/?format=json';
$.get(url, function (data) {
  let movies = data.results;
  for (let mov of movies) {
    $('ul#list_movies').append(`<li>${film.title}</li>`);
  }
});
