from movie_list import movies



print("Welcome to movie assist!")

movie_list_answer = input("Do you want to see what we have available?")
if movie_list_answer == "Yes":
    from functions import print_every_movie_title
    print(print_every_movie_title(movies))

movie_list_genre = input("Do you want to see the genre list?")
if movie_list_genre == "Yes":
    from functions import get_unique_genres
    print(get_unique_genres (movies))

movie_genre_pick_answer = input("What genre do you want?")
def get_movies_in_genre(genre):
    genre_movies = [movie for movie in movies if movie['genre'] == genre]
    return genre_movies
if movie_genre_pick_answer == get_movies_in_genre:
        print(get_movies_in_genre(genre))
    


#prints list of movies 
#Returns genre list
#filters movies by genre
#select genre choice
#select movie by genre
