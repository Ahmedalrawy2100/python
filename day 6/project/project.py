# welcome 

import function as fun
print("Welcome to Lucky Movie")

while True:

    fun.show_menu()

    num_choose = input("Enter your choice: ")

    if num_choose == "1":

        fun.add_movie()

    elif num_choose == "2":

        fun.Pick_Random_Movie()

    elif num_choose == "3":
        
        print("Goodbye!")
        break 

    else:
        print("Invalid Choice.")

