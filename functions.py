from movie_list import movies

#Goes through movie list and prints every title
def print_every_movie_title (movie_list):
  for movies in movie_list:
    print(movies["title"])
print_every_movie_title(movies)


#A function that returns the length of the description 
def get_movie_description_length_1(movie):
    #description = movie.get('description', '')  
    #return len(description)
#description_length = get_movie_description_length_1(movies[0])
#print({description_length})

#Returns the length of each movie
def get_movie_description_length_2 (movie_length):
 for movies in movie_length:
  #print(len(movies["description"]))
get_movie_description_length_2 (movies)

#Returns the length of the movie description
def get_movie_description_length (movies):
    description = movies.get('description')
    return len(description)

#A function that takes data from a file and prints out a list of movies
import json 
def load_movies_data ():
  movies = []
  with open ('movies.json') as file:
    movies = json.load(file)
  return movies

#Return unquie list of genres 
def get_unique_genres(movie_list):
    unique_genres = set()
    for movie in movie_list:
        unique_genres.add(movie['genre'])
    return unique_genres

#Filters movie genre
def get_movies_in_genre(genre):
    genre_movies = [movie for movie in movies if movie['genre'] == genre]
    return genre_movies

#Genre choice
def get_user_genre_choice (genre):
  unique_genre = get_unique_genres(movies)
  print(unique_genre)
  genre_choice = input('Whats your genre?')
  return genre_choice


#show the movies in a selected genre
#genre = get_user_genre_choice (get_unique_genres)
#movie_list = get_movies_in_genre(genre)
#for index, movie in enumerate(movie_list, start=1):
  #print(f"{index}: {movie}")

#Prints genres 
def get_movie_by_index ():
#print out all the movies in the genre selected.
  genre = get_user_genre_choice (movies)
  movie_list = get_movies_in_genre(genre)
  for index, movie in enumerate(movie_list, start=1):
    print(f"{index}: {movie}")
#ask the user to select a movie by entering the index of the movie
  selected_movie_index = input('movie index?')
  print(f"{selected_movie_index}: {movie}")
  return
#get_movie_by_index ()


# The "get_user_genre_choice" function raises an error when you use a genre that is not in the dataset
def get_user_genre_choice():
  valid_genres = ['Action', 'Adventure', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Mystery', 'Sci-Fi', 'Thriller']
  while True:
        user_genre = input("Please enter your preferred genre: ")
        if user_genre in valid_genres:
            return user_genre
        else:
            print("Invalid genre choice. Please choose from the following genres:")
            print(valid_genres)
#get_user_genre_choice()

#The "get_user_genre_choice" function raises a ValueError exception when you use a genre that is not in the datase
def get_user_genre_choice():
    valid_genres = ['Action', 'Adventure', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Mystery', 'Sci-Fi', 'Thriller']
    while True:
        user_genre = input("Please enter your preferred genre: ")
        if user_genre in valid_genres:
            return user_genre
        else:
            raise ValueError("This is not a valid genre. Please choose from the following genres: " + ', '.join(valid_genres))