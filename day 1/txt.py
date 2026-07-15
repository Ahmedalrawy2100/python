
#print welcome message
print("welcome to the profile program")


#get user input
name=str(input("what is your name? "))
age=int(input("what is your age? "))
country=str(input("what is your country? "))
height=float(input("what is your height? "))
learning_python=bool(input("do you learn python? (yes/no) :"))
opinion=bool(input("do you think python is useful in 2026? (yes/no) :"))


#print user profile
print("\n=========================")
print("your profile")
print("=========================")
print("name: ", name)
print("age: ", age)
print("country: ", country)
print("height: ", height)
print("learning python: ", learning_python)
print("opinion: ", opinion)
print("=========================")
print("Good luck with your python journey "+name)

#print("\nData types:")
print("name: ", type(name))
print("age: ", type(age))
print("country: ", type(country))
print("height: ", type(height))
print("learning python: ", type(learning_python))
print("opinion: ", type(opinion))
print("=========================")
#done
