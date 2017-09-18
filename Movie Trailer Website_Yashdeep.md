# Movie Trailer Webaite using Python
## Introduction
This is a code for a **Movie Trailer Website** which :
1. Shows the movie names along with their **posters**
2. Plays **Youtube trailers** of movies when the Movie Poster is clicked
3. Contains the information about the **storyline of the movie**

## Modules and Functions used in the Project
- 1. `Media.py` contains the class Movie which contains the information to be stored about the movie.
- 2. `Entertainment.py` contains the instances of the class Movie or the information about the movies to be displayed on the website
- 3. The module `webbrowser` is used to open the browser and play the youtube trailer
        -   funtion `showtrailer` which plays the youtube trailer  
- 4.  `freshtomatoes.py` contains the html code to create the website along with other functions.
        -   Takes a list of movies as input and creates and opens an HTML page or webbsite which contains the movies given to it.
        -  function `open_movies_page` which takes the array `movies` (contains list of movie to be included in the website) defined in `entertainment.py`

    
## Issues to consider
- A movie will not be displayed on the website until it is included in the array `movies` even if its instance has been created. So be sure to include in the array `movie`.

## Suggestions and Links
- Feel free to suggest interesting movies I can add to the website
- Download the file `fresh_tomatoes.py' from [here](https://s3.amazonaws.com/udacity-hosted-downloads/ud036/fresh_tomatoes.py)


    