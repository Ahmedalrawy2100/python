# Welcome Message
print("Welcome to Student Management System")

name=""
age=0
courses=0

# Menu
options = [
    "Add Student",
    "Show Students",
    "Exit"
]

while True:

    # Print Menu
    i = 1
    for word in options:
        print(f"{i}-{word}")
        i += 1

    # User Choice
    num_choose = input("Choose a number: ")


    # -------------------------
    # Add Student
    # -------------------------

    if num_choose=="1":
        #name
        name=input("enter your name:")
        if name =="admin":
            print("This name is not allowed.")
            continue
        #age
        while True:
            age=int(input("Enter your age: "))
            if age > 0:
                break
            print("Invalid age! Please enter a valid age.")
        #courses
        while True:
            courses=int(input("How many courses?"))

            if courses > 5:
                print("Maximum is 5 courses.")

            elif courses < 1:
                print("You must choose at least one course.")

            else:
                break
        # Print Courses 
        for i in range(1, courses + 1):

           course_name = input(f"Enter Course {i}: ")

        print("\nStudent Added Successfully.")
    
    # -------------------
    # Show Student
    # -------------------

    elif num_choose =="2":
        if name=="":
            print("No student found.")
        else :
            print(f"\nName : {name}")
            print(f"Age : {age}")
            print(f"Number of Courses : {courses}")

    # -------------------
    # Exit
    # -------------------  

    elif num_choose =="3":
            print("Goodbye Ahmed.")
            break

    # -------------------
    # Wrong Choice
    # -------------------

    else:
        print("Invalid Choice.")

            

