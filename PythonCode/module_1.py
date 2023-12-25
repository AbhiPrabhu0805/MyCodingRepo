'''print('What is your name?')
username=input("Enter your name:")
print('Hello!', username)
print("Hello Everyone",\
      "My name is",username,end='.\n',sep='-')'''

my_list=[1,2,3,4,5]
print(my_list)
print(my_list[::-1])
del my_list[2]
print(my_list)
my_list.append(2)
print(my_list)

my_tuple=(1,2,3,4,5)
print(my_tuple)
print(my_tuple[0:3])

dict={}
dict["John"]='A'
dict["Brown"]='B'
print(dict)

for i in dict.values():
    print(i)

def recursive_factorial_function(number):
    if number<=1:
        return 1
    return number * recursive_factorial_function(number-1)


print(recursive_factorial_function(4))