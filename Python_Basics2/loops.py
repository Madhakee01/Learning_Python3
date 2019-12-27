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
