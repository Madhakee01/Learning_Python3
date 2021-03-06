# loops: for and while , and range


#this for loop prints every character in the string "zero to mastery"
# each character printed in separate lines


for item in "zero to mastery":
    print(item)
print()
for item1 in {1,2,3,4,5}:
    print(item1)


# { set}, (tuple), and (dictionary)

for item2 in (1,2,3,4,5):
    for x in ['a','b','c']:
        print(item2, x, 'c')


    
#iterable  , an object or collection that can be iterated over and over agian

#iterable - list, dictionaty, tuple, set, adn string and etc. 

user = {
    'name': 'Nancy',
    'age': 5006, 
    'can_swim': False
}

print("The items in a dictionary: ")

#items methods

for list1 in user.items():
    print(list1)
  
#value methods
#this prints the values of each key
for list2 in user.values():
    print(list2)

#key methods
#this prints the keys of each key

for list3 in user.keys():
    print(list3)

#printing both key, and values in one single line

print("Both the key and values in a dictionary at the same time: ")

for key, value in user.items():
    print(key, value)

# exercise tricky 

#to count the number of elements and sum in a list

print("to count the number of elements and it sum in a list")

my_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0

for items in my_list :
    counter = counter + items

print(counter)


# range function ()
# it gives a range object of (0,100)

print(range(100))

 
 #using a loop to print 100 numbers in a loop

for number in range(0,100):
     print(number)


# jumping by a certain value in a range
#to print the even numbers
print("To print the even values using a range function in a for loop")
for some in range(0,10,2): 
    print(some)\

#enumerate () function

for i, char in enumerate('Hellooo'):
    print(i, char)

for i, char in enumerate([1,2,3]):
    print(i,char)

#it prints the i value of all the wonderful things.


#finding 50 in the range of 100

for i,char in enumerate(list(range(100))):
   print(i,char)
   if char == 50:
        print(f'index of 50 i: {i}')


# <<<<>>>><<<<>>> While Looops <><><><><><><
#infinite loops can be very dangerous. 
# be careful of indentation in python

i = 0
while i < 50:
    print(i)
    i += 1
else:
    print("done with all the work")
    
# break, continue and pass 

print()

my_list1 = [1,2,3]

for item in my_list1:
    print(item)

#using lists and while loop
k = 0
while k< len(my_list1):
    print(my_list1[k])
    k += 1

#input while loop and etc

while True:
    response = input('Say Something: ')
    if(response == 'bye'):
        break

  #when continue is used .... you can use it to go back to top of the loop again

  # pass is sused to pass to the next line

for item in my_list1:
    pass

#Graphical User Interface

#exercise

#developers code
#clean
#Readability
# predictibility


picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for image in picture:
    for pixel in image:
        if(pixel): #if it is 1 
            print('*', end="")
        else: 
            print(' ', end = "")
    print('') #need a new line after every row


#
         
some_list = ['a','b','c','b', 'd', 'm', 'n', 'n']
print()
duplicates = [ ]

for value in some_list:
     if some_list.count(value) >  1: #checks if there is a duplicatr
      if value not in duplicates:
        duplicates.append(value)

print(duplicates)

 



