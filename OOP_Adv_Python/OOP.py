#object oriented programming in python


#everythinig in Python is an object

print("all the data types in Python")
print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))

#objects have methods and attributes 
# you create your own objects using the class keyword. 

 #  more and more technology requires thousands of lines. so you need classes

 #for example Amazon Delivery Drones can be broken down into different functionality and each can be its own classes

 #OOP is a paradigm is a way to think about our code and structure the code.

 #previous programming languages 
 
 #assembly language - really close to machine language
 # procedural code - C Programming Language

# class name should start with a Capital Letter
 
class Big_Object:
     pass

obj = Big_Object() # instantiating the object, creating a new object

print(type(Big_Object))
print("the type of class Big_Object is " + str(type(obj)))

#creating our own objects

class Player_Characters:
    def __init__(self,name):
        self.name = name

    def run(self):
      print("run")

player1 = Player_Characters('Johnny')

print(player1.name)
