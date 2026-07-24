
# welcome 
import function as fun


print("To Do List")

while True:

    fun.show_menu()

    num_choose = input("Enter your choice: ")

    if num_choose == "1":

        fun.Add_Task()

    elif num_choose == "2":

        fun.Show_Tasks()

    elif num_choose == "3":
    
         fun.Mark_Task_As_Done()
     
    elif num_choose == "4":
         
        fun.exit_program()
        
        break 

    else:
        print("Invalid Choice.")
