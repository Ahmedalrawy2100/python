#============================================

class car:

    def __init__(self,color,speed,size):

        self.color=color
        self.speed=speed
        self.size=size
        

CarOne=car("white",255,"big")


print(f"speed car one is :{CarOne.speed}")



class student:

    def __init__(self,name,age):
       
        self.name=name
        self.age=age

    def show(self):
        print(self.name)
        print(self.age)

s1=student("ahmed",25)
s1.show()
