# date % function
import random
from datetime import datetime

menu = (
    "Add Movie",
    "Pick Random Movie",
    "Exit"
)
#=======================================================
def show_menu():

    i = 1

    for choice in menu:
        print(f"{i}- {choice}")
        i += 1
#=========================================

def add_movie():

    movie_name = input("Enter Movie Name: ")

    file = open("movies.txt", "a")

    file.write(movie_name + "\n")

    file.close()

    print("Movie Added Successfully.")

#====================================
def time():

     today = datetime.now()

     print(f"Date: {today.day}/{today.month}/{today.year}")


def Pick_Random_Movie():

    file=open("movies.txt","r")

    movies=file.readlines()

    file.close()

    movie = random.choice(movies)

    time()

    print("Tonight's Movie:")
    print(movie)

#====================================


