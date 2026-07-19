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
students = []

while True:

    #menu
    i=1
    for optino in menu:
        print(f"{i}-{optino}")
        i+=1
    # use choose
    num_choose=input("enter number please: ")

    if num_choose =="1":
        #name
        name=input("what 's your name ? ")
        if name =="admin":
            print("This name is not allowed.")
            continue

        #age
        while True:
            age = int(input("how old are you? "))
            if age >= 16:
                break
            print("Invalid age! Please enter a valid age.")

        #courses
        while True:
            courses_count = int(input("enter number of courses: "))
            if courses_count > 3:
                print("Maximum is 3 courses.")
            elif courses_count < 1:
                print("You must choose at least one course.")
            else:
                break
        

        courses = []
        for x in range(1, courses_count + 1):
            course = input(f"Enter course {x}: ")
            courses.append(course)

        student = {
           "name":name,
            "age":age,
            "courses":courses
                 }

        students.append(student)
        print("Student Added Successfully.")


    elif num_choose == "2":

     if not students:
        print("No Students Found.")

     else:

        for student in students:

            print(f"Name : {student['name']}")
            print(f"Age : {student['age']}")
            print("Courses :")

            for inside_courses in student['courses']:
              print(f"- {inside_courses}")
            
            print("-------------------")
        

    elif num_choose =="3":

        search_name=input("enter name :")
        found=False

        for student in students:

            if student['name'] == search_name:

              print(f"Name : {student['name']}")
              print(f"Age : {student['age']}")
              print("Courses :")

              for inside_courses in student['courses']:
                print(f"- {inside_courses}")
            
              print("-------------------")

              found=True

        if not found:
            print("Student Not Found.")



    elif num_choose == "4":


          search_name = input("Enter Name : ")
          found = False

          for student in students:

            if student["name"] == search_name:

              student["name"] = input("Enter New Name : ")

              print("Student Updated Successfully.")

              found = True

          if not found:
            print("Student Not Found.")

    elif num_choose == "5":

       search_name = input("Enter Name : ")
       found = False

       for student in students:

            if student["name"] == search_name:

              students.remove(student)

              print("Student Deleted Successfully.")

              found = True

       if not found :
        print("Student Not Found.")
        

    elif num_choose=="6":
       print( "bye")
       break
    else :
        print("invaled")


