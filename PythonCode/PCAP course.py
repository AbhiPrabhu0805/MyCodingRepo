#PCAP course


#Importing modules

#import sys
#import math
import sys, math
#from sys import exit as bye_bye
#from sys import exit
import random
import platform

#for name in dir(sys):
#    print(name, end=" --- ")


#sys.exit()
#bye_bye()

print("hello")

for name in dir(math):
    print(name,'\t')

#### Math modules ####
#ceil(), floor(), trunc()
#factorial()
#sqrt() --- square root
#hypot()  -- hypotenuse

print(random.random()) # -- random number between 0 & 1
print(random.random())
print(random.random())
    
random.seed(0)  # -- defining a seed
print(random.random()) # -- random number between 0 & 1
print(random.random())
print(random.random())

numbers=[1,2,3,4,5,6,7,8,9]
name="Abhimanyu"
names=["Abhi","Manu","Prabhu"]

print(random.choice(numbers)) # But it can return the same value multiple times
print(random.choice(name))
print(random.choice(names))

print(random.sample(numbers,1)) # This function avoids returning values already sampled and returns a list
print(random.sample(numbers,1))
print(random.sample(numbers,1))
print(random.sample(numbers,1))

print(platform.platform())

print(platform.platform(aliased=True, terse=True))

print(platform.machine())
print(platform.processor())
print(platform.system())
print(platform.python_implementation())
print(platform.python_version_tuple())
print(platform.version())

