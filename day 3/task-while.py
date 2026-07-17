# while loop
i = 0
while i < 10:
    print(i)
    i+=1
print("Done with the loop")

#done

#while list
names = ["ahmed", "ali", "omar", "sara", "mona", "laila", "nour", "youssef", "hassan", "alrawy"]

i = 0
while i < len(names):

    print(f"#{str(1+i).zfill(2)}: {names[i]}")
    i+=1

print("Done with the loop")

#done