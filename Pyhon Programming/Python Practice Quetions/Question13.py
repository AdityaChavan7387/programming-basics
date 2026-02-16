# Write a program to ask the user to enter names of their 3 favorite movies and store them in a list.

list_of_movies = []


movie_name1 = input("Enter the name of your favorite movie 1: ") 
movie_name2 = input("Enter the name of your favorite movie 2: ") 
movie_name3 = input("Enter the name of your favorite movie 3: ") 

list_of_movies.append(movie_name1)
list_of_movies.append(movie_name2)
list_of_movies.append(movie_name3)

print("Your favorite movies are: ", list_of_movies)


