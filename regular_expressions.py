#regular expressions

import re

string = 'search inside of this text please'

print('search' in string)

a = re.search('this', string)

print(a.span())
print(a.start())
print(a.group())