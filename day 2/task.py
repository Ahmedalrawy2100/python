# #welcome to python programming
# print("welcome to the calculator program")
# num=input("This program will help you to add two numbers")


# first=int(num[0] )
# second=int(num[1] )

# print(first+second)
# 1
# #add two numbers

#acounting
# length=float(input("enter a length "))
# width=float(input("enter a width "))
# money=float(input("how much for 1 meter? "))

# area=length*width
# cost =area*money

# print("the area is: ", area)
# print("the cost is: ", cost)

# welcome to the dgree  
# print("welcome to the degree program")
# age=float(input("what is your degree? "))
# if age>=90:
#     print("congratulations you are well done")
# elif age>=75:
#     print("congratulations you are very good ")
# elif age>=50:
#     print("congratulations you are good ")
# else:
#     print("you are failed, try again next time")
# #code block
    

#welcome message
print("welcome to the profile program")

name=str(input("what is your name? "))
age=int(input("what is your age? "))
has_account=(input("do you have an account? (yes/no) :"))
is_admin=(input("are you an admin? (yes/no) :"))

print("\n=========================")
print("your profile")
print("=========================")
print("name: ", name)
print("age: ", age)



if age>=18 :
    if has_account=="yes"or has_account=="y" and is_admin=="yes" or is_admin=="y":
        print("welcome to the system admin "+name)
    elif has_account=="yes"or has_account=="y" and is_admin=="no" or is_admin=="n":
        print("welcome to the system user "+name)
    elif has_account=="no"or has_account=="n" :
        print("please create an account to access the system")
else:
    print("sorry you are not allowed to access the system")
  
