
from datetime import datetime

class Task:
    def __init__(self, title, status="Pending"):
        self.title = title
        self.status = status


menu = (
    "Add Task",
    "Show Tasks",
    'Mark Task As Done',
    "Exit"
)

Tasks=[]
#==========================================
def show_menu():

    i = 1

    for choice in menu:
        print(f"{i}- {choice}")
        i += 1
#=========================================

def Add_Task():

    task_name= input("Enter Task Name: ")

    task=Task(task_name)

    Tasks.append(task)

    print("task Added Successfully.")

#====================================
def time():

     today = datetime.now()

     print(f"Date: {today.day}/{today.month}/{today.year}")


def Show_Tasks():


    if not Tasks:
        print(" No Tasks Found")

    else:
     i=1
     for MyTask in Tasks:
         
         print(f"{i}-{MyTask.title} = {MyTask.status}")
         i+=1

    time()

#====================================

def Mark_Task_As_Done():

    search = input("Enter Task Name: ")

    found = False

    for task in Tasks:

        if task.title == search:

            task.status = "Done"
            found = True

    if found:

        print("Task Updated Successfully.")

    else:

        print("Task Not Found.")

#========================================

def  exit_program():

    print("Goodbye!")
    