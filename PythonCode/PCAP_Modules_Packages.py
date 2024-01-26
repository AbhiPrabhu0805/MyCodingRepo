#!/usr/bin/env python3 (tells unix based OS that it should inteprt it as a python file)

import sys, math
from sys import exit as bye_bye
from sys import *

for name in dir(math):
    print(name, end=" -- ")

def exit():
    print("I wanna exit")

exit()
#sys.exit()

## math modules
print(math.ceil(3.6))
print(math.floor(3.6))
print(math.trunc(3.6))
print(math.factorial(3))
print(math.hypot(3,4))

# random modules
import random
print(random.random())
print(random.random())
print(random.random())
random.seed(0)
print(random.random())
print(random.random())
print(random.random())
random.seed(0)
print(random.random())
print(random.random())
print(random.random())
numbers=[1,2,3,4,5,6,7,8,9,10]

names=["Abhi","Manu","Prabhu"]

print(random.choice(names))
print(random.choice(numbers)) ##but it might repeat values

print(random.sample(names,1)) ## returns a list!
print(random.sample(numbers,1))


import platform

print(platform.platform())


print(platform.platform(aliased=True, terse=True))

print(platform.machine())

print(platform.processor())

print(platform.system())

print(platform.python_implementation())

print(platform.python_version_tuple())

print(platform.version())

import random
 
def generate_tickets(ticket_count, max_number):
    list_to_return = random.sample(range(0, max_number), ticket_count)
    return list_to_return, random.sample(list_to_return, 1)


print(generate_tickets(2,10))

import own_module ## modules stored in __pycache__

print(sys.path) ##locations python checks for modules

#__init__.py is no longer necessary for packages
random.seed()
print(random.choice("Abhimanyu"))
print(random.choice("Abhimanyu"))
print(random.sample("Abhimanyu",1))

