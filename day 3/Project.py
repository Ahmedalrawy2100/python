# Welcome Message
print("Welcome to Student Management System")

# Menu
menu = (
    "Add Student",
    "Show Students",
    "Search Student",
    "Update Student",
    "Delete Student",
    "Exit"
)
students = [

    # {
    #     "name":"Ahmed",
    #     "age":25,
    #     "courses":["Python","Linux"]
    # },

    # {
    #     "name":"Ali",
    #     "age":20,
    #     "courses":["CCNA"]
    # },

    # {
    #     "name":"Mohamed",
    #     "age":30,
    #     "courses":["c++","CCNA"]
    # }

]

while True:

    #menu
    i=1
    for optino in menu:
        print(f"{i}-{optino}")
        i+=1
    # use choose
    num_choose=input("enter number please: ")

    if num_choose =="1":
        print("add student")
    elif num_choose =="2":
        print("show students")
    elif num_choose =="3":
        print('search student')
    elif num_choose =="4":
        print("update")
    elif num_choose =="5":
        print("delete")
    elif num_choose=="6":
       print( "bye")
       break
    else :
        print("invaled")


