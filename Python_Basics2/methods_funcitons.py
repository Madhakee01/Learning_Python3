# mehtods vs Funtions 
# list()
# print()
# max()
# min()
#input()



# conditional logic

#if else conditions.

is_old = True
is_licences = True

#if age is 
#if this and that - true
# if this or that - true
if is_old and is_licences:
    print("you are old enough to drive, and you have a license!")
elif is_licences:
    print("you can drive now!")
else:
    print("you are not of age!")

print("okkokokok")


#truthy and falsy

print(bool('hello'))

#thruthy and falsy 
# all values are considered as truthy 
# some values like falsy are false, 0, 0.o, [], {} and etc


#conditional language very nice. 


password = '123'
username = 'keerthana'

#if password and username exist 

if password and username:
    print('you are old enough to drive, adn you have a license')
else:
    print('you are not of age!')



# Ternary Operator, one of the conditional expression

#conditon_if_true if condition else condition_if_else

is_friend = False
is_user = True
can_message = "message allowed" if is_friend else "not allowed to message"

# so the above message executes like this, if the is_friend is available (true) then you can message
# else you cannot message because he/she is not your friends

#short circuiting 
# using 0r instead of and

if is_friend or is_user:
    print('best friends forever')


#logical operator

print(4<5)
print(4>5)
print(4==5)
print(5>=5)
print(4<=5)

#not keyword.

print("using not method " + str(not(True)))



#logical operators exercises

is_magician = False
is_expert = False

if is_magician and is_expert:
    print("you are a master magician")
elif is_magician and not is_expert:
    print("at least you are getting there")
elif not is_magician:
    print("you need magic powers ")