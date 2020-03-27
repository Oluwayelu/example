'''
Create a function named password_generator that takes in the desired
password length as an argument/parameter and returns the generated
password as a string. The passwords generated are to be alphanumeric
containing upper and lower cases. If the password length is less than 8, tell the user that their password is weak.
'''

import string
from random import choice

def password_generator(pass_length): 
  chars = string.ascii_letters + string.digits
  if pass_length >= 8:
    return ''.join(choice(chars) for _ in range(pass_length))
  else:
    return 'Password is weak'

#test
print(password_generator(9))
