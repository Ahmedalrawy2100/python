#welcome message
print("welcome to the profile program")

name=str(input("what is your name? "))
age=int(input("what is your age? "))
has_account=input("do you have an account? (yes/no) :")
is_admin=input("are you an admin? (yes/no) :")

print("\n=========================")
print("your profile")
print("=========================")
print("name: ", name)
print("age: ", age)
print("has account: ", has_account)
print("is admin: ", is_admin)


if has_account=="yes" or has_account=="y" and is_admin=="yes" or is_admin=="y":
    print("you can access the admin panel")
elif has_account=="yes" or has_account=="y" and is_admin=="no" or is_admin=="n":
    print("you can access the user panel")
elif has_account=="no" or has_account=="n" and is_admin=="no" or is_admin=="n":
    print("you can access the guest panel")
else:
    print("sorry you can't access any panel")

#done