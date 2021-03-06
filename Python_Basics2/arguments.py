#arguments

# *args and **kwargs, arguments and keyword arguments

#for multiple arguments use the symbol *

def super_functions(*args, **kwargs):
    total = 0
    print(kwargs)
    for items in kwargs.values():
        total += items
    print(args)
    return sum(args) + total

print(super_functions(1,2,3,4,5, num1=5, num2=10))


#RuleL params, *argsm default parameters, **kwargs

def super_functions1(name, *args, i='hi', **kwargs):
    total1 = 0
    for items in kwargs.values():
        total1 += items
    
    return sum(args) + total1

print(super_functions1('Andy', 1,2,3,4,5, num1=5, num2=10))


# finding the highest even

def highest_even(li):
    evens = []
    for item in li:
        if item in li:
            evens.append(item)
    return max(evens)

print(highest_even([10,1,2,3,4,8]))

#scope - what variabless do you have , who has access to who

if True:
    x  = 10

def some_func():
    total = 100

print(x)

#global keyword

total2 = 0

def count(total):
    global total2
    total2 += 1
    return total2

count(total2)
count(total2)
print(count(total2))


#non local keyword - not a global variable but want to use a variable outside of scope

