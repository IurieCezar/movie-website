"""This module stores the instances of the class Movie, the information
and a list of them. It also calls the 'open_movie_page()' function from
'fresh_tomatoes module', this way running the whole program.
"""

import fresh_tomatoes
import media

passengers = media.Movie("Passengers",
                         "http://images.fandango.com/images/fandangoblog/passengersposter.jpg",
                         "https://www.youtube.com/watch?v=7BWWWQzTpNU")

momentum = media.Movie("Momentum",
                       "http://www.impawards.com/2015/posters/momentum_ver2.jpg",
                       "https://www.youtube.com/watch?v=bZDHKxXBzCM")

plastic = media.Movie("PLASTIC",
                      "http://www.flickeringmyth.com/wp-content/uploads/2014/04/Plastic-Movie-Poster-Julian-Gilbey.jpg",
                      "https://www.youtube.com/watch?v=Y6qJU5VtIVg")

life_partners = media.Movie("Life Partners",
                            "https://upload.wikimedia.org/wikipedia/en/e/e8/Life_Partners_poster_(2014).png",
                            "https://www.youtube.com/watch?v=AgCPs6iKF2w")

left_behind = media.Movie("Left Behind",
                          "http://images.christianpost.com/full/66965/the-official-left-behind-movie-poster.jpg",
                          "https://www.youtube.com/watch?v=GrXe8YDbzYs")

ice_age = media.Movie("Ice Age",
                      "http://www.impawards.com/2002/posters/ice_age.jpg",
                      "https://www.youtube.com/watch?v=AW9b6unX_wo")

movies = [passengers, momentum, plastic, life_partners, left_behind, ice_age]

fresh_tomatoes.open_movies_page(movies)
