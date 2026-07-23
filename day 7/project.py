print("Pet System")

pet1 = None


class Pet:

    def __init__(self, name, pet_type, age):
        self.name = name
        self.pet_type = pet_type
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Type: {self.pet_type}")
        print(f"Age: {self.age}")


while True:

    print("1- Create Pet")
    print("2- Show Pet")
    print("3- Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        pet_type = input("Enter Type: ")

        try:
            age = int(input("Enter Age: "))

            pet1 = Pet(name, pet_type, age)

            print("Pet Created Successfully.")

        except Exception:
            print("Invalid Age!")

    elif choice == "2":

        if pet1 is None:
            print("No Pet Found.")

        else:
            pet1.show_info()

    elif choice == "3":

        print("Goodbye!")
        break

    else:
        print("Invalid Choice.")