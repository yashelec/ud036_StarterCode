import fresh_tomatoes  #module which includes the code to create an html page and fetch the movie info to the webpage
import media  #module which includes the class Movie
shawshank_redemption=media.Movie("Shawshank Redemption",
                                 "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                                 "http://www.impawards.com/1994/posters/shawshank_redemption_ver1.jpg",
                                 "https://www.youtube.com/watch?v=6hB3S9bIaco") 
dark_knight=media.Movie("The Dark Knight",
                        "When the menace known as the Joker emerges from his mysterious past,he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
                        "http://www.impawards.com/2008/posters/dark_knight.jpg","https://www.youtube.com/watch?v=_PZpmTj1Q8Q")
fightclub=media.Movie("Fight Club",
                      "An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more.",
                      "http://www.flore-maquin.com/wp-content/uploads/Fight_club_RVB_721.jpg",
                      "https://www.youtube.com/watch?v=_XgQA9Ab0Gw")
interstellar=media.Movie("Interstellar",
                         "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
                         "http://www.joblo.com/timthumb.php?src=/posters/images/full/interstellar-mcconaughey.jpg&h=600&q=100","https://www.youtube.com/watch?v=zSWdZVtXT7E")
forrest_gump=media.Movie("Forrest Gump",
                         "JFK, LBJ, Vietnam, Watergate, and other history unfold through the perspective of an Alabama man with an IQ of 75.",
              "http://www.impawards.com/1994/posters/forrest_gump.jpg","https://www.youtube.com/watch?v=uPIEn0M8su0")
pulp_fiction=media.Movie("Pulp Fiction",
                         "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
                         "http://www.impawards.com/1994/posters/pulp_fiction.jpg","https://www.youtube.com/watch?v=s7EdQ4FqbhY")

movies=[shawshank_redemption,dark_knight,fightclub,interstellar,forrest_gump,pulp_fiction]      #list of movies instances. The module fresh tomatoes.py fetches the info of the movie instance
                                                                                                #mentioned in this list only to display on the webpage.  

fresh_tomatoes.open_movies_page(movies) #function defined in fresh tomatoes.py to open the movies page and display the movie info of the movies listed in the list "movies"



