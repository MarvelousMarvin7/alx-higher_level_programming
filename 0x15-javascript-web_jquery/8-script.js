$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  success: function (data) {
    $('UL#list_movies').append(data.results.map(film => `<li>${film.title}</li>`));
  }
});
