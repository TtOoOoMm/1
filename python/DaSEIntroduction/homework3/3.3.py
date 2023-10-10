import re
x = input()
if re.match('(^\d{15}$)|(^\d{17}([0-9]|x)$)', x):
    print('True')
else:
    print('False')