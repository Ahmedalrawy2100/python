# date % function
import os
import random
from datetime import datetime

menu = (
    "Add Movie",
    "Pick Random Movie",
    "Exit"
)
#=======================================================
# Get the path to movies.txt in the same directory as this script
movies_file = os.path.join(os.path.dirname(__file__), "movies.txt")

def show_menu():

    i = 1

    for choice in menu:
        print(f"{i}- {choice}")
        i += 1
#=========================================

def add_movie():

    movie_name = input("Enter Movie Name: ")

    file = open(movies_file, "a")

    file.write(movie_name + "\n")

    file.close()

    print("Movie Added Successfully.")

#====================================
def time():

     today = datetime.now()

     print(f"Date: {today.day}/{today.month}/{today.year}")


def Pick_Random_Movie():

    file=open(movies_file,"r")

    movies=file.readlines()

    file.close()

    movie = random.choice(movies)

    time()

    print("Tonight's Movie:")
    print(movie)

#====================================


