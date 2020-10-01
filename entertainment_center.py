import media
import fresh_tomatoes
import webbrowser
import urllib
import json


# Taking name of movie as an argument.
def get_info(movie_name):
    # Get a response after opening the URL
    response = urllib.urlopen(
        "http://www.omdbapi.com/?t="+movie_name+"&y=&plot=short&r=json")
    # It reads the desired movie name
    # collects information corresponding to that movie.
    result = response.read()
    # Parsing values from JSON data.
    data = json.loads(result)
    # returns the information.
    return data

# A call to the get_info method of json API
# which takes the name of the movie as an argument
info = get_info("Minions")
# Reference of media which takes name of the movie, plot, poster URL
# and youtube link of the trailor as an argument.
minions = media.Movie(info['Title'], info['Plot'], info['Poster'],
                      "https://www.youtube.com/watch?v=P9-FCC6I7u0")

info = get_info("Conjuring 2")
conjuring = media.Movie(info['Title'], info['Plot'], info['Poster'],
                        "https://www.youtube.com/watch?v=KyA9AtUOqRM")

info = get_info("The Notebook")
notebook = media.Movie(info['Title'], info['Plot'], info['Poster'],
                       "https://www.youtube.com/watch?v=S3G3fILPQAU")

info = get_info("The vow")
vow = media.Movie(info['Title'], info['Plot'], info['Poster'],
                  "https://www.youtube.com/watch?v=7JoXHO3ceUY")

info = get_info("Annabelle")
annabelle = media.Movie(info['Title'], info['Plot'], info['Poster'],
                        "https://www.youtube.com/watch?v=jdUysoK6tdQ")

info = get_info("garfield")
pets = media.Movie(info['Title'], info['Plot'], info['Poster'],
                   "https://www.youtube.com/watch?v=5g1SLGRM6qU")
# array of movies.
movies = [minions, conjuring, notebook, vow, annabelle, pets]
# passing the array to open_movies method of fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
