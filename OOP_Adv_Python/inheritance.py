# inheritance

#all the users must be signed in , so we use inheritance

class User:
    def sign_in(seld):
      print('Logged In')

class Wizard(User): #users, we have to pass the parent class user to inherit sign in method
    def __init__(self, name, power):
        self.name = name 
        self.power = power
    def attack(self):
        print(f"attacking with power of {self.power}")

class Archer(User): #users 
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows: arrows left- {self.num_arrows}")


wizard1 = Wizard('Peter', 50)
archer1 = Archer('Mary', 100)

wizard1.attack()
archer1.attack()

#print(wizard1.sign_in())  

#you abstract the User class because both the archer and wizard share these code

#to check if something is an instance of the class you would use isinstance function
wizard2 = Wizard('happy', 60)

print(isinstance(wizard2, Wizard)) #return true of false, in this case it is true

# the bases class of all objects is Object
print(isinstance(wizard2, object)) # you still get true

 #polymorphism, allows us to have many forms, it gives us the ability to redefine methods in many forms
 # 
def player_attack(char):
     char.attack() # the object you pass into it calls different attack methodss

player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()