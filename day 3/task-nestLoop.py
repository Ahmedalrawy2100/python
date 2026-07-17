# This program will print a pattern of symbols based on user input for the number of rows, columns, and the symbol to be used


rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))
symbol=input("Enter the symbol: ")

for i in range(rows):
    for j in range(cols):
        print(symbol, end="")
    print("")


# some nested loops examples


cplus = 0
html = 0
python = 0
css = 0
js = 0
cc = 0

name=input("Enter your name: ")

if name == "ahmed":
   html=int(input("Enter your html score: "))
   css=int(input("Enter your css score: "))
   js=int(input("Enter your js score: "))

elif name == "ali":
   cplus=int(input("Enter your c++ score: "))
   python=int(input("Enter your python score: "))

elif name == "saed":
    cc=int(input("Enter your c++ score: "))

else:
    print("Sorry, you are not registered in the system")

mydict ={
        "ahmed":{
            "html": html,
            "css": css,
            "js": js
        },
        "ali":{
            "c++": cplus,
            "python": python
        },
        "saed":{
            "c#": cc
        }
    }

for name in mydict:
    print("")
    print(f"skill of {name} is:")
    
    for skill in mydict[name]:
        print(f"{skill} : {mydict[name][skill]}")
   
   #done