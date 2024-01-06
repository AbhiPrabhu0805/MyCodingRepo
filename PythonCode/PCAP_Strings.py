#ASCII - AMerican Standard Code for Information Interchange

## UTF-8 - unicode, simialr to ASCII, but cant store up to i million different characters vs 256 in ASCII



print("Hi there".upper())

print(''' HI There
      my name is Abhimanyu''')

print(len(''' HI There
      my name is Abhimanyu'''))

text="Hi there"

print(text)

#del text
#print(text)

# space has the lower ascii value of any english character

print(ord(' '))
print(ord('a'))
print(ord('A'))
print(ord(';'))
print(ord('@'))
print(ord('z'))
print(chr(60))


## searching in string

print("Hi there".index('i'))
#print("Hi there".index('a')) will return error

print("Hi there".find('i'))
print("Hi there".find('a')) # wont return error, but will return -1

print("Hi there".find('i',1,5))

print("Hi there".rfind('e',1,5)) #searches from the end of the string

print("Hi there".rfind('e')) #searches from the end of the string


print("adrain".isalnum())
print("adrain".isalpha())
print("adrain".isupper())
print("adrain".islower())
print("adrain".isspace())  #Accepts new line character as space as well